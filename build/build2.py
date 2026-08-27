# -*- coding: utf-8 -*-
"""Brand guide, privacy notice and 404."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from shell import page, cta, MAIL
from build import write   # reuses the writer (and rebuilds the main pages)

MONO_SVG = """<img src="/assets/brand/badge-reverse.svg" alt="Windsor Harlow mark" style="width:86px">%.0s"""

SWATCHES = [
    ("Blue", "#0079CA", "Brand blue. Primary: buttons, links, active states, eyebrows.", "R0 G121 B202"),
    ("Teal", "#1FA6B8", "Data and technical. Capability labels, stack keys, mono metadata.", "R31 G166 B184"),
    ("Green", "#2ED89C", "Brand green. Emphasis only: one accented word, stage numbers, lead markers. Deepens to #0A7A55 on paper.", "R46 G216 B156"),
    ("Ink", "#04212C", "Dark surfaces, headlines, body text.", "R12 G11 B31"),
    ("Paper", "#F1F5F6", "Page background. Slate #4C6169 for secondary text.", "R243 G243 B249"),
]

TYPE_ROWS = [
    ("Display XL", "Newsreader", "200", "clamp(2.6rem → 5.05rem)", "Page headlines. One per screen."),
    ("Display L", "Newsreader", "300", "clamp(1.95rem → 3.05rem)", "Section headings."),
    ("Display M", "Newsreader", "300", "1.3 → 1.66rem", "Card and panel titles."),
    ("Body", "Archivo", "400", "16.5px / 1.62", "All running text."),
    ("Lede", "Archivo", "400", "1.05 → 1.24rem / 1.58", "Opening paragraphs, in Slate."),
    ("Label", "IBM Plex Mono", "400", "10–11px / .14em tracking", "Eyebrows, metadata, data. Uppercase."),
]

BRAND = f"""
<section class="phero wrap">
  <div class="phero-grid">
    <div>
      <p class="crumb">Brand</p>
      <h1>Windsor Harlow <em>identity system</em>.</h1>
      <p class="lede">A two-colour identity stretched into a three-role system. The logo gives us green and blue; the teal between them is the connective tissue. Blue carries structure, teal marks anything technical, green is rationed to one point of emphasis per view.</p>
      <div class="dl-row">
        <a class="btn" href="/assets/brand/logo-primary.svg" download>Primary logo (SVG)</a>
        <a class="btn btn-ghost" href="/assets/brand/logo-reverse.svg" download>Reverse logo</a>
        <a class="btn btn-ghost" href="/assets/brand/monogram.svg" download>Monogram</a>
      </div>
    </div>
    <dl class="phero-facts">
      <div><dt>Display type</dt><dd>Newsreader &mdash; 200 / 300</dd></div>
      <div><dt>Body type</dt><dd>Archivo &mdash; 400 / 500</dd></div>
      <div><dt>Utility type</dt><dd>IBM Plex Mono &mdash; 400</dd></div>
      <div><dt>Core colours</dt><dd>Violet, Cyan, Amber on Ink / Paper</dd></div>
    </dl>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="sec-head">
      <div><p class="eyebrow">The mark</p><h2>Two forms, interlocked.</h2></div>
      <p class="sec-count">Neither shape closes on its own</p>
    </div>
    <p class="lede" style="margin-bottom:30px">The mark is two hooked forms turned against each other &mdash; green reaching down and left, blue reaching up and right &mdash; each closing the gap the other leaves open. It holds at 16px and carries both brand colours without the wordmark beside it.</p>
    <div class="logoboard">
      <div><div class="lb"><img src="/assets/brand/monogram.svg" alt="Windsor Harlow monogram" style="width:86px"></div><p class="lb-cap">Monogram &mdash; violet-to-cyan gradient</p></div>
      <div><div class="lb on-ink">{MONO_SVG % '#EAF2F4'}</div><p class="lb-cap">Reverse &mdash; paper on ink</p></div>
      <div><div class="lb on-claret">{MONO_SVG % '#04212C'}</div><p class="lb-cap">Single colour &mdash; ink on violet</p></div>
    </div>
    <div class="logoboard" style="margin-top:1px">
      <div style="grid-column:1/-1"><div class="lb" style="min-height:150px"><img src="/assets/brand/logo-primary.svg" alt="Windsor Harlow primary lockup" style="max-width:430px;width:100%"></div>
      <p class="lb-cap">Primary horizontal lockup &mdash; minimum width 180px. Clear space on all sides equals the monogram's cap height.</p></div>
    </div>
  </div>
