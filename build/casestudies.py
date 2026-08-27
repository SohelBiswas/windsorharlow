# -*- coding: utf-8 -*-
"""Case-study detail pages. One entry per project; the page shape is fixed:
   what it is, the problem, what we built, what it does, what it runs on,
   what came out of it."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from shell import page, cta
from build import write

# --- feature glyphs -------------------------------------------------------
# 24x24 stroke icons, inherit currentColor. Kept deliberately plain.
G = {
 "scan":   '<path d="M3 8V4h4M17 4h4v4M21 16v4h-4M7 20H3v-4"/><path d="M3 12h18"/>',
 "speech": '<path d="M4 5h16v11H9l-5 4V5z"/><path d="M8 9h8M8 12.5h5"/>',
 "sort":   '<path d="M4 6h16M4 12h11M4 18h6"/>',
 "target": '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3"/>',
 "window": '<rect x="3" y="4" width="18" height="16" rx="1.5"/><path d="M3 9h18M6.5 6.5h.01M9.5 6.5h.01"/>',
 "gear":   '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M2 12h3M19 12h3M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1"/>',
 "wifi":   '<path d="M2.5 8.5a15 15 0 0 1 19 0M5.5 12a10.5 10.5 0 0 1 13 0M8.5 15.5a6 6 0 0 1 7 0"/><circle cx="12" cy="19" r="1.4"/>',
 "radar":  '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4.5"/><path d="M12 12l6-4"/>',
 "phone":  '<rect x="6" y="2.5" width="12" height="19" rx="2"/><path d="M10.5 18.5h3"/>',
 "drop":   '<path d="M12 3v11"/><path d="M8 10l4 4 4-4"/><path d="M4 17v3h16v-3"/>',
 "pulse":  '<path d="M2 12h4l2.5-6 4 12L15 12h7"/>',
 "layers": '<path d="M12 3l9 5-9 5-9-5 9-5z"/><path d="M3 13l9 5 9-5"/>',
 "branch": '<circle cx="6" cy="5" r="2.5"/><circle cx="6" cy="19" r="2.5"/><circle cx="18" cy="12" r="2.5"/><path d="M6 7.5v9M8.5 5H14a2 2 0 0 1 2 2v3M8.5 19H14a2 2 0 0 0 2-2v-3"/>',
 "cube":   '<path d="M12 2.5l8 4.5v9l-8 4.5-8-4.5v-9l8-4.5z"/><path d="M4 7l8 4.5 8-4.5M12 11.5V20"/>',
 "lock":   '<rect x="4" y="10.5" width="16" height="10" rx="2"/><path d="M8 10.5V7a4 4 0 0 1 8 0v3.5"/><path d="M12 14v3"/>',
 "key":    '<circle cx="8" cy="12" r="4"/><path d="M12 12h9M18 12v3M15.5 12v2.4"/>',
 "shield": '<path d="M12 3l7.5 3v5.5c0 4-3.1 7.6-7.5 9-4.4-1.4-7.5-5-7.5-9V6L12 3z"/><path d="M9.2 12l2 2 3.6-3.8"/>',
 "clock":  '<circle cx="12" cy="12" r="8.5"/><path d="M12 7v5.2l3.2 2"/>',
 "heart":  '<path d="M3 12h4l2-5 3 10 2.5-5H21"/>',
 "arrows": '<path d="M4 8h13M13 4l4 4-4 4"/><path d="M20 16H7M11 12l-4 4 4 4"/>',
}


def glyph(k):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true">{G[k]}</svg>')


CASES = [
    dict(
        slug="accessibility-testing",
        name="Accessibility Test Framework",
        cat="Quality Engineering",
        title="Accessibility testing that produces evidence, not a pass mark",
        stand="Automated WCAG scanning wired into a BDD suite, with every violation rendered as a report a non-engineer can act on.",
        stack=["Java", "Selenium", "Cucumber", "Deque Axe", "React", "Node.js"],
        about=[
            "An automated accessibility audit that runs like any other test. Selenium drives real pages, the Deque Axe engine scans the rendered DOM, and a React interface turns the raw findings into a report the whole team can read.",
        ],
        meta=[("Type", "Test framework"),
              ("Target", "Any web application"),
              ("Output", "JSON &rarr; HTML report")],
        problem=[
            "Accessibility is usually checked once, by hand, just before release &mdash; when it is far too late and far too expensive to fix.",
            "The tools that automate it return raw JSON. An engineer can read that. A product owner, a designer or a compliance officer cannot, so the findings stall.",
        ],
        solution=[
            ("Scanning inside the test suite",
             "Deque Axe runs against real pages driven by Selenium, so accessibility is checked on the rendered DOM in the same run as every other test."),
            ("Scenarios in plain English",
             "Cucumber keeps each check readable as a sentence, so the suite doubles as documentation of what is being enforced."),
            ("A report for the whole team",
             "The JSON is transformed into a React interface grouping violations by severity and by page &mdash; readable without opening a terminal."),
        ],
        features=[
            ("scan",   "Rule-based scanning",   "Axe checks the rendered page, not the source."),
            ("speech", "Plain-English tests",   "Each scenario reads as a sentence in Gherkin."),
            ("sort",   "Grouped by severity",   "Critical to minor, and by page."),
            ("target", "Element-level detail",  "Every finding names the element and the rule."),
            ("window", "Browser-based report",  "Opens as a page, not a terminal dump."),
            ("gear",   "Fits into CI",          "Runs with the rest of the suite on every build."),
        ],
        tech=[
            ("Language",      ["Java"]),
            ("Browser driver", ["Selenium WebDriver"]),
            ("Specification", ["Cucumber", "Gherkin"]),
            ("Audit engine",  ["Deque Axe"]),
            ("Reporting UI",  ["React", "Tailwind CSS", "Node.js"]),
        ],
        result=[
            ("Every build", "Accessibility runs with the rest of the suite instead of as a pre-release scramble."),
            ("Whole team", "Violations land somewhere designers and product owners can act on them."),
            ("Evidence trail", "Each run leaves a report that can be attached to a procurement or compliance response."),
        ],
        note="Built in-house as a working reference for how we approach quality engineering.",
    ),
    dict(
        slug="air-bridge",
        name="Air Bridge",
        cat="Developer Tooling",
        title="Wireless Android debugging without the command line",
        stand="A desktop app that discovers devices on the network, connects ADB over Wi-Fi and installs builds by drag-and-drop.",
        stack=["Electron", "Node.js", "ADB", "electron-builder"],
        about=[
            "A desktop client that sits on top of the Android Debug Bridge. It finds handsets already in wireless-debugging mode, connects to them over Wi-Fi, reports what they are, and installs an APK when you drop one on the window.",
        ],
        meta=[("Type", "Desktop application"),
              ("Packages for", "Windows &middot; macOS &middot; Linux"),
              ("Talks to", "Android over ADB")],
        problem=[
            "Wireless debugging on Android is a sequence of terminal commands and an IP address that changes every time the device rejoins the network.",
            "It is a small friction repeated many times a day, and it quietly excludes QA testers and designers who need a build on a device but do not live in a shell.",
        ],
        solution=[
            ("Discovery instead of typing",
             "The app finds devices on the network that already have wireless debugging enabled, so nobody hunts for an IP."),
            ("The device, described",
             "Brand, model, Android version and battery are shown on connect &mdash; enough to know you are on the right handset before you install."),
            ("Drag a build onto it",
             "APK installation is a drop target rather than a command, with connection state shown plainly rather than inferred from silence."),
        ],
        features=[
            ("wifi",   "Connect over Wi-Fi",    "Pair by IP and port, no cable."),
            ("radar",  "Nearby devices",        "Finds handsets already in debugging mode."),
            ("phone",  "Device readout",        "Brand, model, Android version, battery."),
            ("drop",   "Drag-and-drop install", "Drop an APK on the window; it installs."),
            ("pulse",  "Live connection state", "Shown plainly, not inferred from silence."),
            ("layers", "One codebase, three OSes", "Packaged by electron-builder."),
        ],
        tech=[
            ("Shell",        ["Electron"]),
            ("Runtime",      ["Node.js"]),
            ("Device bridge", ["ADB"]),
            ("Packaging",    ["electron-builder"]),
            ("Bundled",      ["scrcpy"]),
        ],
        result=[
            ("Anyone on the team", "Getting a build onto a device stops being an engineering-only task."),
            ("Three platforms", "One Electron codebase ships to Windows, macOS and Linux."),
            ("Fewer interruptions", "Testers stop queueing behind whoever owns the cable."),
        ],
        note="Built in-house to remove a daily friction from our own mobile work.",
    ),

    dict(
        slug="terraform-aws",
        name="AWS Infrastructure as Code",
        cat="Cloud & Infrastructure",
        title="An AWS environment nobody applies from a laptop",
        stand="A full environment in modular Terraform, with a pipeline that plans on every pull request and applies on merge.",
        stack=["Terraform", "AWS", "GitHub Actions", "OIDC", "DynamoDB"],
        about=[
            "A complete AWS environment defined in modular Terraform and applied by CI &mdash; VPC and networking, compute, storage, and the identity boundaries around them, with state held remotely and locked so more than one engineer can work on it safely.",
        ],
        meta=[("Type", "Infrastructure as code"),
              ("Applied by", "GitHub Actions"),
              ("Auth", "OIDC, no stored keys")],
        problem=[
            "Clicking through the AWS console produces an environment nobody can rebuild. The settings live in one person&rsquo;s memory, staging quietly drifts from production, and a rollback turns into archaeology.",
            "The usual fix &mdash; putting it in Terraform &mdash; only half solves it. If engineers still run <code>apply</code> from their own machines, you have swapped an unrepeatable environment for an unrepeatable process.",
        ],
        solution=[
            ("Modules, not one long file",
             "Network, compute, storage and IAM are separate modules with their own inputs, so an environment is composed rather than copied and edited."),
            ("State that two people can share",
             "An S3 backend with DynamoDB locking, so a second apply waits instead of corrupting the first."),
            ("The pipeline holds the credentials",
             "GitHub Actions plans on every pull request and posts the plan back for review, then applies on merge &mdash; authenticating to AWS by OIDC rather than long-lived keys in secrets."),
        ],
        features=[
            ("cube",   "Composed environments",  "Four modules, assembled per environment."),
            ("layers", "Remote locked state",    "S3 backend, DynamoDB lock table."),
            ("branch", "Plan on every PR",       "The diff is reviewed before it exists."),
            ("gear",   "Apply on merge",         "One path to production, and it is audited."),
            ("shield", "OIDC, not stored keys",  "No AWS credentials live in GitHub."),
            ("arrows", "Reproducible teardown",  "Stands up and comes down the same way."),
        ],
        tech=[
            ("Provisioning",  ["Terraform"]),
            ("Cloud",         ["AWS", "VPC", "EC2", "EBS", "S3", "IAM"]),
            ("State",         ["S3 backend", "DynamoDB locking"]),
            ("Pipeline",      ["GitHub Actions"]),
            ("Authentication", ["OIDC to an IAM role"]),
        ],
        result=[
            ("Rebuildable", "The environment is a repository, not a memory. Anyone can stand up a copy."),
            ("Reviewable", "Every infrastructure change arrives as a diff with its plan attached."),
            ("No laptop applies", "Credentials live in the pipeline, so the audit trail is the git history."),
        ],
        note="Built in-house, and the pattern we apply to client infrastructure.",
    ),
    dict(
        slug="eks-deploy",
        name="Kubernetes Delivery on EKS",
        cat="Platform Engineering",
        title="Shipping to Kubernetes is a merge, not a run of kubectl",
        stand="A containerised application on Amazon EKS with rolling updates, health probes and a build-push-deploy workflow.",
        stack=["Kubernetes", "Amazon EKS", "Docker", "GitHub Actions"],
        about=[
            "A web application containerised and deployed to Amazon EKS, with the manifests that decide what happens during a release and the pipeline that performs it. The interesting part is not that it runs &mdash; it is what happens on the fourth deploy of the day.",
        ],
        meta=[("Type", "Container platform"),
              ("Runs on", "Amazon EKS"),
              ("Released by", "GitHub Actions")],
        problem=[
            "A container that runs on a laptop proves very little. The questions that decide whether a platform is usable come later: what happens to traffic during a deploy, what happens when a pod is unhealthy, and who is permitted to push.",
            "Answer those with manual <code>kubectl</code> commands and the answers change depending on who is at the keyboard and whether they remembered the runbook.",
        ],
        solution=[
            ("Rolling updates by default",
             "The Deployment replaces pods gradually rather than all at once, so a release does not drop traffic and a bad build does not take the service with it."),
            ("Probes that make the decision",
             "Liveness and readiness probes decide when a pod is fit to serve, so an unhealthy instance is replaced instead of quietly returning errors."),
            ("The pipeline does the deploy",
             "GitHub Actions builds the image, pushes it to the registry and rolls the deployment. Shipping is a merge, and the record of what shipped is the commit history."),
        ],
        features=[
            ("cube",   "Containerised build",   "One image, promoted rather than rebuilt."),
            ("arrows", "Rolling updates",       "Pods replaced gradually, traffic held."),
            ("heart",  "Liveness &amp; readiness", "An unhealthy pod is replaced, not served."),
            ("branch", "Build, push, roll",     "Three steps, one workflow, no kubectl."),
            ("layers", "Ingress in front",      "Routing declared with the rest of it."),
            ("gear",   "Repeatable releases",   "The fourth deploy looks like the first."),
        ],
        tech=[
            ("Orchestration", ["Kubernetes", "Amazon EKS"]),
            ("Containers",    ["Docker"]),
            ("Manifests",     ["Deployment", "Service", "Ingress"]),
            ("Health",        ["Liveness probes", "Readiness probes"]),
            ("Pipeline",      ["GitHub Actions", "Container registry"]),
        ],
        result=[
            ("No release window", "Rolling updates and probes mean a deploy is not an event anyone has to schedule."),
            ("Anyone can ship", "Merging is the deploy, so releasing is not gated on who knows the commands."),
            ("Recoverable", "A bad image is replaced by rolling the previous one, on the same path."),
        ],
        note="Built in-house as the reference for how we hand over a container platform.",
    ),
    dict(
        slug="rune",
        name="Rune",
        cat="Security Engineering",
        title="A secrets manager whose key never touches disk",
        stand="A self-hosted vault in a single Go binary &mdash; encrypted at rest, sealed by default, with the key held only in memory.",
        stack=["Go", "AES-256-GCM", "Argon2id", "BoltDB"],
        about=[
            "A minimal secrets manager for developers and small teams who want their credentials on infrastructure they control. A CLI and an HTTP server in one binary, with no cloud services, no agents and no external dependencies.",
        ],
        meta=[("Type", "Self-hosted vault"),
              ("Runs on", "macOS &middot; Linux &middot; Windows"),
              ("Storage", "Encrypted, on your disk")],
        problem=[
            "Every serious secrets manager assumes you already have cloud infrastructure and someone to operate it. For a solo developer or a team of four, that is a great deal of machinery to protect a handful of credentials.",
            "So the credentials stay in a <code>.env</code> file, in plain text, copied between machines over chat &mdash; which is the outcome the machinery existed to prevent.",
        ],
        solution=[
            ("Sealed until you open it",
             "The vault starts locked and nothing is readable until it is unsealed with a passphrase. Argon2id derives the key, so guessing it is expensive in memory as well as time."),
            ("The key lives in memory only",
             "Once unsealed, the encryption key exists in the running process and is never written to disk. Seal the vault and it is gone until someone types the passphrase again."),
            ("Encrypted per secret, not per file",
             "AES-256-GCM with a unique nonce for every secret, so the storage file gives away nothing &mdash; not even which entries changed. Tokens are hashed before they are stored."),
        ],
        features=[
            ("lock",   "Sealed by default",     "Starts locked. Unsealing is deliberate."),
            ("key",    "Key in memory only",    "Never written to disk, gone on seal."),
            ("shield", "AES-256-GCM",           "Unique nonce per secret."),
            ("scan",   "Argon2id derivation",   "Memory-hard, resists GPU attacks."),
            ("layers", "Namespaces",            "Isolated containers for separate work."),
            ("gear",   "Tokens, hashed",        "Created, listed and revoked; never stored raw."),
        ],
        tech=[
            ("Language",   ["Go"]),
            ("Encryption", ["AES-256-GCM"]),
            ("Key derivation", ["Argon2id"]),
            ("Storage",    ["BoltDB, embedded"]),
            ("Interfaces", ["CLI", "HTTP API"]),
        ],
        result=[
            ("No infrastructure", "A vault that is one binary, on hardware you already own."),
            ("A stated threat model", "It protects against an attacker with your disk. That boundary is written down rather than implied."),
            ("Small enough to read", "Few enough moving parts that a solo developer can understand what protects them."),
        ],
        note="Built in-house by our engineers, and the tool we use on our own work.",
    ),
]


def render(c):
    stack = "".join(f"<li>{s}</li>" for s in c["stack"])
    about = "".join(f"<p>{p}</p>" for p in c["about"])
    meta = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in c["meta"])
    problem = "".join(f"<p>{p}</p>" for p in c["problem"])
    solution = "".join(
        f'<div class="cs-step"><span class="cs-n">0{i+1}</span>'
        f"<h3>{h}</h3><p>{b}</p></div>" for i, (h, b) in enumerate(c["solution"]))
    feats = "".join(
        f'<div class="cs-feat"><i>{glyph(g)}</i><b>{t}</b><p>{d}</p></div>'
        for g, t, d in c["features"])
    tech = "".join(
        f'<div class="cs-tech-row"><dt>{k}</dt><dd>'
        + "".join(f"<span>{v}</span>" for v in vals) + "</dd></div>"
        for k, vals in c["tech"])
    result = "".join(
        f'<div class="cs-out"><b>{h}</b><p>{b}</p></div>' for h, b in c["result"])
    return f"""
