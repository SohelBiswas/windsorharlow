/**
 * Windsor Harlow — enquiry endpoint.
 *
 * One AWS Lambda behind one Function URL. It takes the JSON the contact form
 * posts, checks it, and sends two emails through SES: the enquiry to you, and
 * an acknowledgement to the person who sent it.
 *
 * Runtime: nodejs20.x   Handler: enquiry-lambda.handler   Memory: 256MB
 * Environment variables:
 *   TO_ADDRESS     business@windsorharlow.com
 *   FROM_ADDRESS   an address on a domain verified in SES
 *   ALLOW_ORIGIN   https://windsorharlow.com
 */
import { SESv2Client, SendEmailCommand } from "@aws-sdk/client-sesv2";

const ses = new SESv2Client({});
const TO = process.env.TO_ADDRESS;
const FROM = process.env.FROM_ADDRESS;
const ORIGIN = process.env.ALLOW_ORIGIN || "*";

/* Crude per-instance rate limit. Not a security boundary — it just stops one
   source hammering the endpoint between cold starts. Real abuse control is the
   honeypot below plus SES's own sending limits. */
const seen = new Map();
const WINDOW_MS = 60_000;
const MAX_PER_WINDOW = 3;

const cors = {
  "Access-Control-Allow-Origin": ORIGIN,
  "Access-Control-Allow-Headers": "Content-Type",
  "Access-Control-Allow-Methods": "POST,OPTIONS",
  "Content-Type": "application/json",
};

const reply = (code, body) => ({ statusCode: code, headers: cors, body: JSON.stringify(body) });

/* Header values end up inside an email. Strip anything that could start a new
   header line — this is the classic header-injection route. */
const clean = (s, max) => String(s ?? "").replace(/[\r\n]+/g, " ").trim().slice(0, max);

export const handler = async (event) => {
  const method = event.requestContext?.http?.method || event.httpMethod;
  if (method === "OPTIONS") return { statusCode: 204, headers: cors, body: "" };
  if (method !== "POST") return reply(405, { error: "Method not allowed" });

  let data;
  try {
    data = JSON.parse(event.body || "{}");
  } catch {
    return reply(400, { error: "Malformed request" });
  }

  /* Honeypot: a field no human sees and no human fills. Answer 200 so a bot
     believes it succeeded and does not retry with a different shape. */
  if (clean(data.website, 200)) return reply(200, { ok: true });

  const name = clean(data.name, 120);
  const email = clean(data.email, 200);
  const detail = String(data.detail ?? "").trim().slice(0, 5000);

  if (!name || !email || !detail) return reply(400, { error: "Name, email and detail are required" });
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) return reply(400, { error: "That email address is not valid" });

  const ip = event.requestContext?.http?.sourceIp || "unknown";
  const now = Date.now();
  const hits = (seen.get(ip) || []).filter((t) => now - t < WINDOW_MS);
  if (hits.length >= MAX_PER_WINDOW) return reply(429, { error: "Too many enquiries. Try again shortly." });
  seen.set(ip, [...hits, now]);

  const company = clean(data.company, 160) || "—";
  const practice = clean(data.practice, 80) || "—";
  const model = clean(data.model, 80) || "—";
  const timeline = clean(data.timeline, 80) || "—";

  const text = [
    `Name:      ${name}`,
    `Email:     ${email}`,
    `Company:   ${company}`,
    `Practice:  ${practice}`,
    `Model:     ${model}`,
    `Timeline:  ${timeline}`,
    `IP:        ${ip}`,
    "",
    "Detail:",
    detail,
  ].join("\n");

  const send = (to, subject, body, replyTo) =>
    ses.send(new SendEmailCommand({
      FromEmailAddress: FROM,
      Destination: { ToAddresses: [to] },
      ReplyToAddresses: replyTo ? [replyTo] : undefined,
      Content: { Simple: {
        Subject: { Data: subject, Charset: "UTF-8" },
        Body: { Text: { Data: body, Charset: "UTF-8" } },
      } },
    }));

  try {
    /* Reply-To is the enquirer, so hitting reply in your inbox just works. */
    await send(TO, `New enquiry — ${practice} — ${company === "—" ? name : company}`, text, email);
  } catch (err) {
    console.error("enquiry send failed", err);
    return reply(502, { error: "Could not send the enquiry" });
  }

  /* The acknowledgement is best-effort. If it fails the enquiry is already
     delivered, and telling the sender otherwise would be wrong. */
  try {
    await send(email, "We have your enquiry — Windsor Harlow",
      [`Hello ${name.split(" ")[0] || name},`, "",
       "Your enquiry reached us and a senior engineer will read it.",
       "You will have a reply within one business day.", "",
       "For reference, this is what you sent:", "", detail, "",
       "— Windsor Harlow"].join("\n"));
  } catch (err) {
    console.warn("acknowledgement failed (enquiry was delivered)", err);
  }

  return reply(200, { ok: true });
};
