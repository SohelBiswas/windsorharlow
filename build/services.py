# -*- coding: utf-8 -*-
"""The dedicated services page."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from shell import page, cta
from practices import P, BY_ID
from build import write   # rebuilds home + practice pages, then we add this

# Plain-language layer: one sentence a non-technical buyer understands, plus the
# situations they would recognise in their own words. The stack stays underneath
# in mono for the engineer they hand it to.
PLAIN = {
  "ai": ("AI features that still work once real customers use them.",
    ["A chatbot or assistant that answers from your own documents",
     "Search that understands meaning, not just keywords",
     "Getting an AI prototype ready for real traffic",
     "Cutting what your AI costs to run"]),
  "salesforce": ("Salesforce work the next admin can actually maintain.",
    ["Custom Apex and Lightning components",
     "Untangling years of half-finished automation",
     "Connecting Salesforce to the rest of your systems",
     "Getting a failing org back under control"]),
  "cloud": ("Infrastructure your own team can run after we leave.",
    ["Moving off on-prem or a legacy host",
     "Cloud bills that keep climbing",
     "Deploys that are slow, manual or frightening",
     "Systems that fall over under load"]),
  "web": ("Backends and web apps that hold up as you grow.",
    ["A new product built from scratch",
     "An application that has outgrown its original design",
     "Splitting a monolith without stopping the business",
     "APIs other teams can build on"]),
  "mobile": ("iOS and Android apps, on the right platform for the job.",
    ["A new mobile app for both stores",
     "Rebuilding an app that is slow or crashing",
     "Getting through App Store and Play review",
     "Adding offline or real-time features"]),
  "commerce": ("Storefronts and interfaces designed and built by one team.",
    ["A Shopify store that has outgrown its theme",
     "Migrating a store without losing search rankings",
     "Slow pages costing you sales",
     "Design that arrives build-ready, not as a picture"]),
}

PROBLEMS = [
  ("We need to build something new", "Backend &amp; Web &middot; Mobile &middot; Commerce", "#catalogue"),
  ("What we have is slow or breaking", "Cloud &amp; DevOps &middot; Backend", "#catalogue"),
  ("We want AI in the product", "AI, ML &amp; MLOps", "#catalogue"),
  ("We are moving to the cloud", "Cloud, DevOps &amp; Infrastructure", "#catalogue"),
  ("Our Salesforce org is a mess", "Salesforce Development", "#catalogue"),
  ("We need senior engineers, now", "Embedded team &middot; Retainer", "#matrix"),
]
PROBS = "\n".join(
  f'      <a class="prob" href="{h}"><span>0{i+1}</span><b>{q}</b><i>{w}</i></a>'
  for i,(q,w,h) in enumerate(PROBLEMS))
PROB_SECTION = f"""<section class="band-tight" id="start">
  <div class="wrap">
    <p class="eyebrow">Start from the problem</p>
    <div class="probs">
{PROBS}
    </div>
  </div>
</section>

