# -*- coding: utf-8 -*-
"""Per-practice content. This is the source of truth for the practice pages."""

P = []

# ------------------------------------------------------------------ AI / ML
P.append(dict(
    id="ai",
    live_h="Retrieval that refuses rather than invents.", live_p="Dense and sparse retrieval fused, re-ranked, with a floor below which the system declines to answer. The eval gate blocks the deploy when faithfulness drops.", slug="ai-ml", cat="AI/ML", short="AI/ML", label="AI, ML & MLOps",
    h1="Retrieval and LLM systems that <em>hold up in production</em>.",
    lede="Most AI pilots die in month two. We build the parts that decide whether yours survives.",
    facts=[("Typical first engagement", "6&ndash;10 weeks, fixed scope"),
           ("Starts with", "An eval set built from your real questions"),
           ("Ends with", "Runbooks, eval harness and cost model in your repo")],
    intro=[
        "The demo works because someone asked it three friendly questions. Production breaks on the fourth kind.",
        "So we build an evaluation set from real user questions first, then measure every retrieval, prompt and model change against it. You get a number, not an opinion."],
    bullets=[
        "Grounding on your own corpus &mdash; documents, tickets, code, CRM records, database rows",
        "Guardrails that refuse rather than invent when retrieval comes back thin",
        "Citations traced to source spans, so a reviewer can verify an answer in seconds",
        "Cost per resolved query modelled at design time, not discovered on the first invoice"],
    stack=[
        ("RAG systems", "Retrieval pipeline design, pgvector, Pinecone, Weaviate, chunking and metadata strategy, prompt/response evaluation, output guardrails"),
        ("Retrieval quality", "Hybrid dense + sparse/BM25 search, re-ranking models, multi-modal document and image retrieval"),
        ("Agentic systems", "LangGraph, multi-agent workflows, tool and function-calling design, ReAct-pattern agents, human-in-the-loop checkpoints"),
        ("Orchestration", "LangChain, LlamaIndex, Semantic Kernel"),
        ("Serving &amp; inference", "vLLM, Triton Inference Server, SageMaker and Vertex AI endpoints, batching and quantisation, inference cost optimisation"),
        ("Fine-tuning", "LoRA, QLoRA, parameter-efficient fine-tuning, instruction tuning, dataset construction"),
        ("Evaluation", "Automated RAG evaluation harnesses, LLM tracing and debugging, regression gates in CI, custom eval pipelines"),
        ("MLOps", "Deployment pipelines, model versioning and registry, CI/CD for ML, drift monitoring, experiment tracking"),
        ("Platforms", "MLflow, Kubeflow, Weights &amp; Biases, feature pipelines with Airflow and dbt")],
    examples=[
        dict(tag="Fixed scope", h4="Internal knowledge assistant",
             p="Hybrid retrieval across scattered internal documentation, with citation enforcement and an eval harness that gates every prompt change in CI.",
             meta="6&ndash;10 weeks &middot; pgvector &middot; re-ranking &middot; eval harness"),
        dict(tag="Fixed scope", h4="Agentic back-office workflow",
             p="A multi-step agent that reads a request, gathers what it needs from your systems, drafts the action, and stops for human approval where the cost of error is real.",
             meta="8&ndash;12 weeks &middot; LangGraph &middot; tool design &middot; audit trail"),
        dict(tag="Advisory", h4="AI feature audit",
             p="Independent review of a pilot that is not converting: retrieval quality, prompt architecture, latency budget, unit economics, and whether the use case is winnable at all.",
             meta="2&ndash;3 weeks &middot; written findings &middot; prioritised remediation")],
    dels=[
        dict(h4="Evaluation harness", p="A versioned eval set with pass thresholds wired into CI, so quality regressions fail a build rather than a customer conversation."),
        dict(h4="Retrieval architecture", p="Documented chunking, embedding, hybrid search and re-ranking decisions with the trade-offs and the benchmark numbers behind each."),
        dict(h4="Cost and latency model", p="Cost per query and p95 latency at your projected volume, with the levers that move them ranked by effort."),
        dict(h4="Operating runbook", p="What to do when quality drops, retrieval goes stale, or a provider deprecates a model &mdash; written for your on-call engineer.")],
    faqs=[
        ("Do we need to fine-tune a model?",
         "Usually not first. In most engagements retrieval quality, prompt architecture and re-ranking move accuracy far more than fine-tuning, at a fraction of the cost and with none of the retraining burden. We fine-tune when there is a measured ceiling that retrieval cannot lift &mdash; typically format adherence, domain vocabulary, or latency-driven use of a smaller model. We will tell you which case you are in before you spend on it."),
        ("Can this run without sending our data to a third-party provider?",
         "Yes. We deploy open-weight models on your own infrastructure with vLLM or Triton when data residency, contractual restrictions or cost make hosted APIs unworkable. The trade-off is real &mdash; you take on GPU capacity and evaluation burden &mdash; and we will quantify it before you commit rather than after."),
        ("How do you stop it inventing answers?",
         "Three layers, none of which is a prompt asking it politely. Retrieval returns scored passages and the system refuses when scores fall below a floor. Answers must cite retrieved spans, and uncited claims are stripped. The eval harness includes questions with no correct answer, and refusing them correctly is a passing result.")],
))