</section>

<section class="band lift">
  <div class="wrap">
    <div class="sec-head">
      <div><p class="eyebrow">Colour</p><h2>Three brand colours. Two surfaces.</h2></div>
      <p class="sec-count">Amber never exceeds 5% of a layout</p>
    </div>
    <div class="swatches">
""" + "\n".join(f"""      <div class="sw"><div class="sw-chip" style="background:{hexv}"></div>
        <div class="sw-info"><b>{name}</b><span>{hexv}</span><br><em>{rgb}</em><br><em>{use}</em></div></div>"""
                for name, hexv, use, rgb in SWATCHES) + """
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="sec-head">
      <div><p class="eyebrow">Typography</p><h2>Three faces, three jobs.</h2></div>
      <p class="sec-count">Newsreader &middot; Archivo &middot; IBM Plex Mono</p>
    </div>
    <div class="specimen">
      <p class="spec-label">Display &mdash; Newsreader 200</p>
      <p class="spec-xl">Systems that keep running</p>
    </div>
    <div class="specimen">
      <p class="spec-label">Display &mdash; Newsreader 300 italic accent</p>
      <p class="spec-lg">Senior engineers, <em style="font-style:italic;color:var(--claret)">documented handoff</em></p>
    </div>
    <div class="specimen">
      <p class="spec-label">Body &mdash; Archivo 400</p>
      <p class="spec-body">An LLM feature is not a model problem. It is a retrieval problem, an evaluation problem, and a cost problem wearing a model's clothes. We start at the end: an evaluation set built from the questions your users actually ask.</p>
    </div>
    <div class="specimen">
      <p class="spec-label">Utility &mdash; IBM Plex Mono 400</p>
      <p class="spec-mono">STAGE 03 &nbsp;&middot;&nbsp; TERRAFORM &nbsp;&middot;&nbsp; LANGGRAPH &nbsp;&middot;&nbsp; APEX &nbsp;&middot;&nbsp; 6&ndash;10 WEEKS</p>
    </div>
    <div style="margin-top:44px;overflow-x:auto">
      <table class="scale">
        <thead><tr><th>Role</th><th>Face</th><th>Weight</th><th>Size</th><th>Used for</th></tr></thead>
        <tbody>
