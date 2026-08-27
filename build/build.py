# -*- coding: utf-8 -*-
"""Renders the Windsor Harlow static site into ../public."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from shell import page, cta, MAIL, SITE, live_section, orbit_section, TERMINAL, PIPELINE, INTRO, OVERTURE
from practices import P, BY_ID

OUT = os.path.join(os.path.dirname(__file__), "..", "public")


def write(rel, html):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("  wrote", rel, f"({len(html)//1024} KB)")


# ============================================================ HOME
JSONLD = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"ProfessionalService","name":"Windsor Harlow",
"description":"Technology consultancy delivering AI/ML systems, Salesforce platform engineering, cloud infrastructure, distributed web and mobile applications.",
"url":"%s","email":"%s","areaServed":"Worldwide",
"address":{"@type":"PostalAddress","addressCountry":"IN"},
"knowsAbout":["Artificial Intelligence","Salesforce","Cloud Architecture","Kubernetes","Distributed Systems","Mobile Development"]}
</script>
""" % (SITE, MAIL)

HOME = """
__OVERTURE__
<section class="hero wrap">
  <div class="hero-grid">
    <div>
      <p class="eyebrow seq seq-1">Technology consultancy &mdash; engineered in India, delivering globally</p>
      <h1>
        <span class="h-line"><span>Backends that hold under load.</span></span>
        <span class="h-line"><span>AI that survives production. Apps that <em>survive the handover</em>.</span></span>
      </h1>
      <div class="hero-cta seq seq-5">
        <a class="btn" href="/contact.html">Scope an engagement <span class="arrow">&#8594;</span></a>
        <a class="btn btn-ghost" href="/services.html">See all services</a>
      </div>
    </div>

    <div class="hero-visual seq seq-3" aria-hidden="true">
      <svg class="graph" viewBox="0 0 440 330" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="gBrand" x1="0" y1="1" x2="1" y2="0">
            <stop offset="0" stop-color="#0079CA"/><stop offset=".55" stop-color="#1B93E4"/>
            <stop offset="1" stop-color="#1FA6B8"/>
          </linearGradient>
          <linearGradient id="gScan" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0" stop-color="#1FA6B8" stop-opacity="0"/>
            <stop offset=".5" stop-color="#1FA6B8" stop-opacity=".55"/>
            <stop offset="1" stop-color="#1FA6B8" stop-opacity="0"/>
          </linearGradient>
        </defs>

        <g class="g-scan"><rect x="218" y="10" width="1.2" height="310" fill="url(#gScan)"/></g>

        <text class="g-title" x="0" y="14">REQUEST LIFECYCLE</text>
        <line class="g-tier" x1="0" y1="24" x2="440" y2="24"/>

        <g class="g-edge-set">
          <path class="g-edge" d="M65 62 H150"/>
          <path class="g-edge" d="M180 62 H265"/>
          <path class="g-edge" d="M295 62 H375"/>
          <path class="g-edge" d="M390 77 V120 Q390 155 355 155 H295"/>
          <path class="g-edge" d="M265 155 H180"/>
          <path class="g-edge" d="M165 170 V225"/>
          <path class="g-edge" d="M150 155 H65"/>
          <path class="g-edge" d="M50 170 V225"/>
          <path class="g-edge" d="M65 240 H150"/>
          <path class="g-edge" d="M180 240 H265"/>
          <path class="g-edge" d="M280 225 V180" stroke-dasharray="3 4"/>
        </g>
        <g>
          <path class="g-flow" d="M65 62 H150"/>
          <path class="g-flow d2" d="M180 62 H265"/>
          <path class="g-flow d3" d="M295 62 H375"/>
          <path class="g-flow d4" d="M390 77 V120 Q390 155 355 155 H295"/>
          <path class="g-flow d5" d="M265 155 H180"/>
          <path class="g-flow d6" d="M150 155 H65"/>
          <path class="g-flow d3" d="M65 240 H150"/>
          <path class="g-flow d5" d="M180 240 H265"/>
        </g>

        <circle class="g-ring" cx="165" cy="62" r="15"/>
        <circle class="g-ring r2" cx="280" cy="155" r="15"/>
        <circle class="g-ring r3" cx="165" cy="240" r="15"/>

        <circle class="g-node g-node-lead" cx="50" cy="62" r="15"/>
        <circle class="g-node" cx="165" cy="62" r="15"/>
        <circle class="g-node g-node-lead" cx="280" cy="62" r="15"/>
        <circle class="g-node" cx="390" cy="62" r="15"/>
        <circle class="g-node" cx="280" cy="155" r="15"/>
        <circle class="g-node" cx="165" cy="155" r="15"/>
        <circle class="g-node" cx="50" cy="155" r="15"/>
        <circle class="g-node" cx="50" cy="240" r="15"/>
        <circle class="g-node g-node-lead" cx="165" cy="240" r="15"/>
        <circle class="g-node" cx="280" cy="240" r="15"/>

        <g text-anchor="middle">
          <text class="g-label" x="50" y="95">Client</text>
          <text class="g-label" x="165" y="95">Gateway</text>
          <text class="g-label g-label-key" x="280" y="95">Service</text>
          <text class="g-label" x="390" y="95">Auth</text>
          <text class="g-label g-label-key" x="280" y="188">Queue</text>
          <text class="g-label" x="165" y="188">Worker</text>
          <text class="g-label g-label-key" x="50" y="188">Database</text>
          <text class="g-label" x="50" y="273">Cache</text>
          <text class="g-label" x="165" y="273">Web app</text>
          <text class="g-label" x="280" y="273">Mobile</text>
        </g>
      </svg>
      <p class="hero-visual-cap">A request, end to end. We build every tier on this diagram.</p>
    </div>
  </div>

  <div class="ticker seq seq-6" aria-hidden="true">
    <span class="ticker-live"></span><span class="ticker-label">Working stack</span>
    <div class="ticker-view"><div class="ticker-track" id="tick"></div></div>
  </div>

  <div class="figures">
    <div class="figure"><span class="figure-n">Practices</span><b data-to="6">0</b><p>Three leading, three at the same delivery standard.</p></div>
    <div class="figure"><span class="figure-n">Capability index</span><b data-to="auto-index" data-suffix="">0</b><p>Named technologies, all searchable.</p></div>
    <div class="figure"><span class="figure-n">Engagement models</span><b data-to="4">0</b><p>Fixed scope, embedded, retainer, advisory.</p></div>
    <div class="figure"><span class="figure-n">Time zones</span><b data-to="3" data-suffix="">0</b><p>Americas, EMEA and APAC, covered every working day.</p></div>
  </div>
</section>

__INTRO__
<section class="dark band">
  <div class="wrap">
    <div class="statement">
      <h2>Most firms sell you a proposal. We are built for the <em>eighteen months after it</em>.</h2>
      <div>
        <p class="lede">The people who understood the architecture were never the people who wrote the code.</p>
        <p class="lede">Same names, same numbers, first call to final commit.</p>
      </div>
    </div>
    <div class="pillars">
      <div class="pillar"><span class="pillar-n">Staffing</span><h3>Senior engineers only</h3><p>Every engagement is scoped and delivered by engineers who have shipped this class of system before.</p></div>
      <div class="pillar"><span class="pillar-n">Access</span><h3>No relay layer</h3><p>Direct access to the people building your system &mdash; in your sprint calls, in your channels, throughout.</p></div>
      <div class="pillar"><span class="pillar-n">Commercials</span><h3>Fixed-price clarity</h3><p>Defined scope gets a fixed price and a fixed timeline. Change is priced openly, before it happens.</p></div>
      <div class="pillar"><span class="pillar-n">Exit</span><h3>Documented handoff</h3><p>We optimise for the day you stop needing us. Runbooks, decision records, operational ownership transferred.</p></div>
    </div>
  </div>
</section>

<section class="band" id="lead">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <p class="eyebrow">Where we lead</p>
        <h2>Three practices carry most of our work.</h2>
      </div>
      <p class="sec-count"><a href="/services.html" style="border-bottom:1px solid var(--rule)">All services &#8594;</a></p>
    </div>
    <div class="spears" id="spears"></div>

    <div class="sec-head" style="margin-top:clamp(48px,6vw,80px)">
      <div><h2 style="font-size:clamp(1.5rem,2.2vw,2rem)">The rest of the firm</h2></div>
    </div>
    <div class="strip" id="strip"></div>
  </div>
</section>

__LIVE__
<section class="band lift" id="delivery-model">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <p class="eyebrow">Where we work from</p>
        <h2>Engineered in India. Built for global delivery.</h2>
      </div>
    </div>
    <div class="globe cont-wrap">
      <div class="cont">
      <svg class="cont-svg" viewBox="0 0 900 268" role="img"
           aria-label="On a typical engagement the engineers rotate off and are replaced; at Windsor Harlow the same engineers run from kickoff to handover">
        <text class="cn-tag" x="3" y="80">TYPICAL</text>
        <g class="cn-typ"><line class="cn-old" x1="118" y1="58" x2="300" y2="58" pathLength="100" style="--i:0;--d:0.0s"/><circle class="cn-odot" cx="118" cy="58" r="4.5" style="--d:0.35s"/><line class="cn-old" x1="322" y1="58" x2="560" y2="58" pathLength="100" style="--i:1;--d:0.1s"/><circle class="cn-odot" cx="322" cy="58" r="4.5" style="--d:0.44999999999999996s"/><line class="cn-old" x1="582" y1="58" x2="830" y2="58" pathLength="100" style="--i:2;--d:0.2s"/><circle class="cn-odot" cx="582" cy="58" r="4.5" style="--d:0.55s"/><line class="cn-old" x1="118" y1="76" x2="450" y2="76" pathLength="100" style="--i:3;--d:0.30000000000000004s"/><circle class="cn-odot" cx="118" cy="76" r="4.5" style="--d:0.65s"/><line class="cn-old" x1="472" y1="76" x2="830" y2="76" pathLength="100" style="--i:4;--d:0.4s"/><circle class="cn-odot" cx="472" cy="76" r="4.5" style="--d:0.75s"/><line class="cn-old" x1="118" y1="94" x2="240" y2="94" pathLength="100" style="--i:5;--d:0.5s"/><circle class="cn-odot" cx="118" cy="94" r="4.5" style="--d:0.85s"/><line class="cn-old" x1="262" y1="94" x2="640" y2="94" pathLength="100" style="--i:6;--d:0.6000000000000001s"/><circle class="cn-odot" cx="262" cy="94" r="4.5" style="--d:0.9500000000000001s"/><line class="cn-old" x1="662" y1="94" x2="830" y2="94" pathLength="100" style="--i:7;--d:0.7000000000000001s"/><circle class="cn-odot" cx="662" cy="94" r="4.5" style="--d:1.05s"/></g>
        <line class="cn-rule" x1="118" y1="131" x2="830" y2="131"/>
        <text class="cn-tag cn-tag-us" x="3" y="190">WINDSOR<tspan x="3" dy="13">HARLOW</tspan></text>
        <g class="cn-mine"><line class="cn-new" x1="118" y1="168" x2="830" y2="168" pathLength="100" style="--i:0;--d:0.9s"/><circle class="cn-ndot" cx="118" cy="168" r="5" style="--d:0.9s"/><circle class="cn-ndot" cx="830" cy="168" r="5" style="--d:1.7s"/><line class="cn-new" x1="118" y1="186" x2="830" y2="186" pathLength="100" style="--i:1;--d:1.08s"/><circle class="cn-ndot" cx="118" cy="186" r="5" style="--d:1.08s"/><circle class="cn-ndot" cx="830" cy="186" r="5" style="--d:1.88s"/><line class="cn-new" x1="118" y1="204" x2="830" y2="204" pathLength="100" style="--i:2;--d:1.26s"/><circle class="cn-ndot" cx="118" cy="204" r="5" style="--d:1.26s"/><circle class="cn-ndot" cx="830" cy="204" r="5" style="--d:2.06s"/></g>
        <text class="cn-end" x="118" y="244" text-anchor="start">KICKOFF</text>
        <text class="cn-end" x="830" y="244" text-anchor="end">HANDOVER</text>
      </svg>
    </div>
      <p class="globe-note">Rotations are your decision, not our resourcing convenience.</p>
    </div>
  </div>
</section>

__ORBIT__

<section class="dark band kin" id="promise">
  <div class="wrap">
    <p class="kin-line">
      <span>We build the part</span>
      <span>your customers</span>
      <span class="kin-slot" aria-hidden="true"><i>touch.</i><i>trust.</i><i>never think about.</i></span>
      <span class="kin-sr">touch, trust, and never think about.</span>
      <span class="kin-rule" aria-hidden="true"></span>
    </p>
  </div>
</section>

<section class="dark band" id="index">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <p class="eyebrow">Capability index</p>
        <h2>Search the stack. If it is listed, we have run it in production.</h2>
      </div>
    </div>
    <div class="idx-tools">
      <div class="idx-search">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#EAF2F4" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M16.5 16.5 21 21"/></svg>
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

<section class="band" id="engagement">
  <div class="wrap">
    <div class="sec-head">
      <div><p class="eyebrow">Engagement models</p><h2>Four ways to work with us.</h2></div>
    </div>
    <div class="eng">

      <div class="eng-card">
        <svg class="eng-fig" viewBox="0 0 200 44" aria-label="A bounded engagement: defined start, defined end">
          <line class="ef-base" x1="8" y1="30" x2="192" y2="30" pathLength="100"/>
          <line class="ef-cap" x1="16" y1="14" x2="16" y2="30" pathLength="100"/>
          <line class="ef-cap ef-cap2" x1="140" y1="14" x2="140" y2="30" pathLength="100"/>
          <rect class="ef-bar" x="16" y="20" width="124" height="6" rx="1"/>
        </svg>
        <span class="eng-tag">Fixed scope</span><h3>Project delivery</h3>
        <p>A fixed price and a real end date.</p>
        <p class="eng-chips"><span>MVPs</span><span>Platform builds</span><span>Migrations</span></p>
      </div>

      <div class="eng-card">
        <svg class="eng-fig" viewBox="0 0 200 44" aria-label="Our engineers interleaved with your team, continuing">
          <line class="ef-base" x1="8" y1="30" x2="192" y2="30" pathLength="100"/>
          <g class="ef-weave">
            <circle class="ef-them" cx="30" cy="30" r="4"/><circle class="ef-us" cx="54" cy="30" r="4"/>
            <circle class="ef-them" cx="78" cy="30" r="4"/><circle class="ef-us" cx="102" cy="30" r="4"/>
            <circle class="ef-them" cx="126" cy="30" r="4"/><circle class="ef-us" cx="150" cy="30" r="4"/>
            <circle class="ef-them" cx="174" cy="30" r="4"/>
          </g>
        </svg>
        <span class="eng-tag">Rolling monthly</span><h3>Embedded team</h3>
        <p>Our engineers in your sprints, on your board.</p>
        <p class="eng-chips"><span>Sustained capacity</span><span>Your standards</span></p>
      </div>

      <div class="eng-card">
        <svg class="eng-fig" viewBox="0 0 200 44" aria-label="A continuous line with periodic on-call spikes">
          <line class="ef-base" x1="8" y1="30" x2="192" y2="30" pathLength="100"/>
          <path class="ef-pulse" d="M8 30 h34 l8 -16 l8 16 h38 l8 -13 l8 13 h38 l8 -16 l8 16 h26" pathLength="100"/>
        </svg>
        <span class="eng-tag">Ongoing</span><h3>Retainer &amp; support</h3>
        <p>Iteration, monitoring and on-call after launch.</p>
        <p class="eng-chips"><span>Live platforms</span><span>No full-time hire</span></p>
      </div>

      <div class="eng-card">
        <svg class="eng-fig" viewBox="0 0 200 44" aria-label="A short engagement at the start, then the work is yours">
          <line class="ef-base" x1="8" y1="30" x2="192" y2="30" pathLength="100"/>
          <rect class="ef-bar ef-bar-short" x="16" y="20" width="46" height="6" rx="1"/>
          <line class="ef-dotted" x1="70" y1="23" x2="176" y2="23" pathLength="100"/>
          <path class="ef-arrow" d="M170 18 l8 5 l-8 5" pathLength="100"/>
        </svg>
        <span class="eng-tag">Short form</span><h3>Technical advisory</h3>
        <p>Decide what to build &mdash; or whether to.</p>
        <p class="eng-chips"><span>Architecture review</span><span>Cost audit</span></p>
      </div>

    </div>
  </div>
</section>

<section class="band lift" id="delivery">
  <div class="wrap">
    <div class="sec-head">
      <div><p class="eyebrow">How we deliver</p><h2>The same four stages, every engagement.</h2></div>
    </div>
    <div class="stage-track" id="stageTrack"><i></i></div>
    <div class="stage-dots" id="stageDots" aria-hidden="true"></div>
    <div class="steps" id="steps">

      <div class="step">
        <svg class="step-fig" viewBox="0 0 56 44" aria-hidden="true">
          <path class="sf-line" d="M14 10 h-6 v24 h6" pathLength="100"/>
          <path class="sf-line" d="M42 10 h6 v24 h-6" pathLength="100"/>
          <circle class="sf-dot" cx="22" cy="22" r="3"/><circle class="sf-dot" cx="30" cy="22" r="3"/>
          <circle class="sf-dot" cx="38" cy="22" r="3"/>
        </svg>
        <span class="step-n">Stage 01</span><h3>Scope</h3>
        <p>A written scope, with the assumptions stated.</p>
      </div>

      <div class="step">
        <svg class="step-fig" viewBox="0 0 56 44" aria-hidden="true">
          <path class="sf-line" d="M14 14 C14 26 42 20 42 32" pathLength="100"/>
          <path class="sf-line sf-d2" d="M42 14 C42 26 14 20 14 32" pathLength="100"/>
          <circle class="sf-node" cx="14" cy="12" r="4"/><circle class="sf-node" cx="42" cy="12" r="4"/>
          <circle class="sf-node sf-lead" cx="14" cy="34" r="4"/><circle class="sf-node" cx="42" cy="34" r="4"/>
        </svg>
        <span class="step-n">Stage 02</span><h3>Architect</h3>
        <p>Trade-offs documented: cost, operability, failure modes.</p>
      </div>

      <div class="step">
        <svg class="step-fig" viewBox="0 0 56 44" aria-hidden="true">
          <rect class="sf-inc" x="8" y="30" width="40" height="6" rx="1"/>
          <rect class="sf-inc sf-i2" x="8" y="20" width="30" height="6" rx="1"/>
          <rect class="sf-inc sf-i3" x="8" y="10" width="20" height="6" rx="1"/>
        </svg>
        <span class="step-n">Stage 03</span><h3>Build</h3>
        <p>Two-week increments, deployed and demoed. Tests and CI from the first commit.</p>
      </div>

      <div class="step">
        <svg class="step-fig" viewBox="0 0 56 44" aria-hidden="true">
          <line class="sf-bound" x1="34" y1="6" x2="34" y2="38" pathLength="100"/>
          <path class="sf-cross" d="M8 22 h34" pathLength="100"/>
          <path class="sf-cross sf-head" d="M38 17 l7 5 l-7 5" pathLength="100"/>
        </svg>
        <span class="step-n">Stage 04</span><h3>Hand off</h3>
        <p>Runbooks, decision records, a walkthrough. Retainer optional, never assumed.</p>
      </div>

    </div>
  </div>
</section>

<section class="band" id="work">
  <div class="wrap">
    <div class="sec-head">
      <div><p class="eyebrow">Work</p><h2>Things we built, written up in full.</h2></div>
      <p class="sec-count" id="workCount"></p>
    </div>
    <p style="margin-bottom:30px"><span class="pill off" data-api><b></b><span>Checking API&hellip;</span></span></p>
    <div class="work-filters" id="workFilters"></div>
    <div class="work-grid" id="workGrid"></div>
    <p style="margin-top:28px"><a class="btn btn-ghost" href="/admin.html">Publish a case study <span class="arrow">&#8594;</span></a></p>
  </div>
</section>
""" + cta(
    "Tell us what you are building &mdash; or what is already broken.",
    "A senior engineer replies within one business day.",
    "Start a conversation")