# ------------------------------------------------------------------ Salesforce
P.append(dict(
    id="salesforce",
    live_h="Bulk-safe, governor-aware, actually tested.", live_p="One query, one DML, tested at ten thousand records &mdash; not the two that clear a coverage gate. Metadata in version control, deployed through a pipeline.", slug="salesforce", cat="Salesforce", short="Salesforce", label="Salesforce Development",
    h1="Salesforce platforms that <em>outlive the admin who inherits them</em>.",
    lede="Governor-safe Apex, tested triggers, automation a new admin can read.",
    facts=[("Typical first engagement", "4&ndash;8 weeks, fixed scope"),
           ("Starts with", "Org audit &mdash; automation map and technical debt register"),
           ("Ends with", "Test coverage, deployment pipeline and documented data model")],
    intro=[
        "Anyone can ship a flow. Fewer people can tell you why three generations of automation all fire on the same object, in an order nobody controls, at quarter end.",
        "We treat an org as production software: version control, deployment pipelines, real test coverage, an automation map. The measure is whether your admin can change it safely six months after we leave."],
    bullets=[
        "One automation strategy per object instead of four competing ones",
        "Apex written against governor limits, bulk-tested at realistic volumes",
        "Integrations that fail loudly and retry, rather than dropping records silently",
        "Deployment through a pipeline, not by clicking in production"],
    stack=[
        ("Development", "Apex, Lightning Web Components (LWC), triggers with a single-handler pattern, Batch Apex, Queueable and scheduled jobs"),
        ("Automation", "Flow automation and process optimisation, consolidation of legacy Process Builder and Workflow Rules"),
        ("Data", "SOQL optimisation, data modelling, custom objects, fields, validation rules, large-data-volume strategy"),
        ("Integration", "REST API integrations from Salesforce to external systems, Platform Events, middleware patterns, retry and reconciliation"),
        ("Clouds", "Sales Cloud customisation, Experience Cloud development, B2B Commerce Cloud support"),
        ("Engineering discipline", "Version-controlled metadata, CI deployment pipelines, Apex test coverage that asserts behaviour rather than lines")],
    examples=[
        dict(tag="Fixed scope", h4="Automation consolidation",
             p="Untangle overlapping triggers, flows and process builders on your core objects into one documented, order-controlled automation layer with tests.",
             meta="4&ndash;7 weeks &middot; automation map &middot; regression tests"),
        dict(tag="Fixed scope", h4="Integration build",
             p="Bidirectional integration between Salesforce and an ERP, billing system or data warehouse &mdash; with idempotency, retries, reconciliation reporting and alerting.",
             meta="5&ndash;9 weeks &middot; REST &middot; Platform Events &middot; runbook"),
        dict(tag="Embedded", h4="Salesforce capacity for a product team",
             p="A senior Salesforce engineer inside your sprint process for teams shipping continuously against the platform without a full-time hire.",
             meta="Rolling monthly &middot; your board, your standards")],
    dels=[
        dict(h4="Automation map", p="Every trigger, flow and rule on your core objects, what fires when, and which ones are redundant or actively fighting each other."),
        dict(h4="Deployment pipeline", p="Metadata under version control with CI validation, so changes move through sandboxes instead of being clicked in production."),
        dict(h4="Test coverage that means something", p="Bulk-safe Apex tests asserting real behaviour at realistic volumes &mdash; not coverage padding written to clear a deployment gate."),
        dict(h4="Admin handover", p="A written walkthrough of the data model, integration contracts and known constraints, aimed at the person who owns the org next.")],
    faqs=[
        ("Do you replace our Salesforce admin?",
         "No, and you should be wary of anyone who says yes. Admins own configuration, users and process; we handle the engineering layer &mdash; Apex, LWC, integrations, deployment and performance. The best outcome is your admin ending the engagement with more confidence to make changes, not less."),
        ("Our org is a decade of undocumented customisation. Where do you even start?",
         "With an audit, priced separately and small. Two to three weeks produces an automation map, a technical debt register ranked by risk, and a recommendation on sequence. That artefact is useful whether or not you continue with us, and it means the build phase is scoped against reality rather than optimism."),
        ("Flow or Apex?",
         "Flow where admins should own the logic and the volume is modest. Apex where you need bulk safety, complex branching, external calls or testable business rules. The failure mode we see most often is complex logic pushed into Flow because it felt faster, then hitting limits at quarter end with no tests to refactor against.")],
))