""" + "\n".join(f"          <tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td><td>{r[4]}</td></tr>"
                for r in TYPE_ROWS) + """
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="dark band">
  <div class="wrap">
    <div class="sec-head">
      <div><p class="eyebrow">Voice</p><h2>How Windsor Harlow sounds.</h2></div>
      <p class="sec-count" style="color:#7194A0">Specific, plain, willing to say no</p>
    </div>
    <div class="dos">
      <div class="do-col do-yes">
        <h3>Do</h3>
        <ul>
          <li>Name the failure mode before the capability. "Most AI pilots die in month two" earns the sentence that follows.</li>
          <li>Use numbers you can defend, and no others. No invented client counts, no fabricated satisfaction scores.</li>
          <li>Say what you will not do. Declining work is the most credible thing a consultancy can write.</li>
          <li>Write for the engineer who will inherit the system, not the executive who signs the invoice.</li>
          <li>Keep sentences short enough to read on a phone between meetings.</li>
        </ul>
      </div>
      <div class="do-col do-no">
        <h3>Do not</h3>
        <ul>
          <li>Use "cutting-edge", "world-class", "seamless", "end-to-end", "synergy", "leverage" as a verb, or "digital transformation".</li>
          <li>Claim clients, logos, awards or team size that do not exist. It is the fastest way to lose an enterprise buyer who checks.</li>
          <li>Stack three adjectives where one specific noun works.</li>
          <li>Use green for large fills, or more than one emphasis per headline. It is a highlighter, not a background.</li>
          <li>Introduce a fourth accent colour, or use the blue&ndash;green gradient on type smaller than 24px.</li>
          <li>Set body copy in Newsreader, or headlines in Archivo.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="band lift">
  <div class="wrap">
    <div class="split">
      <div><p class="eyebrow">Application</p><h2>Rules that keep it consistent.</h2></div>
      <div class="prose">
        <h3>Layout</h3>
        <ul>
          <li>Hairline rules at 1px in <em>--rule</em> separate content. Boxes and shadows do not.</li>
          <li>The blue&ndash;green gradient appears as a 2px edge or an underline sweep &mdash; never as a page background or a large fill.</li>
          <li>Zero border radius everywhere. The system is squared by design.</li>
          <li>Section rhythm comes from one variable, <em>--band</em>. Do not hand-tune padding per section.</li>
          <li>Grids are asymmetric &mdash; a narrower heading column against a wider content column. Never centre long text.</li>
        </ul>
        <h3>Motion</h3>
        <ul>
          <li>The page-load sequence is a staggered rise: eyebrow, headline lines masked upward, lede, buttons. Total under 900ms, one time only.</li>
          <li>One reveal on scroll, 700ms, 18px rise, easing <em>cubic-bezier(.2,.7,.2,1)</em>. Nothing bounces.</li>
          <li>Ambient motion &mdash; the aurora field on dark bands and the pipeline flow in the hero &mdash; runs slow enough to read as atmosphere, 26 seconds and up per cycle. If it draws the eye, it is too fast.</li>
          <li>Gradient edges wipe in on hover from a single origin. Hover states shift position or draw a rule. They do not glow or scale.</li>
          <li><em>prefers-reduced-motion</em> disables all of it. This is not optional.</li>
        </ul>
        <h3>Photography and imagery</h3>
        <ul>
          <li>No stock photography of handshakes, glass towers or diverse teams pointing at monitors.</li>
          <li>Where imagery is needed, use architecture diagrams, terminal output, dashboards &mdash; artefacts of the actual work.</li>
          <li>Duotone in Windsor Ink and Paper if photography becomes unavoidable.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="split">
      <div><p class="eyebrow">Files</p><h2>Assets and production notes.</h2></div>
      <div class="prose">
        <p>The lockup SVGs set the wordmark as live text in Newsreader with a Georgia fallback. That is correct for the website, where the webfont is loaded. <strong>Before any print, signage or third-party use, convert the text to outlines</strong> so the letterforms cannot substitute.</p>
        <p>Favicon is a filled ink square with a claret cap rule and the reverse monogram &mdash; legible at 16px, which the full lockup is not.</p>
        <div class="dl-row">
          <a class="btn" href="/assets/brand/logo-primary.svg" download>logo-primary.svg</a>
          <a class="btn btn-ghost" href="/assets/brand/logo-reverse.svg" download>logo-reverse.svg</a>
          <a class="btn btn-ghost" href="/assets/brand/monogram.svg" download>monogram.svg</a>
          <a class="btn btn-ghost" href="/assets/brand/favicon.svg" download>favicon.svg</a>
        </div>
      </div>
    </div>
  </div>
</section>
"""

write("brand.html", page("/brand.html", "Brand guidelines — Windsor Harlow",
      "The Windsor Harlow identity system: logo, colour, typography, voice and application rules.", BRAND))


# ============================================================ PRIVACY
PRIV = f"""
<section class="phero wrap">
  <div class="phero-grid">
    <div>
      <p class="crumb">Legal</p>
      <h1>Privacy &amp; <em>data handling</em>.</h1>
      <p class="lede">How Windsor Harlow handles personal data on this website and inside client engagements &mdash; under India's Digital Personal Data Protection Act, 2023 and, where EU or UK personal data is involved, the GDPR and UK GDPR.</p>
    </div>
    <dl class="phero-facts">
      <div><dt>Controller</dt><dd>Windsor Harlow, India</dd></div>
      <div><dt>Contact</dt><dd><a href="mailto:{MAIL}" style="border-bottom:1px solid var(--rule)">{MAIL}</a></dd></div>
      <div><dt>Last updated</dt><dd>On publication</dd></div>
    </dl>
  </div>
</section>

