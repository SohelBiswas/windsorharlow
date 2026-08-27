# Enquiry endpoint — deployment

The site works without this. Until `window.WH_API` is set, the contact form
composes the enquiry and hands it to the visitor's mail client, showing them
the text so nothing is lost if that fails. This makes the form send by itself.

Roughly forty minutes, most of it waiting on AWS.

## 1. Verify the sending domain in SES

In the SES console, **Verified identities → Create identity → Domain**, enter
`windsorharlow.com`, and add the DKIM records it gives you to your DNS.
Verification usually completes within an hour.

**Then request production access** (SES → Account dashboard). A new SES account
is in sandbox mode and can only send to addresses you have separately verified,
which would mean acknowledgement emails to enquirers silently fail. Approval
takes a day or two, so start it early.

## 2. Create the function

```bash
mkdir wh-enquiry && cd wh-enquiry
cp /path/to/enquiry-lambda.mjs .
npm init -y && npm install @aws-sdk/client-sesv2
zip -r function.zip enquiry-lambda.mjs node_modules package.json

aws lambda create-function \
  --function-name wh-enquiry \
  --runtime nodejs20.x \
  --handler enquiry-lambda.handler \
  --zip-file fileb://function.zip \
  --role arn:aws:iam::ACCOUNT_ID:role/wh-enquiry-role \
  --timeout 15 --memory-size 256 \
  --environment "Variables={TO_ADDRESS=business@windsorharlow.com,FROM_ADDRESS=noreply@windsorharlow.com,ALLOW_ORIGIN=https://windsorharlow.com}"
```

The execution role needs the basic Lambda logging policy plus one statement:

```json
{ "Effect": "Allow", "Action": ["ses:SendEmail"], "Resource": "*" }
```

## 3. Give it a URL

```bash
aws lambda create-function-url-config \
  --function-name wh-enquiry --auth-type NONE

aws lambda add-permission \
  --function-name wh-enquiry --statement-id public-url \
  --action lambda:InvokeFunctionUrl --principal "*" --function-url-auth-type NONE
```

It returns a URL ending in `.lambda-url.<region>.on.aws`. The function handles
CORS itself, so it can be called straight from the site.

## 4. Point the site at it

In `build/shell.py`, find `window.WH_API` and set it to the URL **without** the
trailing slash and **without** `/enquiry` — the site appends the path:

```js
window.WH_API = "https://abc123.lambda-url.ap-south-1.on.aws";
```

Rebuild (`python3 build/make.py`) and redeploy. The form now posts. If the post
fails for any reason, the visitor still gets the mail handoff — that path stays.

## What the function does

- Rejects anything that is not a POST, answers CORS preflight.
- Requires name, email and detail; checks the email is shaped like one.
- Silently accepts and discards submissions that fill the honeypot field, so
  bots do not learn to retry.
- Strips carriage returns from anything placed in a header, which is how mail
  header injection works.
- Rate-limits to three per minute per IP per warm instance.
- Sets Reply-To to the enquirer, so replying from your inbox reaches them.
- Sends an acknowledgement, and does not fail the request if that part fails.

## The honeypot

Already wired. The form carries an offscreen `website` field that no visitor
sees and no visitor fills; the function accepts and discards anything that
arrives with it set, answering 200 so a bot does not learn to retry with a
different shape.