# ------------------------------------------------------------------ Cloud
P.append(dict(
    id="cloud",
    live_h="Everything reproducible from code.", live_p="No hand-built resources in production, cost tags applied at creation, and a policy scan that fails the plan before anything reaches an account.", slug="cloud", cat="Cloud", short="Cloud", label="Cloud, DevOps & Infrastructure",
    h1="Cloud infrastructure <em>your own team can still operate</em>.",
    lede="Cost and operability designed in as requirements, not cleaned up after the invoice arrives.",
    facts=[("Typical first engagement", "6&ndash;14 weeks, fixed scope"),
           ("Starts with", "Architecture and cost review against your actual usage"),
           ("Ends with", "Terraform in your repo, runbooks, and on-call handover")],
    intro=[
        "The expensive cloud mistakes are architectural and made early. Default instance families, egress nobody modelled, a Kubernetes cluster running four services.",
        "We design infrastructure for the team that inherits it: fewer moving parts, everything in Terraform, and a documented answer to what each alert means at 3am."],
    bullets=[
        "Everything reproducible from code &mdash; no hand-built resources in production",
        "Cost modelled at design time and tagged for attribution from day one",
        "Failure modes written down, with the recovery path tested rather than assumed",
        "Migrations sequenced so there is always a way back"],
    stack=[
        ("AWS", "EC2, Lambda, ECS/EKS, RDS, S3, CloudFront, API Gateway, IAM, VPC design, CloudFormation &amp; CDK"),
        ("Google Cloud", "Compute Engine, GKE, Cloud Functions, Cloud Run, BigQuery, Cloud Storage"),
        ("Azure", "Azure VMs, AKS, Azure Functions, Azure DevOps, Azure Active Directory"),
        ("Infrastructure as code", "Terraform, CloudFormation, AWS CDK, module design and state strategy"),
        ("Containers &amp; orchestration", "Docker, Kubernetes on EKS / GKE / AKS, Helm, Istio, Linkerd, GitOps with ArgoCD and Flux, Operators and CRDs, HPA / VPA / KEDA autoscaling"),
        ("CI/CD", "GitHub Actions, GitLab CI, Jenkins"),
        ("Serverless", "Step Functions, EventBridge, Azure Logic Apps, GCP Workflows, Lambda@Edge, CloudFront Functions"),
        ("Data infrastructure", "Kafka / Amazon MSK, Redis / ElastiCache, Aurora, DynamoDB, data lakes on S3 + Glue + Athena, Snowflake, Redshift, BigQuery"),
        ("Migrations", "Lift-and-shift, replatforming and full re-architecture &mdash; from on-premise or between providers"),
        ("Resilience", "Multi-region architecture, active-active and active-passive failover, backup and recovery strategy, tested restores"),
        ("Security", "Vault, AWS Secrets Manager, Azure Key Vault, OPA, Checkov, tfsec, zero-trust network design, SSO, IAM policy design, SSL/TLS"),
        ("Observability", "Dynatrace, CloudWatch, APM and log aggregation, alerting that maps to runbooks"),
        ("FinOps", "Rightsizing, reserved instance and savings plan strategy, idle-resource audits, tagging, Kubecost showback and chargeback")],
    examples=[
        dict(tag="Fixed scope", h4="On-premise to cloud migration",
             p="Assessment, landing zone, and a sequenced cutover with rollback at every stage. Replatforming where it pays for itself, lift-and-shift where it does not.",
             meta="10&ndash;16 weeks &middot; Terraform &middot; staged cutover"),
        dict(tag="Advisory", h4="Cloud cost and architecture audit",
             p="Where the spend actually goes, what is idle, what is over-provisioned, and which architectural decisions are generating recurring cost. Findings ranked by saving against effort.",
             meta="2&ndash;3 weeks &middot; written findings &middot; savings model"),
        dict(tag="Retainer", h4="Platform operation and on-call",
             p="Ongoing operation of a live platform: patching, capacity, incident response and continuous cost control, with a named senior engineer.",
             meta="Monthly &middot; defined response times")],
    dels=[
        dict(h4="Infrastructure as code", p="Your entire environment in Terraform, in your repository, reviewable and reproducible from a clean account."),
        dict(h4="Architecture decision records", p="Every significant choice with the alternatives considered, the trade-off accepted, and the conditions under which it should be revisited."),
        dict(h4="Runbooks and alerting", p="Alerts that map to documented procedures, so on-call means following a runbook rather than reverse-engineering a system."),
        dict(h4="Cost baseline", p="Tagged, attributable spend with a projection at your growth rate and the specific levers available to change it.")],
    faqs=[
        ("Which cloud should we be on?",
         "Usually the one your team already knows, unless a specific requirement overrides that &mdash; a managed service you depend on, a data residency rule, or committed spend you have already negotiated. Migration between providers rarely pays for itself on cost grounds alone, and the retraining bill is routinely underestimated. We will say so even when it means a smaller engagement."),
        ("Do we need Kubernetes?",
         "Often not. Kubernetes earns its operational cost when you have many services, several teams deploying independently, and a real need for portability. For four services and one team, ECS, Cloud Run or plain container hosting will cost less to build and far less to run. We will recommend the smaller thing when the smaller thing is correct."),
        ("Can you work with our existing DevOps team?",
         "That is the preferred arrangement. We embed in your sprint process, work in your repositories to your review standards, and document as we go so that capability stays with your team. Handover is a requirement of the engagement rather than a phase we run out of time for.")],
))