"""


SERVICE_LINES = {
    "ai": ["Retrieval-augmented generation (RAG) platforms",
           "Agentic workflows and tool-calling systems",
           "Model serving, inference cost optimisation",
           "Evaluation harnesses and drift monitoring",
           "Fine-tuning: LoRA, QLoRA, instruction tuning",
           "MLOps pipelines, model registry, CI/CD for ML"],
    "salesforce": ["Apex development and Lightning Web Components",
                   "Automation consolidation: triggers, Flow, Process Builder",
                   "REST and Platform Event integrations",
                   "Sales Cloud, Experience Cloud, B2B Commerce Cloud",
                   "SOQL and large-data-volume optimisation",
                   "Metadata version control and CI deployment"],
    "cloud": ["AWS, Google Cloud and Azure architecture",
              "Cloud migration: lift-and-shift to full re-architecture",
              "Kubernetes, service mesh, GitOps",
              "Terraform and infrastructure as code",
              "Multi-region high availability and disaster recovery",
              "FinOps: cost audits, rightsizing, chargeback"],
    "web": ["Full-stack product builds, greenfield to launch",
            "Microservices and event-driven architecture",
            "GraphQL, gRPC and real-time APIs",
            "Event sourcing, CQRS, saga orchestration",
            "PostgreSQL performance, partitioning, multi-tenancy",
            "Load testing and observability-driven tuning"],
    "mobile": ["React Native and Flutter delivery",
               "Native iOS (Swift) and Android (Kotlin)",
               "Kotlin Multiplatform shared-logic builds",
               "Offline-first sync and conflict resolution",
               "Mobile CI, signing and store release",
               "Crash and performance monitoring"],
    "commerce": ["Custom Shopify storefronts and themes",
                 "Headless commerce front ends",
                 "Platform migration with data reconciliation",
                 "UI/UX design delivered as coded components",
                 "Core Web Vitals and performance budgets",
                 "Checkout and funnel instrumentation"],
}

MATRIX = [
    ("Fixed-scope project", "A defined deliverable", "Fixed price, fixed date",
     "yes", "yes", "MVPs, migrations, platform builds"),
    ("Embedded team", "Sustained capacity", "Rolling monthly",
     "yes", "no", "Teams shipping continuously"),
    ("Retainer &amp; support", "Keeping it alive", "Monthly, defined response times",
     "no", "yes", "Live platforms after launch"),
    ("Technical advisory", "Deciding what to build", "Fixed price, 2&ndash;4 weeks",
     "yes", "no", "Audits, reviews, migration planning"),
]

from content import PRACTICE_META, PRACTICE_ORDER

# One order, one lead set, shared with the home page.
ORDERED = [BY_ID[i] for i in PRACTICE_ORDER if i in BY_ID]
def is_lead(p):
    return bool(PRACTICE_META.get(p["id"], {}).get("lead"))

tiles = []
for i, p in enumerate(ORDERED):
    lines = "\n".join(f"          <li>{l}</li>" for l in SERVICE_LINES[p["id"]])
    badge = '<span class="svc-badge">Lead practice</span>' if is_lead(p) else \
            f'<span>{len(p["stack"])} capability groups</span>'
    tiles.append(f"""      <article class="svc{' lead' if is_lead(p) else ''}">
        <div class="svc-head"><i>0{i+1}</i><h3>{p['label']}</h3></div>
        <p class="svc-lead">{PLAIN.get(p['id'], (p['lede'], []))[0]}</p>
        <p class="svc-forlabel">You would come to us for</p>
        <ul class="svc-for">{''.join(f'<li>{o}</li>' for o in PLAIN.get(p['id'], ('', []))[1])}</ul>
        <p class="svc-stack">{' &middot; '.join(s[0] for s in p['stack'][:6])}</p>
        <div class="svc-foot">{badge}
          <a href="/practices/{p['slug']}.html">Full practice page &#8594;</a></div>
      </article>""")



rows = "\n".join(f"""        <tr><td>{m[0]}</td><td>{m[1]}</td><td>{m[2]}</td>
          <td class="{'yes' if m[3]=='yes' else 'no'}">{'Fixed price' if m[3]=='yes' else 'Time-based'}</td>
          <td class="{'yes' if m[4]=='yes' else 'no'}">{'Included' if m[4]=='yes' else 'Optional'}</td>
          <td>{m[5]}</td></tr>""" for m in MATRIX)

BODY = f"""
<section class="phero wrap">
  <div class="phero-grid">
    <div>
      <p class="crumb seq seq-1">Services</p>
      <h1>
        <span class="h-line"><span>Everything Windsor Harlow</span></span>
        <span class="h-line"><span>actually <em>does</em>.</span></span>
      </h1>
      <p class="lede seq seq-4">Six practices, about 170 named technologies. We lead with backend, AI/ML and mobile; the rest run to the same standard.</p>
      <div class="hero-cta seq seq-5">
        <a class="btn" href="/contact.html">Scope an engagement <span class="arrow">&#8594;</span></a>
        <a class="btn btn-ghost" href="#matrix">Compare engagement models</a>
      </div>
    </div>
    <dl class="phero-facts seq seq-3">
      <div><dt>Lead practices</dt><dd>Backend &amp; Web &middot; AI, ML &amp; MLOps &middot; Mobile</dd></div>
      <div><dt>Also delivering</dt><dd>Cloud &middot; Salesforce &middot; Commerce</dd></div>
      <div><dt>Regions</dt><dd>Global &mdash; Americas, EMEA, APAC</dd></div>
      <div><dt>Minimum engagement</dt><dd>Two-week advisory</dd></div>
    </dl>
  </div>