<section class="phero wrap cs-hero">
  <p class="eyebrow">Case study &middot; {c['cat']}</p>
  <p class="cs-name"><i></i>{c['name']}</p>
  <h1>{c['title']}</h1>
  <p class="lede">{c['stand']}</p>
  <ul class="cs-stack">{stack}</ul>
</section>

<section class="band lift" id="about">
  <div class="wrap cs-grid">
    <div><p class="eyebrow">What it is</p></div>
    <div class="cs-body">{about}
      <dl class="cs-meta">{meta}</dl>
    </div>
  </div>
</section>

<section class="band" id="problem">
  <div class="wrap cs-grid">
    <div><p class="eyebrow">The problem</p></div>
    <div class="cs-body">{problem}</div>
  </div>
</section>

<section class="dark band" id="solution">
  <div class="wrap">
    <div class="sec-head"><div><p class="eyebrow">What we built</p>
      <h2>Three decisions that shaped it.</h2></div></div>
    <div class="cs-steps">{solution}</div>
  </div>
</section>

<section class="band lift" id="features">
  <div class="wrap">
    <div class="sec-head"><div><p class="eyebrow">What it does</p>
      <h2>Six things, plainly.</h2></div></div>
    <div class="cs-feats">{feats}</div>
    <div class="cs-tech">
      <p class="eyebrow">Built with</p>
      <dl class="cs-tech-list">{tech}</dl>
    </div>
  </div>
</section>

<section class="band" id="result">
  <div class="wrap">
    <div class="sec-head"><div><p class="eyebrow">What came out of it</p>
      <h2>The outcome.</h2></div></div>
    <div class="cs-outs">{result}</div>
    <p class="cs-note">{c['note']}</p>
    <p style="margin-top:26px"><a class="btn btn-ghost" href="/index.html#work">All work <span class="arrow">&#8594;</span></a></p>
  </div>
</section>
""" + cta("Have a problem shaped like this one?",
          "Describe the situation and a senior engineer will tell you what it needs.")


for c in CASES:
    write(f"work/{c['slug']}.html",
          page(f"/work/{c['slug']}.html", f"{c['name']} — {c['title']} — Windsor Harlow",
               c["stand"], render(c), depth=1))
print("case studies done")