# ------------------------------------------------------------------ Web
P.append(dict(
    id="web",
    live_h="Bulk-safe services, typed contracts, tested at load.",
    live_p="Spring Boot where transactional integrity matters, Node and Go where iteration speed does. Contract tests underneath, so one team can deploy without asking four others.",
    slug="web", cat="Web", short="Backend & Web", label="Backend, Web & Distributed Systems",
    h1="Backends that scale past the first version <em>without a rewrite</em>.",
    lede = "Distributed patterns that survive growth, without the premature architecture that sinks a product first.",
    facts=[("Typical first engagement", "8&ndash;16 weeks, fixed scope"),
           ("Starts with", "Domain model and the constraints that actually bind"),
           ("Ends with", "Deployed system, tests, CI and architecture records")],
    intro=[
        "Two ways to lose here: a monolith with no seams that hits a wall at scale, or twelve microservices for a product with four hundred users.",
        "We size the architecture to the next eighteen months. Clear domain boundaries so it can be split when that is justified, and boring, well-tested code everywhere else."],
    bullets=[
        "Domain boundaries defined before the service boundaries",
        "Contract tests between services, so independent deploys stay safe",
        "Migrations, tests and CI from the first commit rather than the last sprint",
        "Performance work driven by profiling rather than by intuition"],
    stack=[
        ("Java &amp; JVM", "Spring Boot, Spring Cloud, Spring Security, Hibernate/JPA, Maven and Gradle, JUnit and Testcontainers, Kotlin on the JVM"),
        ("Node &amp; TypeScript", "Node.js, Nest.js, Express, Fastify, Prisma and TypeORM, end-to-end typed APIs"),
        ("Frontend", "React, Next.js, Vue.js, TypeScript, design-system implementation, SSR and edge rendering"),
        ("Additional stacks", "Go (Gin, Fiber), Python (FastAPI, Django), .NET Core, Rust (Axum) &mdash; for teams standardised outside our primary toolset"),
        ("Distributed design", "Microservices, event-driven architecture, Kafka, RabbitMQ, SQS, API gateway design, service-to-service authentication"),
        ("API paradigms", "REST, GraphQL (Apollo), gRPC, WebSockets, Server-Sent Events"),
        ("Architecture patterns", "Event sourcing and CQRS, saga pattern for distributed transactions, domain-driven design"),
        ("Data layer", "Advanced PostgreSQL indexing, partitioning and replication, MongoDB, multi-tenant data architecture, Redis caching strategy"),
        ("Auth", "OAuth2 / OIDC, JWT, RBAC and ABAC authorisation models"),
        ("Quality", "Contract testing with Pact, load testing with k6 and JMeter, observability-driven performance tuning")],
    examples=[
        dict(tag="Fixed scope", h4="Backend platform build",
             p="A greenfield product build to a defined scope: domain model, API, interface, deployment pipeline and the seams that let it be extended without unpicking.",
             meta="10&ndash;16 weeks &middot; fixed price &middot; handover included"),
        dict(tag="Fixed scope", h4="Monolith decomposition",
             p="Strangler-fig extraction of the parts that actually need independence, with contract tests and a cutover sequence that keeps the old path available.",
             meta="8&ndash;14 weeks &middot; incremental &middot; reversible"),
        dict(tag="Advisory", h4="Performance and scale review",
             p="Profiling, load testing and query analysis against a target volume, with a ranked list of what to fix and what the fix is worth.",
             meta="2&ndash;4 weeks &middot; load-test suite retained")],
    dels=[
        dict(h4="Working system", p="Deployed, monitored, documented, with the infrastructure defined as code alongside the application."),
        dict(h4="Test suite", p="Unit, integration and contract tests running in CI, at a level of coverage your team can maintain rather than abandon."),
        dict(h4="Architecture decision records", p="Why the boundaries are where they are, what was rejected, and the conditions that should trigger a rethink."),
        dict(h4="Load-test baseline", p="Reproducible k6 or JMeter scenarios plus measured headroom at your projected volume.")],
    faqs=[
        ("Microservices or monolith?",
         "Start with a well-structured monolith and clear internal boundaries unless you have multiple teams needing independent deploys today, or a component with a genuinely different scaling profile. Splitting later is straightforward when the boundaries were drawn properly. Merging back after a premature split is not."),
        ("Can you take over a codebase from another team?",
         "Yes, and we will be direct about its condition. The first two weeks are assessment: what works, what is load-bearing, what is undocumented, and what should be replaced rather than repaired. You get that written down before we commit to a delivery scope."),
        ("Will our team be able to maintain what you build?",
         "That is the design constraint. We work in mainstream stacks, in your repository, to your review standards, and we avoid clever solutions where an obvious one will do. Every engagement ends with a walkthrough and written architecture records aimed at the engineers who will own it next.")],
))

