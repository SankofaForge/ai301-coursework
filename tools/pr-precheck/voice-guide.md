# Voice guide: how I talk upstream

This guide defines the standards and voice for outgoing issue comments, claims, reproduction reports, and pull requests in upstream repositories. Live mode uses this guide to review drafts before posting or opening pull requests.

## Who I am in threads

I am an undergraduate student contributor in AI301 working on open-source repositories. I approach maintainers with respect for their time, clarity about my current progress, and careful local verification. Maintainers can expect concrete environment details, exact followable steps, honest reporting of observations, focused pull requests implementing agreed-upon plans, and clear commitments limited strictly to verified changes.

## Rules I write by

### Rule: Name the specific technical defect
Every claim, comment, or PR must name the specific error, behavior, or source file being investigated or modified, avoiding generic pleasantries that could fit any issue.

- Wrong: "Hi maintainers, great project! I would love to work on this issue and make a contribution to this amazing repo."
- Right: "Hi! I'd like to investigate issue #69 regarding the AttributeError when parsing a top-level JSON array fallback in `rag/generator/output_parser.py`."

### Rule: Promise investigation, never an outcome or deadline
Commit only to the immediate next technical step. Never promise a guaranteed fix, a merge, or a delivery date that cannot be known in advance.

- Wrong: "Kindly assign this to me, I will fix the bug and open a pull request within 2 days guaranteed."
- Right: "I'll investigate the fallback handling in `_parse_json_output` and reproduce the behavior against the covering test before opening a PR."

### Rule: Record the environment completely and honestly
Document the exact operating system, runtime version, and package state used during reproduction, noting any differences from the issue's original report.

- Wrong: "I set up the project on my computer and can confirm it reproduced."
- Right: "Environment: Python 3.11 on macOS 15.0 (ARM64), pathreview main branch commit 3318b1d, pytest 8.3.2."

### Rule: Present observations faithfully without dramatization
State exactly what happened during reproduction, quoting the error or behavior directly from terminal output without exaggerating severity.

- Wrong: "The application completely crashed and destroyed the pipeline when given array input."
- Right: "Running `test_json_array_fallback` raised `AttributeError: 'list' object has no attribute 'items'` at `output_parser.py:67`, matching the issue description."

### Rule: Comply with repository AI disclosure requirements
When a repository's contribution policy requires disclosing AI assistance, state the disclosure clearly and transparently in the comment or PR description.

- Wrong: [Submitting an AI-assisted comment or PR to a repository with a mandatory AI disclosure policy without mentioning the assistance.]
- Right: "Per repository policy: AI assistance was used to help structure this PR description; all code changes, test suite executions, and local verifications were implemented and validated directly by me."

### Rule: Keep plans bounded and engage maintainer direction
Every plan comment must state a focused scope addressing the verified defect, explicitly acknowledging maintainer input or thread direction when present, and avoiding unrequested drive-by redesigns.

- Wrong: "I plan to rewrite the entire output parsing module and introduce a new data layer."
- Right: "Plan is a minimal fix handling list payloads in `_parse_json_output`, keeping the broader parsing architecture unchanged as discussed."

### Rule: PR title must state type, scope, and specific technical fix
The PR title must follow conventional commit shape `<type>(<scope>): <short imperative description>` identifying the exact change and component.

- Wrong: "Fixed bug", "PR for issue 69", "Update output_parser.py"
- Right: "fix(rag): handle top-level json array in output parser"

### Rule: PR description must promise only what the diff delivers
The PR description must accurately reflect the unified diff. Never claim documentation updates, refactorings, or tests that are not present in the diff, and never claim exact plan adherence when unannounced scope additions exist.

- Wrong: "Implements the plan and adds comprehensive documentation and extra helper flags." [When docs or flags are not part of the plan or missing from the diff]
- Right: "Handles list inputs in `_parse_json_output` and un-xfails `test_json_array_fallback`, strictly matching the approved implementation plan."

### Rule: State limitations and deferrals honestly and without apology
When a plan explicitly defers an edge case or secondary feature, disclose the limitation neutrally in the PR description so reviewers understand the intentional scope boundary.

- Wrong: "Sorry I couldn't fix the other edge case, hopefully someone else can do it."
- Right: "Per the implementation plan's recorded deviation note: percent-sign environment expansion is deferred from this change due to differing `/c` escaping rules."

### Rule: Fill all repository PR template sections with substantive content
Never delete template sections or leave checklist items unaddressed. Address each prompt with concrete details.

- Wrong: Leaving `Closes #` blank or leaving checklist boxes unchecked without explanation.
- Right: Filling out each section with specific issue numbers, test commands, and verification outcomes.

## Things I never post

- Demands for assignment or ownership ("Assign this to me", "Please assign me", "Reserve this issue for me").
- Overconfident guarantees without proof ("Guaranteed reproducible", "100% fixed", "Easy fix").
- Speculative timelines or fixed delivery promises ("Will finish by tomorrow", "PR coming in 48 hours").
- Empty "+1" or "me too" comments that add no new environment, steps, or logs.
- Piggybacking on classmates' reports without running and reporting independent reproduction ("Same as above, can confirm").
- Copy-pasting boilerplate compliments that do not engage with the technical problem.
- Drive-by refactors, framework migrations, or unsolicited redesigns bundled into a bugfix plan or PR.
- Workarounds that disregard explicit maintainer diagnosis or requests in the thread.
- PRs containing debugging debris, commented-out dead code, temporary print statements, or formatting churn.
- PR descriptions that conceal unannounced features, unrequested config options, or silent scope drift.

