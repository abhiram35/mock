from app.database import SessionLocal
from app.models.topic import Topic
from app.models.question import Question
from app.enums.question_difficulty import QuestionDifficulty


TOPIC_NAME = "Software Engineering & Management"


QUESTIONS = [
    # =========================================================
    # EASY — 20 QUESTIONS
    # =========================================================

    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the SDLC, and what are its phases?"
        ),
        "expected_answer": (
            "The SDLC (Software Development Life Cycle) is a "
            "structured process for planning, creating, testing, and "
            "deploying software. Common phases are requirements "
            "gathering, system design, implementation (coding), "
            "testing, deployment, and maintenance. The exact phases "
            "and their order vary by methodology."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "Agile vs Waterfall -- key differences?"
        ),
        "expected_answer": (
            "Waterfall is a sequential process where each phase "
            "(requirements, design, implementation, testing, "
            "deployment) completes before the next begins, making it "
            "rigid but predictable. Agile is iterative and "
            "incremental, delivering working software in short cycles "
            "(sprints), welcoming changing requirements, and "
            "emphasizing collaboration and continuous feedback."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a sprint in Scrum?"
        ),
        "expected_answer": (
            "A sprint is a fixed-length iteration (typically one to "
            "four weeks) during which the Scrum team commits to "
            "completing a set of backlog items and delivering a "
            "potentially shippable increment. Each sprint includes "
            "planning, daily stand-ups, development, review, and "
            "retrospective."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is version control, and why is it used?"
        ),
        "expected_answer": (
            "Version control is a system that records changes to files "
            "over time so that specific versions can be recalled later. "
            "It enables collaboration, tracks history, supports "
            "branching and merging, and allows reverting to previous "
            "states. Git is the most widely used version control system."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "Verification vs validation?"
        ),
        "expected_answer": (
            "Verification checks whether the product is being built "
            "correctly according to specifications (\"Are we building "
            "the product right?\"). Validation checks whether the "
            "product meets the user's actual needs and expectations "
            "(\"Are we building the right product?\"). Verification is "
            "process-focused; validation is product-focused."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a user story vs a use case?"
        ),
        "expected_answer": (
            "A user story is a short, informal description of a "
            "feature from the end user's perspective, typically "
            "following the format \"As a [role], I want [goal] so "
            "that [benefit].\" A use case is a more detailed, "
            "structured document describing the interactions between "
            "an actor and the system to achieve a goal, including "
            "main flows, alternate flows, and error handling."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What roles exist in a Scrum team?"
        ),
        "expected_answer": (
            "A Scrum team has three roles. The Product Owner manages "
            "the product backlog and prioritizes work based on "
            "business value. The Scrum Master facilitates the Scrum "
            "process, removes impediments, and coaches the team. The "
            "Development Team is a cross-functional group that does "
            "the actual work of delivering the increment."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a backlog in Agile?"
        ),
        "expected_answer": (
            "A backlog is a prioritized list of work items (user "
            "stories, bugs, tasks) that need to be completed. The "
            "product backlog contains all desired features for the "
            "product and is maintained by the Product Owner. The "
            "sprint backlog is the subset of items selected for the "
            "current sprint."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the difference between a bug and a defect?"
        ),
        "expected_answer": (
            "In practice, the terms are often used interchangeably. "
            "Strictly, a defect is a flaw introduced during "
            "development (incorrect code, design error) that may or "
            "may not have been discovered yet. A bug is a defect that "
            "has been found and reported, typically during testing or "
            "by users in production."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a stand-up meeting used for?"
        ),
        "expected_answer": (
            "A daily stand-up (or daily Scrum) is a short, time-boxed "
            "meeting (usually 15 minutes) where each team member "
            "shares what they did yesterday, what they plan to do "
            "today, and any blockers they face. Its purpose is to "
            "synchronize the team and surface impediments early."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the difference between white-box and "
            "black-box testing?"
        ),
        "expected_answer": (
            "White-box testing examines the internal structure and "
            "logic of the code (e.g. testing branches, paths, and "
            "conditions). Black-box testing focuses on inputs and "
            "expected outputs without knowledge of the internal "
            "implementation. White-box is typically done by developers; "
            "black-box is often done by QA or testers."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a use case diagram?"
        ),
        "expected_answer": (
            "A use case diagram is a UML diagram that shows the "
            "interactions between external actors and the system. It "
            "visually represents the system's functional requirements "
            "by depicting actors (stick figures), use cases (ovals), "
            "and the relationships between them. It helps stakeholders "
            "understand what the system does at a high level."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is regression testing?"
        ),
        "expected_answer": (
            "Regression testing is the practice of re-running existing "
            "tests after code changes to verify that previously working "
            "functionality has not been broken. It is typically "
            "automated and run as part of a CI pipeline to catch "
            "unintended side effects of new code."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the difference between functional and "
            "non-functional requirements?"
        ),
        "expected_answer": (
            "Functional requirements describe what the system should "
            "do, such as specific features, behaviors, and business "
            "rules. Non-functional requirements describe how the "
            "system should perform, covering qualities like "
            "performance, scalability, security, usability, and "
            "reliability."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a Gantt chart used for?"
        ),
        "expected_answer": (
            "A Gantt chart is a horizontal bar chart that visualizes "
            "a project schedule. Each bar represents a task, showing "
            "its start date, end date, and duration. Dependencies "
            "between tasks can also be shown. Gantt charts help "
            "project managers plan, coordinate, and track progress."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the difference between a project manager "
            "and a Scrum Master?"
        ),
        "expected_answer": (
            "A project manager is responsible for planning, executing, "
            "and closing a project, managing scope, budget, timeline, "
            "and resources. A Scrum Master is a servant-leader who "
            "facilitates the Scrum process, removes impediments, and "
            "coaches the team but does not manage scope or timelines "
            "directly. The Scrum Master focuses on team effectiveness "
            "rather than project delivery."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is pair programming?"
        ),
        "expected_answer": (
            "Pair programming is a practice where two developers work "
            "together at one workstation. The driver writes code while "
            "the navigator reviews each line, thinks ahead, and "
            "suggests improvements. Roles are switched regularly. It "
            "improves code quality, spreads knowledge, and catches "
            "bugs early."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a retrospective meeting?"
        ),
        "expected_answer": (
            "A retrospective is a meeting held at the end of a sprint "
            "where the team reflects on what went well, what did not "
            "go well, and what can be improved in the next sprint. "
            "The goal is continuous process improvement. Action items "
            "are identified and tracked."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the difference between QA and QC?"
        ),
        "expected_answer": (
            "QA (Quality Assurance) is process-oriented and focuses "
            "on preventing defects by improving the development "
            "process itself. QC (Quality Control) is product-oriented "
            "and focuses on identifying defects in the finished "
            "product through testing and inspection. QA is proactive; "
            "QC is reactive."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a minimum viable product (MVP)?"
        ),
        "expected_answer": (
            "An MVP is the simplest version of a product that delivers "
            "enough value to early users and provides feedback for "
            "future development. It includes only the core features "
            "necessary to test a hypothesis or validate a market need, "
            "minimizing development effort while maximizing learning."
        ),
    },

    # =========================================================
    # MEDIUM — 20 QUESTIONS
    # =========================================================

    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Unit vs integration vs system testing -- differences?"
        ),
        "expected_answer": (
            "Unit testing verifies individual components (functions, "
            "classes) in isolation, usually with mocked dependencies. "
            "Integration testing verifies that multiple components "
            "work together correctly (e.g. service-to-database). "
            "System testing verifies the entire application as a "
            "whole against the requirements. Each level catches "
            "different categories of defects and has different cost "
            "and speed trade-offs."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is technical debt, and how do you manage it?"
        ),
        "expected_answer": (
            "Technical debt is the implied cost of future rework "
            "caused by choosing a quick or suboptimal solution now "
            "instead of a better approach that would take longer. "
            "It is managed by tracking it visibly (e.g. in the "
            "backlog), allocating a percentage of each sprint to "
            "paying it down, prioritizing debt that slows development "
            "the most, and establishing coding standards and reviews "
            "to prevent unnecessary accumulation."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain CI/CD and why it matters."
        ),
        "expected_answer": (
            "CI (Continuous Integration) automatically builds and "
            "tests code every time a developer pushes changes, "
            "catching integration issues early. CD (Continuous "
            "Delivery) extends CI by automatically preparing releases "
            "for deployment; Continuous Deployment goes further by "
            "automatically deploying to production. CI/CD reduces "
            "manual effort, shortens feedback loops, and increases "
            "release frequency and reliability."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Kanban vs Scrum board -- differences?"
        ),
        "expected_answer": (
            "A Scrum board is reset at the start of each sprint and "
            "displays only the items committed to that sprint, with "
            "work organized in time-boxed iterations. A Kanban board "
            "is continuous, with no fixed iterations; work items flow "
            "through columns with WIP (Work In Progress) limits that "
            "control how many items can be in each stage at once. "
            "Kanban emphasizes flow and cycle time; Scrum emphasizes "
            "cadence and commitment."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "How do you estimate effort with story points "
            "vs man-hours?"
        ),
        "expected_answer": (
            "Story points measure relative complexity and effort of a "
            "user story compared to other stories, abstracting away "
            "individual speed differences. Man-hours estimate absolute "
            "time a specific person needs. Story points are preferred "
            "in Agile because they focus on the team's velocity over "
            "time and are less susceptible to individual variation, "
            "while man-hours can create pressure and false precision."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is a risk register, and how is risk managed "
            "in a project?"
        ),
        "expected_answer": (
            "A risk register is a document that lists identified "
            "risks, their likelihood, potential impact, mitigation "
            "strategies, and owners. Risk management involves "
            "identifying risks early, assessing their probability and "
            "impact, planning mitigation or contingency actions, and "
            "continuously monitoring and updating the register "
            "throughout the project lifecycle."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain the SOLID principles with examples."
        ),
        "expected_answer": (
            "SOLID is an acronym for five design principles. Single "
            "Responsibility: a class should have one reason to change. "
            "Open/Closed: classes should be open for extension but "
            "closed for modification. Liskov Substitution: subtypes "
            "must be substitutable for their base types. Interface "
            "Segregation: clients should not depend on interfaces they "
            "do not use. Dependency Inversion: high-level modules "
            "should depend on abstractions, not concrete "
            "implementations."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is the difference between code review "
            "and pair programming?"
        ),
        "expected_answer": (
            "Code review is an asynchronous process where a developer "
            "submits code for another developer to review after it is "
            "written, typically via a pull request. Pair programming "
            "is synchronous: two developers collaborate in real time, "
            "with one writing code and the other reviewing "
            "continuously. Pair programming catches issues earlier but "
            "requires scheduling alignment; code review is more "
            "flexible but has a longer feedback loop."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain how you'd handle a missed sprint commitment."
        ),
        "expected_answer": (
            "First, identify the root cause (scope creep, inaccurate "
            "estimation, unexpected blockers, or team availability). "
            "Discuss it transparently in the sprint review and "
            "retrospective. Move incomplete items back to the backlog "
            "and re-prioritize them for the next sprint. Adjust "
            "estimation practices or team capacity planning based on "
            "the lessons learned. Do not simply extend the sprint "
            "or pressure the team to cut quality."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is the difference between a monolith and "
            "microservices from a delivery standpoint?"
        ),
        "expected_answer": (
            "A monolith is a single deployable unit; changes require "
            "building and deploying the entire application, which "
            "simplifies initial development but slows down large "
            "teams. Microservices split the application into "
            "independently deployable services, allowing teams to "
            "release, scale, and update their service without "
            "coordinating a full release. The trade-off is increased "
            "operational complexity (networking, monitoring, "
            "distributed debugging)."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain the concept of Definition of Done (DoD) "
            "in Scrum."
        ),
        "expected_answer": (
            "The Definition of Done is a shared checklist of criteria "
            "that a product backlog item must satisfy to be considered "
            "complete. It typically includes code written, tests "
            "passing, code reviewed, documentation updated, and "
            "deployed to a staging environment. DoD ensures consistent "
            "quality and provides transparency about what done means "
            "to the whole team."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is a design pattern? Name a few commonly used ones."
        ),
        "expected_answer": (
            "A design pattern is a reusable, general solution to a "
            "commonly occurring problem in software design. Common "
            "examples include Singleton (single instance), Factory "
            "(object creation without specifying the class), Observer "
            "(publish-subscribe for state changes), Strategy "
            "(interchangeable algorithms), and Adapter (interface "
            "compatibility between incompatible classes)."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "How do you prioritize a backlog with competing "
            "stakeholder demands?"
        ),
        "expected_answer": (
            "Use a prioritization framework such as MoSCoW (Must, "
            "Should, Could, Won't), WSJF (Weighted Shortest Job "
            "First), or RICE (Reach, Impact, Confidence, Effort) to "
            "make trade-offs explicit and data-driven. Involve "
            "stakeholders in prioritization sessions so they "
            "understand constraints. Focus on business value, user "
            "impact, and dependencies. The Product Owner makes the "
            "final call, backed by transparent criteria."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain feature flags and their use in "
            "incremental rollout."
        ),
        "expected_answer": (
            "Feature flags are conditional toggles in code that enable "
            "or disable features at runtime without redeploying. They "
            "support incremental rollout by enabling a feature for a "
            "small percentage of users first (canary or percentage "
            "rollout), monitoring for issues, and gradually increasing "
            "exposure. They also allow instant rollback by turning off "
            "the flag. Flags should be cleaned up after the feature is "
            "fully launched to avoid technical debt."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is the bus factor, and why does it matter "
            "for a team?"
        ),
        "expected_answer": (
            "The bus factor is the minimum number of team members who "
            "would need to leave (\"hit by a bus\") before the project "
            "stalls due to lack of knowledge. A bus factor of one "
            "means a single person's departure could cripple the "
            "project. Teams increase it through knowledge sharing, "
            "pair programming, thorough documentation, code reviews, "
            "and cross-training."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain how code reviews improve software quality "
            "and knowledge sharing."
        ),
        "expected_answer": (
            "Code reviews catch bugs, logic errors, and style "
            "inconsistencies before code is merged. They enforce "
            "coding standards, encourage better design, and expose "
            "more team members to different parts of the codebase, "
            "spreading domain knowledge. Reviews also provide "
            "mentorship opportunities for junior developers and reduce "
            "the bus factor by ensuring multiple people understand "
            "each change."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is the difference between vertical and "
            "horizontal scaling from a planning perspective?"
        ),
        "expected_answer": (
            "Vertical scaling (scale up) adds more resources (CPU, "
            "RAM) to a single machine; it is simpler but has a "
            "hardware ceiling and introduces a single point of "
            "failure. Horizontal scaling (scale out) adds more "
            "machines to distribute the load; it offers near-unlimited "
            "scalability but requires stateless or shared-state "
            "architectures and more complex infrastructure. Planning "
            "for horizontal scaling should start early because "
            "retrofitting it is expensive."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain the concept of a \"spike\" in Agile."
        ),
        "expected_answer": (
            "A spike is a time-boxed research task used to gain "
            "knowledge needed to reduce uncertainty before committing "
            "to a user story. It is used when the team does not have "
            "enough information to estimate or implement a feature. "
            "The output of a spike is knowledge (e.g. a prototype, "
            "a recommendation, or refined estimates), not production "
            "code."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "How would you onboard a new developer efficiently "
            "onto a legacy codebase?"
        ),
        "expected_answer": (
            "Provide a curated onboarding guide with architecture "
            "diagrams, key entry points, and how to set up the "
            "development environment. Assign a mentor or buddy for "
            "the first few weeks. Start with small, well-defined tasks "
            "that touch different parts of the codebase. Use pair "
            "programming sessions to transfer tacit knowledge. "
            "Encourage the new developer to improve documentation as "
            "they learn, which also benefits future hires."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What metrics would you track to measure a "
            "Scrum team's health?"
        ),
        "expected_answer": (
            "Useful metrics include velocity (story points completed "
            "per sprint) for planning, sprint burndown for tracking "
            "within a sprint, cycle time for flow efficiency, defect "
            "escape rate for quality, and team happiness or "
            "satisfaction surveys for morale. Metrics should be used "
            "for the team's own improvement, not for comparing teams "
            "or individual performance."
        ),
    },

    # =========================================================
    # HARD — 20 QUESTIONS
    # =========================================================

    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How would you manage scope creep with a fixed "
            "deadline and shifting requirements?"
        ),
        "expected_answer": (
            "Establish a clear change control process: every new "
            "request is evaluated for impact on scope, timeline, and "
            "resources before acceptance. Use MoSCoW or similar "
            "prioritization to explicitly trade lower-priority items "
            "for new ones, keeping the total scope constant. "
            "Communicate trade-offs transparently to stakeholders. "
            "Maintain a frozen core scope and buffer for negotiable "
            "items. Time-boxing iterations helps surface scope "
            "pressure early rather than discovering it at the deadline."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Design a rollback/release strategy for a large "
            "production deployment (blue-green, canary)."
        ),
        "expected_answer": (
            "Blue-green deployment maintains two identical production "
            "environments; traffic is switched from the current (blue) "
            "to the new (green) after validation, and rolled back by "
            "switching the router back. Canary deployment routes a "
            "small percentage of traffic to the new version while "
            "monitoring error rates, latency, and business metrics. "
            "If anomalies are detected, traffic is shifted back "
            "immediately. Both strategies require automated health "
            "checks, database backward compatibility, and feature "
            "flags to decouple code deployment from feature activation."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How would you lead a team through a project "
            "that's behind schedule?"
        ),
        "expected_answer": (
            "First, assess the root cause honestly: is it scope, "
            "staffing, technical debt, or external dependencies? "
            "Re-prioritize ruthlessly, cutting non-essential scope to "
            "protect the core deliverable. Communicate the situation "
            "and revised plan to stakeholders early. Remove blockers "
            "for the team and shield them from distractions. Avoid "
            "adding people late (Brooks's Law) or forcing overtime, "
            "which reduces long-term productivity. Consider breaking "
            "the remaining work into smaller increments to deliver "
            "partial value earlier."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Compare microservices vs monolith from a "
            "team-scaling perspective (Conway's Law)."
        ),
        "expected_answer": (
            "Conway's Law states that system architecture mirrors "
            "organizational communication structure. A monolith works "
            "well for a small, co-located team but becomes a "
            "coordination bottleneck as the team grows. Microservices "
            "allow independent teams to own and deploy their services "
            "autonomously, scaling the organization by reducing "
            "cross-team dependencies. However, microservices require "
            "strong API contracts, shared infrastructure (CI/CD, "
            "observability), and architectural governance to prevent "
            "fragmentation."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How would you set up DORA metrics to improve "
            "delivery performance?"
        ),
        "expected_answer": (
            "DORA (DevOps Research and Assessment) defines four key "
            "metrics: Deployment Frequency, Lead Time for Changes, "
            "Change Failure Rate, and Mean Time to Restore (MTTR). "
            "Instrument the CI/CD pipeline and incident management "
            "system to capture these automatically. Set baselines, "
            "share dashboards with the team, and run retrospectives "
            "focused on improving specific metrics. Target elite "
            "performance: multiple deploys per day, lead time under "
            "one hour, change failure rate under 15 percent, and "
            "MTTR under one hour."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Describe a framework for a build-vs-buy decision "
            "on a critical component."
        ),
        "expected_answer": (
            "Evaluate along several axes: is the component a core "
            "differentiator (build) or commodity (buy)? Compare total "
            "cost of ownership including development, maintenance, "
            "licensing, and vendor lock-in. Assess the vendor's "
            "roadmap alignment, support quality, and integration "
            "effort. Consider time-to-market: buying accelerates "
            "delivery but may limit customization. Run a time-boxed "
            "proof of concept for the buy option. Document the "
            "decision rationale in an ADR (Architecture Decision "
            "Record) for future reference."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How would you design an incident-response and "
            "postmortem process for production outages?"
        ),
        "expected_answer": (
            "Define severity levels (SEV1-SEV4) with clear escalation "
            "paths and on-call rotations. When an incident is declared, "
            "assign an Incident Commander to coordinate, a "
            "Communications Lead for status updates, and engineers to "
            "diagnose and mitigate. Communicate via a dedicated channel "
            "and update a status page. After resolution, conduct a "
            "blameless postmortem: document the timeline, root cause, "
            "contributing factors, and action items with owners and "
            "deadlines. Track action item completion to prevent "
            "recurrence."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How do you balance innovation (new features) against "
            "reliability (SRE error budgets)?"
        ),
        "expected_answer": (
            "Define SLOs (Service Level Objectives) for reliability "
            "and derive an error budget (the allowed amount of "
            "unreliability). While the error budget is not exhausted, "
            "teams can ship features aggressively. When the error "
            "budget is spent, the team shifts focus to reliability "
            "improvements until the budget replenishes. This creates "
            "a data-driven, non-political negotiation between product "
            "velocity and system stability, aligning incentives across "
            "development and operations."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain how you'd migrate a legacy monolith to "
            "microservices incrementally (strangler fig pattern)."
        ),
        "expected_answer": (
            "The strangler fig pattern gradually replaces the monolith "
            "by building new functionality as microservices and "
            "routing traffic to them via a facade (API gateway). Over "
            "time, existing monolith features are extracted into "
            "services one by one. Each extraction involves identifying "
            "a bounded context, defining API contracts, migrating data "
            "access, setting up the new service, and rerouting traffic. "
            "The monolith shrinks until it can be decommissioned. This "
            "avoids the risk of a big-bang rewrite."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How would you structure teams for a multi-region "
            "product launch across time zones?"
        ),
        "expected_answer": (
            "Organize teams around features or services rather than "
            "functions (cross-functional teams). Establish overlapping "
            "working hours for synchronous collaboration and use async "
            "communication tools for everything else. Designate a "
            "launch coordinator in each region with clear escalation "
            "paths. Create a shared launch checklist and runbook with "
            "go/no-go criteria. Rehearse the launch with a dry run. "
            "Use a follow-the-sun on-call rotation so there is always "
            "someone awake to handle issues during and after launch."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Describe how you'd measure and reduce cycle time "
            "in a slow-moving engineering org."
        ),
        "expected_answer": (
            "Cycle time is the elapsed time from work starting to "
            "work being deployed. Measure it by instrumenting the "
            "workflow from first commit to production deployment. "
            "Identify bottlenecks (long code review queues, manual "
            "QA, slow CI, deployment approvals) using a value stream "
            "map. Attack the largest bottleneck first: automate "
            "testing, parallelize CI, reduce batch sizes, introduce "
            "trunk-based development, and eliminate unnecessary "
            "approval gates. Track improvement over sprints and "
            "celebrate wins to build momentum."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How would you handle a critical security "
            "vulnerability discovered in production?"
        ),
        "expected_answer": (
            "Immediately assess the severity and blast radius. If "
            "actively exploited, apply a hotfix or mitigating control "
            "(WAF rule, feature flag, network block) as fast as "
            "possible. Notify the security team, management, and "
            "potentially affected users as required by policy or "
            "regulation. Develop, test, and deploy a permanent fix "
            "through an expedited but reviewed process. Conduct a "
            "postmortem to understand how the vulnerability was "
            "introduced and improve defenses (SAST, dependency "
            "scanning, penetration testing) to prevent similar issues."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain how you'd design a performance "
            "review/promotion framework for engineers."
        ),
        "expected_answer": (
            "Define a clear engineering ladder with levels, each "
            "having explicit expectations across dimensions like "
            "technical skill, scope of impact, leadership, and "
            "communication. Use a calibration process where managers "
            "compare assessments across the organization to ensure "
            "consistency. Include self-review, peer feedback, and "
            "manager assessment. Separate performance evaluation "
            "from compensation discussions to reduce anxiety. Provide "
            "regular (at least quarterly) feedback, not just annual "
            "reviews, so promotions are never a surprise."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How would you decide between a big-bang rewrite "
            "and incremental refactor of legacy software?"
        ),
        "expected_answer": (
            "A big-bang rewrite is attractive but risky: it freezes "
            "new features, takes longer than expected, and often "
            "re-introduces solved edge cases. It is justified only "
            "when the codebase is so far gone that modification cost "
            "exceeds rewrite cost and the domain is well understood. "
            "Incremental refactoring (strangler fig, branch by "
            "abstraction) delivers value continuously and reduces "
            "risk. Evaluate based on team capacity, business urgency, "
            "test coverage of the legacy code, and stakeholder "
            "appetite for a feature freeze."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Describe your approach to managing a "
            "distributed/remote engineering team across "
            "cultures and time zones."
        ),
        "expected_answer": (
            "Establish asynchronous communication as the default "
            "(written design docs, recorded demos, detailed PR "
            "descriptions). Minimize required synchronous meetings "
            "and rotate meeting times to share the burden across time "
            "zones. Document decisions and context in shared tools "
            "(wiki, ADRs) rather than relying on hallway conversations. "
            "Be intentional about inclusion: ensure all team members "
            "have equal access to information and career opportunities. "
            "Build social connection through virtual social events "
            "and periodic in-person gatherings."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How would you drive alignment between product, "
            "design, and engineering when priorities conflict?"
        ),
        "expected_answer": (
            "Start by establishing shared goals and OKRs that all "
            "three functions contribute to. Use a regular planning "
            "cadence (e.g. quarterly planning) where trade-offs are "
            "surfaced and debated openly. Create lightweight RFCs or "
            "one-pagers for significant decisions that require "
            "cross-functional input. When priorities conflict, "
            "escalate with data: user impact, engineering cost, and "
            "business metrics. The product manager typically owns the "
            "what and why; engineering owns the how and when; design "
            "owns the user experience."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain how you'd design an SLA/SLO framework "
            "for a customer-facing API."
        ),
        "expected_answer": (
            "Define SLIs (Service Level Indicators) such as latency, "
            "availability, and error rate. Set SLOs (Service Level "
            "Objectives) as internal targets for each SLI (e.g. 99.9 "
            "percent availability, p99 latency under 200ms). Derive "
            "an error budget from the SLO gap (e.g. 0.1 percent "
            "downtime per month). SLAs are the external contractual "
            "commitments with consequences for breach, set more "
            "conservatively than SLOs. Instrument monitoring and "
            "alerting on SLIs, and use error budgets to govern the "
            "pace of feature releases versus reliability work."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How would you handle a vendor/third-party dependency "
            "that repeatedly causes outages?"
        ),
        "expected_answer": (
            "Short term: implement circuit breakers, fallback "
            "mechanisms, and caching to isolate the dependency's "
            "failures from your system. Set aggressive timeouts and "
            "retries with backoff. Medium term: escalate with the "
            "vendor, demanding root-cause analyses and SLA "
            "commitments. Track the vendor's incident history and "
            "business impact quantitatively. Long term: evaluate "
            "alternative vendors or building the capability in-house "
            "if the vendor cannot meet reliability requirements. "
            "Ensure contractual protections (SLAs, exit clauses) "
            "are in place."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Describe how you'd introduce Agile practices into "
            "a traditionally Waterfall organization."
        ),
        "expected_answer": (
            "Start with a pilot team willing to experiment, rather "
            "than a top-down mandate. Introduce Scrum or Kanban with "
            "coaching and training. Demonstrate early wins (faster "
            "delivery, higher quality) to build organizational "
            "support. Gradually expand to other teams while adapting "
            "practices to the organization's culture. Address "
            "structural barriers (approval gates, annual budgeting, "
            "siloed teams) that conflict with Agile principles. "
            "Leadership sponsorship and patience are critical because "
            "culture change takes time."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How would you evaluate and mitigate the risk of "
            "key-person dependency (bus factor) at an "
            "organizational level?"
        ),
        "expected_answer": (
            "Map critical knowledge areas to individuals and identify "
            "single points of failure. For each, create a mitigation "
            "plan: pair the key person with a backup through pair "
            "programming or shadowing, document critical processes and "
            "architecture decisions, record video walkthroughs of "
            "complex systems, and rotate on-call and ownership "
            "periodically. At the organizational level, build a "
            "culture that values documentation and knowledge sharing "
            "as first-class responsibilities, not afterthoughts. "
            "Track bus factor as a team health metric in retrospectives."
        ),
    },
]