# ------------------------------------------------------------------ Mobile
P.append(dict(
    id="mobile",
    live_h="Offline-first, because the network is not a given.",
    live_p="The hard part is what happens when a request fails mid-flight and the user backgrounds the app. Deterministic sync, written conflict rules, a build pipeline anyone can run.",
    slug="mobile", cat="Mobile", short="Mobile", label="Mobile Development",
    h1="Cross-platform or native &mdash; decided <em>per project, not by habit</em>.",
    lede="We will tell you when native is worth the cost, and when it is a waste of budget.",
    facts=[("Typical first engagement", "8&ndash;14 weeks, fixed scope"),
           ("Starts with", "Platform decision, written with the trade-offs"),
           ("Ends with", "Store-released build, CI pipeline and release runbook")],
    intro=[
        "Mobile projects rarely fail on rendering. They fail on offline behaviour, sync conflicts, push reliability and a release process nobody documented.",
        "So the platform question gets answered quickly, then attention goes where the risk is: state and sync, release engineering, and the operational tail after launch."],
    bullets=[
        "One written platform recommendation with the cost of each option",
        "Offline-first data and conflict resolution designed rather than discovered",
        "Automated builds and signing, so releases are not one person's private ritual",
        "Crash and performance monitoring wired up before the first store submission"],
    stack=[
        ("Cross-platform", "React Native, Flutter, Kotlin Multiplatform (KMP), Expo tooling"),
        ("iOS", "Swift, SwiftUI, Xcode, App Store review and release process"),
        ("Android", "Kotlin, Jetpack Compose, Java, Android Studio, Play Console release process"),
        ("State &amp; data", "Offline-first sync and conflict resolution, local persistence (Room, Core Data, SQLDelight), background upload that survives process death"),
        ("Delivery", "Push architecture, deep linking, feature flags, staged rollout, CI for mobile builds and signing"),
        ("Quality", "Crash-free session monitoring, startup and frame-time profiling, automated UI testing")],
    examples=[
        dict(tag="Fixed scope", h4="Consumer app build",
             p="From platform decision to store release: architecture, interface, API integration, analytics, crash reporting and a documented release pipeline.",
             meta="10&ndash;14 weeks &middot; iOS + Android"),
        dict(tag="Fixed scope", h4="Field / offline app",
             p="Applications that must work with no connectivity: local-first data, deterministic sync, conflict resolution and background upload that survives being killed.",
             meta="8&ndash;12 weeks &middot; offline-first"),
        dict(tag="Advisory", h4="Platform and codebase review",
             p="Assessment of an existing app: architecture, crash trends, release process, and whether a rewrite is genuinely cheaper than repair.",
             meta="2 weeks &middot; written recommendation")],
    dels=[
        dict(h4="Released build", p="Shipped through App Store and Play Console with the submission process documented for your team to repeat."),
        dict(h4="Build pipeline", p="Automated builds, signing and distribution to testers, so any engineer can cut a release."),
        dict(h4="Sync specification", p="The offline data model, conflict rules and retry behaviour written down, because this is where mobile bugs live."),
        dict(h4="Monitoring baseline", p="Crash-free session rate, startup time and key funnel instrumentation, with alert thresholds set.")],
    faqs=[
        ("React Native, Flutter or native?",
         "React Native when you have a React web team and want shared knowledge. Flutter when the interface is highly custom and you want identical rendering across platforms. Native when you depend on platform-specific hardware, need the last increment of performance, or you already have iOS and Android engineers. We write the recommendation down with the cost of each option, and we are happy to be argued with."),
        ("Do you handle store submission?",
         "Yes, including the parts nobody enjoys: review responses, privacy declarations, screenshots and staged rollout. We document the process so the second release does not need us."),
        ("Can you maintain an app someone else built?",
         "Usually. We start with a short review of architecture, dependency health and crash trends, then give you a maintenance plan or an honest case for rebuilding. We would rather tell you the codebase is worth keeping than sell a rewrite.")],
))