<section class="band">
  <div class="wrap doc">
    <p class="mark-note">Before publishing: insert your registered entity name, CIN, registered office address, and the named grievance officer required under section 13 of the DPDP Act. Have a lawyer in your jurisdiction review this page &mdash; it is a well-structured starting point, not legal advice.</p>

    <h2>1. Who we are</h2>
    <p>Windsor Harlow is a technology consultancy registered in India, delivering services to clients in the United States and the European Union. For website enquiries we act as the data fiduciary (controller). Inside client engagements we normally act as a data processor on our client's instructions, governed by the data processing terms in the engagement agreement.</p>

    <h2>2. What we collect on this website</h2>
    <ul>
      <li><strong>Enquiry form data</strong> &mdash; name, work email, company, selected practice, engagement model, timeline and the description you write.</li>
      <li><strong>Server logs</strong> &mdash; IP address, user agent, requested URL and timestamp, retained for security and abuse prevention.</li>
      <li><strong>No advertising or cross-site tracking cookies.</strong> We do not run advertising pixels or sell data to anyone.</li>
    </ul>

    <h2>3. Why we process it</h2>
    <ul>
      <li>To reply to your enquiry and scope potential work &mdash; on the basis of your consent, and our legitimate interest in responding to business contact.</li>
      <li>To keep the site secure and available &mdash; legitimate interest.</li>
      <li>To meet accounting, tax and contractual record-keeping obligations &mdash; legal obligation.</li>
    </ul>

    <h2>4. How long we keep it</h2>
    <p>Enquiries that do not become engagements are deleted within 24 months. Engagement records are retained for the period required by Indian tax and contract law, and by the terms of the relevant agreement. Server logs are retained for 90 days.</p>

    <h2>5. International transfers</h2>
    <p>We are based in India and process data there. Where we process personal data on behalf of an EU or UK client, transfers are covered by Standard Contractual Clauses (and the UK International Data Transfer Addendum where applicable), together with the technical and organisational measures set out in the engagement agreement.</p>

    <h2>6. Client data inside engagements</h2>
    <p>Where an engagement requires access to systems containing personal data, we work to the following defaults, tightened where a client's own policy is stricter:</p>
    <ul>
      <li>Least-privilege, time-boxed access, granted through the client's own identity provider wherever possible.</li>
      <li>No production personal data copied to engineer workstations. Anonymised or synthetic data for development and testing.</li>
      <li>Secrets held in a managed secret store &mdash; never in code, tickets or chat.</li>
      <li>Access revoked at engagement close, with confirmation provided in writing.</li>
      <li>NDA signed before scoping, on request.</li>
    </ul>

    <h2>7. Your rights</h2>
    <p>Under the DPDP Act you may request access to, correction of, or erasure of your personal data, nominate another person to exercise your rights, and raise a grievance with us. Under the GDPR and UK GDPR, where applicable, you additionally have rights to restriction, portability and objection, and the right to lodge a complaint with your supervisory authority.</p>
    <p>To exercise any of these, email <a href="mailto:{MAIL}" style="border-bottom:1px solid var(--rule)">{MAIL}</a>. We respond within 30 days.</p>

    <h2>8. Subprocessors</h2>
    <p>This site is served from a commercial hosting provider, and enquiry emails are delivered through a transactional email provider. A current list of subprocessors, with their locations, is available on request &mdash; and is provided as a matter of course in any engagement involving personal data.</p>

    <h2>9. Changes</h2>
    <p>Material changes to this notice are published on this page with a revised date. Where a change affects processing you have consented to, we will seek fresh consent.</p>
  </div>
</section>
"""
write("privacy.html", page("/privacy.html", "Privacy & data handling — Windsor Harlow",
      "How Windsor Harlow handles personal data on this website and inside client engagements, under India's DPDP Act 2023 and the GDPR.", PRIV))


# ============================================================ 404
write("404.html", page("/404.html", "Page not found — Windsor Harlow",
      "That page does not exist. Here is where to go instead.", """
<section class="phero wrap">
  <div class="phero-grid">
    <div>
      <p class="crumb">404</p>
      <h1>That page <em>does not exist</em>.</h1>
      <p class="lede">The link is wrong, or the page moved. Nothing has broken on your side.</p>
      <div class="hero-cta">
        <a class="btn" href="/">Back to the home page <span class="arrow">&#8594;</span></a>
        <a class="btn btn-ghost" href="/practices/">Browse the practices</a>
      </div>
    </div>
    <dl class="phero-facts">
      <div><dt>Looking for</dt><dd><a href="/practices/ai-ml.html" style="border-bottom:1px solid var(--rule)">AI, ML &amp; MLOps</a></dd></div>
      <div><dt>Or</dt><dd><a href="/practices/salesforce.html" style="border-bottom:1px solid var(--rule)">Salesforce</a></dd></div>
      <div><dt>Or just</dt><dd><a href="/contact.html" style="border-bottom:1px solid var(--rule)">Contact us</a></dd></div>
    </dl>
  </div>
</section>
""", extra_head='<meta name="robots" content="noindex, nofollow">'))
print("extras done")