def seed_swe_questions() -> None:
    db = SessionLocal()

    try:
        topic = (
            db.query(Topic)
            .filter(Topic.name == TOPIC_NAME)
            .first()
        )

        if not topic:
            topic = Topic(
                name=TOPIC_NAME,
                description=(
                    "Software Engineering and Management "
                    "interview questions covering fundamentals, "
                    "intermediate concepts, and advanced topics."
                ),
                is_active=True,
            )

            db.add(topic)
            db.commit()
            db.refresh(topic)

            print(
                f"Created topic: {topic.name} "
                f"(ID: {topic.id})"
            )

        else:
            print(
                f"Using existing topic: {topic.name} "
                f"(ID: {topic.id})"
            )

        existing_count = (
            db.query(Question)
            .filter(Question.topic_id == topic.id)
            .count()
        )

        if existing_count >= len(QUESTIONS):
            print(
                f"Software Engineering & Management topic "
                f"already contains {existing_count} question(s)."
            )
            print(
                "No questions were inserted to avoid duplicates."
            )
            return

        questions = [
            Question(
                topic_id=topic.id,
                difficulty=item["difficulty"],
                question_text=item["question_text"],
                expected_answer=item["expected_answer"],
            )
            for item in QUESTIONS
        ]

        db.add_all(questions)
        db.commit()

        print()
        print("=" * 60)
        print(
            "SOFTWARE ENGINEERING & MANAGEMENT "
            "INTERVIEW QUESTION BANK CREATED"
        )
        print("=" * 60)
        print(f"Topic ID       : {topic.id}")
        print(f"Topic          : {topic.name}")
        print(f"Total questions: {len(questions)}")
        print(
            "Easy           : "
            f"{sum(1 for q in questions if q.difficulty == QuestionDifficulty.EASY)}"
        )
        print(
            "Medium         : "
            f"{sum(1 for q in questions if q.difficulty == QuestionDifficulty.MEDIUM)}"
        )
        print(
            "Hard           : "
            f"{sum(1 for q in questions if q.difficulty == QuestionDifficulty.HARD)}"
        )
        print("=" * 60)

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_swe_questions()