# ------------------------------------------------------------------ Commerce
P.append(dict(
    id="commerce", slug="commerce", cat="Commerce", short="Commerce", label="Commerce & Product Design",
    h1="Storefronts that convert, and design that arrives <em>build-ready</em>.",
    lede = "The interface that gets designed is the interface that gets shipped.",
    facts=[("Typical first engagement", "5&ndash;12 weeks, fixed scope"),
           ("Starts with", "Performance and conversion baseline"),
           ("Ends with", "Live storefront, design tokens and editor documentation")],
    intro=[
        "Design handed over as flat mockups gets rebuilt by whoever is available, in whatever the theme already does. That gap is where conversion goes to die.",
        "We keep design and engineering in one engagement: components specified with states and tokens, a performance budget agreed before the first screen, a conversion baseline taken at the start."],
    bullets=[
        "Design delivered as coded components and tokens, not static files",
        "Core Web Vitals treated as a launch requirement, not post-launch cleanup",
        "Checkout and funnel instrumentation in place before the redesign ships",
        "Content editable by your merchandising team without a developer"],
    stack=[
        ("Shopify", "Custom storefronts, theme development, headless builds (Hydrogen and custom front ends), platform migrations, app and API integration"),
        ("UI/UX design", "Product design delivered as build-ready components, design tokens, states and breakpoints; design-system documentation"),
        ("Front of funnel", "Performance budgets, Core Web Vitals, image and font strategy, checkout and conversion instrumentation"),
        ("Migration", "Catalogue, customer and order migration with reconciliation, plus redirect mapping to protect search rankings")],
    examples=[
        dict(tag="Fixed scope", h4="Custom Shopify storefront",
             p="Design and build on a defined scope, with a theme your merchandising team can operate and a measured performance budget at launch.",
             meta="6&ndash;10 weeks &middot; design + build"),
        dict(tag="Fixed scope", h4="Headless commerce build",
             p="Shopify as commerce engine with a custom front end where content, personalisation or performance demands justify the additional complexity.",
             meta="8&ndash;12 weeks &middot; headless"),
        dict(tag="Fixed scope", h4="Platform migration",
             p="Move to Shopify with catalogue, customer and order data reconciled, redirects mapped, and search visibility protected through cutover.",
             meta="5&ndash;9 weeks &middot; reconciled migration")],
    dels=[
        dict(h4="Design system", p="Components, states, tokens and breakpoints, documented and implemented in code &mdash; one source of truth for design and build."),
        dict(h4="Performance budget", p="Agreed Core Web Vitals targets, verified at launch, with the specific costs of any exception written down."),
        dict(h4="Editor documentation", p="How your team changes content, merchandising and page structure without a developer in the loop."),
        dict(h4="Conversion baseline", p="Funnel instrumentation and a before/after measurement, so the redesign can be judged on results rather than taste.")],
    faqs=[
        ("Headless or a Shopify theme?",
         "A well-built theme covers most stores and costs materially less to run and maintain. Headless earns its keep with complex content needs, multiple storefronts or personalisation that themes cannot express. We will price both and tell you which one we would choose with our own money."),
        ("Do you do design as well as build?",
         "Yes, and preferably together. Design arrives as build-ready components with tokens and states rather than flat mockups, which removes the interpretation gap that usually degrades a design between approval and launch."),
        ("Will a redesign hurt our search rankings?",
         "Not if migration is treated as an engineering task. Redirect mapping, structured data, URL preservation and Core Web Vitals are part of the scope, with a pre-launch crawl comparison so regressions are caught before cutover rather than in next month's traffic report.")],
))

BY_ID = {p["id"]: p for p in P}