</section>

{PROB_SECTION}<section class="band" id="catalogue">
  <div class="wrap">
    <div class="sec-head">
      <div><p class="eyebrow">Service catalogue</p><h2>Six practices, thirty-six service lines.</h2></div>
    </div>
    <div class="svc-grid">
{chr(10).join(tiles)}
    </div>
  </div>
</section>

<section class="dark band" id="matrix">
  <div class="wrap">
    <div class="sec-head">
      <div><p class="eyebrow">Engagement models</p><h2>How the commercials work.</h2></div>
      <p class="sec-count" style="color:var(--on-dark-3)">Any service, any model</p>
    </div>
    <div style="overflow-x:auto">
      <table class="matrix">
        <thead><tr><th>Model</th><th>What it is for</th><th>Commercials</th><th>Pricing</th><th>Handoff docs</th><th>Typical fit</th></tr></thead>
        <tbody>
{rows}
        </tbody>
      </table>
    </div>
    <p class="lede" style="margin-top:34px;color:var(--on-dark-2)">Fixable scope gets a fixed price. We tell you which one you are in before you sign.</p>
  </div>
</section>

<section class="band lift" id="index">
  <div class="wrap">
    <div class="sec-head">
      <div><p class="eyebrow">Capability index</p><h2>Search every technology we work in.</h2></div>
    </div>
    <div class="idx-tools">
      <div class="idx-search">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" style="color:var(--slate)" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M16.5 16.5 21 21"/></svg>
        <label for="idxq" style="position:absolute;left:-9999px">Search capabilities</label>
        <input id="idxq" type="search" placeholder="langgraph, apex, terraform, kafka&hellip;" autocomplete="off">
      </div>
      <div class="chips" id="idxChips"></div>
    </div>
    <p class="idx-meta" id="idxMeta"></p>
    <div class="idx-grid" id="idxGrid"></div>
    <div class="idx-empty" id="idxEmpty" hidden>No match in the index. That does not mean no. <a href="/contact.html">Tell us what you are running</a> and we will answer honestly about fit.</div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="sec-head">
      <div><p class="eyebrow">How we deliver</p><h2>The same four stages, whichever service you buy.</h2></div>
    </div>
    <div class="stage-track" id="stageTrack"><i></i></div>
    <div class="stage-dots" id="stageDots" aria-hidden="true"></div>
    <div class="steps" id="steps">
      <div class="step"><span class="step-n">Stage 01</span><h3>Scope</h3><p>A written scope with the assumptions stated.</p></div>
      <div class="step"><span class="step-n">Stage 02</span><h3>Architect</h3><p>Trade-offs documented: cost, operability, failure modes.</p></div>
      <div class="step"><span class="step-n">Stage 03</span><h3>Build</h3><p>Two-week increments, deployed and demoed. Tests and CI from the first commit.</p></div>
      <div class="step"><span class="step-n">Stage 04</span><h3>Hand off</h3><p>Runbooks, decision records, a walkthrough. Retainer optional, never assumed.</p></div>
    </div>
  </div>
</section>
""" + cta("Not sure which service your problem belongs to?",
          "Describe the situation. We will tell you what it needs &mdash; including when the answer is another firm.")

write("services.html", page("/services.html", "Services — Windsor Harlow",
      "The full Windsor Harlow service catalogue: AI/ML and MLOps, Salesforce, cloud and DevOps, web and distributed systems, mobile, commerce and product design. Six practices, thirty-six service lines.",
      BODY))

# the old practices hub is replaced by /services.html
old = os.path.join(os.path.dirname(__file__), "..", "public", "practices", "index.html")
if os.path.exists(old):
    os.remove(old)
    print("  removed practices/index.html (superseded by services.html)")