HOME = HOME.replace("__OVERTURE__", OVERTURE).replace("__INTRO__", INTRO).replace("__LIVE__", live_section(dark=True)).replace("__ORBIT__", orbit_section())

write("index.html", page(
    "/", "Windsor Harlow — AI, Salesforce and cloud engineering consultancy",
    "Windsor Harlow is a technology consultancy leading with AI/ML and Salesforce engineering, plus cloud, distributed systems, mobile and commerce. Senior engineers only, documented handoff. Engineered in India, delivering globally.",
    HOME, extra_head=JSONLD))


# ============================================================ PRACTICE PAGES
def practice_page(p):
    caps = "\n".join(
        f'      <div class="cap"><dt>{k}</dt><dd>{v}</dd></div>' for k, v in p["stack"])
    facts = "\n".join(
        f'      <div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in p["facts"])
    exs = "\n".join(f"""      <article class="ex">
        <p class="ex-tag">{e['tag']}</p><h3>{e['h4']}</h3><p>{e['p']}</p>
        <p class="ex-meta">{e['meta']}</p></article>""" for e in p["examples"])
    dels = "\n".join(f"""      <div class="del"><i>0{i+1}</i><div><h3>{d['h4']}</h3><p>{d['p']}</p></div></div>"""
                     for i, d in enumerate(p["dels"]))
    faqs = "\n".join(f"""      <div class="acc-item">
        <button class="acc-q" aria-expanded="false">{q}<span>+</span></button>
        <div class="acc-a"><p>{a}</p></div></div>""" for q, a in p["faqs"])
    intro = "\n".join(f"        <p class=\"lede\">{t}</p>" for t in p["intro"])
    bullets = "\n".join(f"          <li>{b}</li>" for b in p["bullets"])

    live_block = ""
    if p["id"] in ("web", "ai", "mobile", "cloud", "salesforce"):
        live_block = f"""
<section class="dark band" id="live">
  <div class="wrap">
    <div class="sec-head">
      <div><p class="eyebrow">In the work</p><h2>What {p['short']} code looks like <em>when we write it</em>.</h2></div>
    </div>
    <div class="live">
      <div>
        <div class="live-tabs" id="liveTabs"></div>
        {TERMINAL.replace('id="term"', 'id="term" data-start="' + p['id'] + '"')}
        {PIPELINE}
      </div>
      <div class="live-copy">
        <h3>{p['live_h']}</h3>
        <p>{p['live_p']}</p>
        <p style="margin-top:24px"><a class="btn btn-ghost" href="/contact.html">Scope a {p['short']} engagement <span class="arrow">&#8594;</span></a></p>
      </div>
    </div>
  </div>
</section>
"""

    others = [o for o in P if o["id"] != p["id"]][:3]
    more = "\n".join(f"""      <a href="/practices/{o['slug']}.html"><i>&rarr;</i><h3>{o['label']}</h3>
        <p>{o.get('lede','')[:118]}&hellip;</p><span>&#8594;</span></a>""" for o in others)

    body = f"""
<section class="phero wrap">
  <div class="phero-grid">
    <div>
      <p class="crumb"><a href="/services.html">Services</a> / {p['label']}</p>
      <h1>{p['h1']}</h1>
      <p class="lede">{p['lede']}</p>
      <div class="hero-cta">
        <a class="btn" href="/contact.html">Scope a {p['short']} engagement <span class="arrow">&#8594;</span></a>
      </div>
    </div>
    <dl class="phero-facts">
{facts}
    </dl>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="split">
      <div><p class="eyebrow">The problem</p><h2>What this practice is actually for.</h2></div>
      <div>
{intro}
        <ul class="prose" style="margin-top:22px;padding-left:20px">
{bullets}
        </ul>
      </div>
    </div>
  </div>
</section>

{live_block}

<section class="band lift">
  <div class="wrap">
    <div class="sec-head">
      <div><p class="eyebrow">Capabilities</p><h2>{p['label']} &mdash; the full stack.</h2></div>
      <p class="sec-count">{len(p['stack'])} capability groups</p>
    </div>
    <dl class="caps">
{caps}
    </dl>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="sec-head">
      <div><p class="eyebrow">Typical engagements</p><h2>How this work usually starts.</h2></div>
      <p class="sec-count">Indicative scope and duration</p>
    </div>
    <div class="exs">
{exs}
    </div>
  </div>
</section>

<section class="dark band">
  <div class="wrap">
    <div class="sec-head">
      <div><p class="eyebrow">What you get</p><h2>Deliverables, every time.</h2></div>
    </div>
    <div class="dels">
{dels}
    </div>
  </div>
</section>

<section class="band lift">
  <div class="wrap">
    <div class="split">
      <div><p class="eyebrow">Questions</p><h2>What clients ask before they commit.</h2></div>
      <div class="acc">
{faqs}
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="sec-head"><div><p class="eyebrow">Also from Windsor Harlow</p><h2 style="font-size:clamp(1.5rem,2.2vw,2rem)">Other practices</h2></div></div>
    <div class="strip">
{more}
    </div>
  </div>
</section>
""" + cta(
        f"Have a {p['short']} problem worth a senior pair of eyes?",
        "Tell us the system, the constraint, and what happens if it is not solved. A senior engineer replies within one business day.")

    return page(f"/practices/{p['slug']}.html",
                f"{p['label']} — Windsor Harlow",
                p["lede"].replace("&mdash;", "—")[:300],
                body, depth=1)


for p in P:
    write(f"practices/{p['slug']}.html", practice_page(p))


# ============================================================ CONTACT
write("contact.html", page(
    "/contact.html", "Contact — Windsor Harlow",
    f"Start a conversation with Windsor Harlow. A senior engineer reads every enquiry and replies within one business day. {MAIL}",
    f"""
<section class="phero wrap">
  <div class="phero-grid">
    <div>
      <p class="crumb">Contact</p>
      <h1>Tell us what you are building &mdash; or what is <em>already broken</em>.</h1>
      <p class="lede">A senior engineer reads every enquiry. If we are the wrong firm for the work, we will say so and tell you what to look for instead.</p>
    </div>
    <dl class="phero-facts">
      <div><dt>Email</dt><dd><a href="mailto:{MAIL}" style="border-bottom:1px solid var(--rule)">{MAIL}</a></dd></div>
      <div><dt>First call</dt><dd>45 minutes, no cost, no deck</dd></div>
      <div><dt>NDA</dt><dd>Signed before scoping, on request</dd></div>
      <div><dt>Registered office</dt><dd>India &mdash; delivering globally</dd></div>
    </dl>
  </div>
</section>

<section class="dark band">
  <div class="wrap">
    <div class="cx">
      <div>
        <p class="eyebrow">What happens next</p>
        <h2>Three steps, no <em>pipeline theatre</em>.</h2>
        <div class="prose" style="margin-top:26px">
          <p class="lede">One &mdash; you send the form. It reaches an engineer, not a CRM queue.</p>
          <p class="lede">Two &mdash; a 45-minute call to understand the system and the constraint. No deck, no discovery invoice.</p>
          <p class="lede">Three &mdash; a written scope with a fixed price where the scope can be fixed, or an honest recommendation to go elsewhere where it cannot.</p>
        </div>
        <dl class="cx-facts">
          <div><dt>Response</dt><dd>One business day, from an engineer</dd></div>
          <div><dt>Americas overlap</dt><dd>Four or more hours daily</dd></div>
          <div><dt>EMEA &amp; APAC overlap</dt><dd>Six or more hours daily</dd></div>
          <div><dt>Data handling</dt><dd><a href="/privacy.html" style="border-bottom:1px solid #123B4D">Privacy &amp; data handling</a></dd></div>
        </dl>
      </div>
      <div>
        <form id="cform" novalidate>
          <div class="f2">
            <div><label for="fn">Name</label><input id="fn" name="name" required autocomplete="name"></div>
            <div><label for="fe">Work email</label><input id="fe" name="email" type="email" required autocomplete="email"></div>
          </div>
          <div class="f2">
            <div><label for="fc">Company</label><input id="fc" name="company" autocomplete="organization"></div>
            <div><label for="fp">Practice</label>
              <select id="fp" name="practice">
                <option>AI, ML &amp; MLOps</option>
                <option>Salesforce</option>
                <option>Cloud, DevOps &amp; Infrastructure</option>
                <option>Web &amp; Distributed Systems</option>
                <option>Mobile</option>
                <option>Commerce &amp; Product Design</option>
                <option>Not sure yet</option>
              </select></div>
          </div>
          <div class="f2">
            <div><label for="fm">Engagement model</label>
              <select id="fm" name="model">
                <option>Fixed-scope project</option><option>Embedded team</option>
                <option>Retainer &amp; support</option><option>Technical advisory</option><option>Advise me</option>
              </select></div>
            <div><label for="ft">Timeline</label>
              <select id="ft" name="timeline">
                <option>Immediate</option><option>This quarter</option><option>Next quarter</option><option>Exploring</option>
              </select></div>
          </div>
          <div><label for="fd">What are you trying to build or fix?</label>
            <textarea id="fd" name="detail" required placeholder="The system, the constraint, and what happens if it is not solved."></textarea></div>
          <div class="hp" aria-hidden="true">
            <label for="fw">Website</label>
            <input id="fw" name="website" type="text" tabindex="-1" autocomplete="off">
          </div>
          <p class="f-msg" id="fmsg" role="status"></p>
          <p><button class="btn" type="submit">Send enquiry <span class="arrow">&#8594;</span></button></p>
          <p class="f-note">Submissions go to {MAIL}.</p>
        </form>
      </div>
    </div>
  </div>
</section>
"""))


# ============================================================ ADMIN
write("admin.html", page(
    "/admin.html", "Publish a case study — Windsor Harlow",
    "Internal console for publishing case studies and portfolio material to the Windsor Harlow site.",
    """
<section class="phero wrap">
  <div class="phero-grid">
    <div>
      <p class="crumb">Internal</p>
      <h1>Publish a <em>case study</em>.</h1>
      <p class="lede">Add a case study, reference build or portfolio document. Published entries appear immediately in the work grid on the home page. Uploads and removals require the admin token set on the server.</p>
    </div>
    <dl class="phero-facts">
      <div><dt>Endpoint</dt><dd>POST /api/portfolio</dd></div>
      <div><dt>Auth</dt><dd>x-admin-token header</dd></div>
      <div><dt>Accepts</dt><dd>Images, PDF, PPT/PPTX, DOC/DOCX &mdash; 15 MB each</dd></div>
    </dl>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="sec-head">
      <div><p class="eyebrow">Current entries</p><h2>What is live now.</h2></div>
      <p class="sec-count" id="workCount"></p>
    </div>
    <p style="margin-bottom:26px"><span class="pill off" data-api><b></b><span>Checking API&hellip;</span></span></p>
    <div class="work-filters" id="workFilters"></div>
    <div class="work-grid" id="workGrid"></div>

    <div class="console" id="console">
      <p class="eyebrow">Add entry</p>
      <h3>New case study</h3>
      <p class="lede" style="font-size:15px">Fill in the copy, attach a cover image or document, and publish. Without the API running, entries are previewed locally so the layout can still be reviewed.</p>
      <form id="pubForm">
        <div class="console-grid">
          <div><label for="pt">Title</label><input id="pt" placeholder="Event-driven order platform at 12k events/minute"></div>
          <div><label for="pc">Practice</label>
            <select id="pc"><option>AI/ML</option><option>Salesforce</option><option>Cloud</option>
              <option>Web</option><option>Mobile</option><option>Commerce</option></select></div>
          <div><label for="ptag">Label</label><input id="ptag" placeholder="Case study / Reference architecture"></div>
          <div><label for="pf">Stack line</label><input id="pf" placeholder="Kafka &middot; Nest.js &middot; PostgreSQL &middot; Pact"></div>
          <div class="full"><label for="pb">Summary</label>
            <textarea id="pb" placeholder="The problem, the architecture, and the measured outcome. Two or three sentences."></textarea></div>
          <div class="full"><label for="ptoken">Admin token</label><input id="ptoken" type="password" placeholder="WH_ADMIN_TOKEN"></div>
        </div>

        <div class="drop" id="drop">
          <h3>Attach cover image or document</h3>
          <p>Drop files here, or choose them. The first image becomes the card cover.</p>
          <p style="margin-top:20px"><button class="btn btn-ghost" type="button" id="pick">Choose files</button></p>
          <label for="file" style="position:absolute;left:-9999px">Case study files</label>
          <input type="file" id="file" multiple accept="image/*,.pdf,.ppt,.pptx,.doc,.docx">
        </div>

        <p class="state" id="pubState"></p>
        <p><button class="btn" type="submit">Publish entry <span class="arrow">&#8594;</span></button></p>
      </form>
    </div>
  </div>
</section>
""", extra_head='<meta name="robots" content="noindex, nofollow">'))

print("done")
