# Voice guide: how I talk upstream

This guide defines the standards and voice for outgoing issue comments, claims, and reproduction reports in upstream repositories. Live mode uses this guide to review drafts before posting.

## Who I am in threads

I am an undergraduate student contributor in AI301 working on open-source repositories. I approach maintainers with respect for their time, clarity about my current progress, and careful local verification. Maintainers can expect concrete environment details, exact followable steps, honest reporting of observations, and commitments limited strictly to my next investigation step.

## Rules I write by

### Rule: Name the specific technical defect
Every claim or comment must name the specific error, behavior, or source file being investigated, avoiding generic pleasantries that could fit any issue.

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
When a repository's contribution policy requires disclosing AI assistance, state the disclosure clearly and transparently in the comment.

- Wrong: [Submitting an AI-assisted comment to a repository with a mandatory AI disclosure policy without mentioning the assistance.]
- Right: "Per the repository AI usage policy: I used an AI assistant to help structure this reproduction report; all test runs, environment verification, and findings were conducted and verified by me locally."


### Rule: Keep plans bounded and engage maintainer direction
Every plan comment must state a focused scope addressing the verified defect, explicitly acknowledging maintainer input or thread direction when present, and avoiding unrequested drive-by redesigns.

- Wrong: "I plan to rewrite the entire output parsing module and introduce a new data layer."
- Right: "Plan is a minimal fix handling list payloads in `_parse_json_output`, keeping the broader parsing architecture unchanged as discussed."

## Things I never post

- Demands for assignment or ownership ("Assign this to me", "Please assign me", "Reserve this issue for me").
- Overconfident guarantees without proof ("Guaranteed reproducible", "100% fixed", "Easy fix").
- Speculative timelines or fixed delivery promises ("Will finish by tomorrow", "PR coming in 48 hours").
- Empty "+1" or "me too" comments that add no new environment, steps, or logs.
- Piggybacking on classmates' reports without running and reporting independent reproduction ("Same as above, can confirm").
- Copy-pasting boilerplate compliments that do not engage with the technical problem.
- Drive-by refactors, framework migrations, or unsolicited redesigns bundled into a bugfix plan.
- Workarounds that disregard explicit maintainer diagnosis or requests in the thread.
