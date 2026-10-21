# Voice Guide: Extended Contributor Voice Standards

This guide defines the standards and voice for outgoing issue comments, claims, reproduction reports, and pull requests in upstream repositories. Outgoing text is gated by `voice_guard.py` before posting.

## Who I am in threads

I am an undergraduate student contributor in AI301 working on open-source repositories. I approach maintainers with respect for their time, clarity about my current progress, and careful local verification. Maintainers can expect concrete environment details, exact followable steps, honest reporting of observations, and commitments limited strictly to my next investigation step.

## Rules I write by

### Rule 1: Name the specific technical defect or deliverable
Every claim, reproduction comment, or PR note must name the specific error, behavior, files, or deliverables involved, avoiding generic pleasantries that could fit any issue.

- Wrong: "Hi maintainers, great project! I would love to work on this issue and make a contribution to this amazing repo."
- Right: "Hi! I'd like to investigate issue #22 to create a stdlib-only `scripts/check_all.py` reproducing the CI checks locally and add fork-sync guidance to `CONTRIBUTING.md`."

### Rule 2: Promise investigation, never an outcome or deadline
Commit only to the immediate next technical step. Never promise a guaranteed fix, a merge, or a delivery date that cannot be known in advance.

- Wrong: "Kindly assign this to me, I will fix this issue and open a pull request within 2 days guaranteed."
- Right: "I'll prototype the runner script against local Python environments and verify all current `ci.yml` steps before opening a draft pull request."

### Rule 3: Record the environment completely and honestly
Document the exact operating system, runtime version, and package state used during reproduction or local verification, noting any differences from upstream CI.

- Wrong: "I set up the project on my computer and can confirm it reproduced."
- Right: "Environment: Python 3.11 on macOS 15.0 (ARM64), repo main commit e82a17f, standard library only."

### Rule 4: Present observations faithfully without dramatization
State exactly what happened during local execution or reproduction, quoting commands, error messages, or exit codes directly from terminal output without exaggerating severity.

- Wrong: "The test runner completely destroyed my terminal and blew up the entire build system."
- Right: "Running `python -m py_compile action/report.py` succeeded with exit code 0, but `scripts/score_readme.py` failed due to missing CLI flags."

### Rule 5: Comply with repository AI disclosure requirements
When a repository's contribution policy requires disclosing AI assistance, state the disclosure clearly and transparently in the comment.

- Wrong: Submitting an AI-assisted comment to a repository with a mandatory AI disclosure policy without mentioning the assistance.
- Right: "Per the repository AI usage policy: I used an AI assistant to help format this reproduction log; all commands, runs, and code edits were conducted and verified by me locally."

## Things I never post

- Demands for assignment or ownership ("Assign this to me", "Please assign me", "Reserve this issue for me").
- Overconfident guarantees without proof ("Guaranteed reproducible", "100% fixed", "Easy fix").
- Speculative timelines or fixed delivery promises ("Will finish by tomorrow", "PR coming in 48 hours", "ETA 2 days").
- Empty "+1" or "me too" comments that add no new environment, steps, or logs.
- Unsolicited architectural refactors or scope expansions beyond the reported issue.
- Boilerplate pleasantries that fail to engage with the concrete technical problem.
