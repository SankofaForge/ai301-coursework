# Evidence guide: where evidence lives in a plan package

This guide maps each kind of evidence evaluated by plan-check to its location in an eval package bundle or live workspace, and defines observable standards for what good looks like.

## Diagnosis and grounding

- **Where it lives**:
  - *Eval bundle*: In the Candidate Plan's "Diagnosis", "Cause", or "Problem statement" section, read directly against the package's "Repro evidence" block (specifically the reproduction steps, control runs, terminal artifacts, stack traces, and actual vs. expected behavior).
  - *Live mode*: In `plan.md` under "Diagnosis" or "Cause", read against the student's posted reproduction comment on the GitHub issue thread (or the instructor house repro pack).
- **What good looks like**:
  - The stated root cause directly accounts for the specific failure demonstrated by the reproduction steps and artifacts.
  - The diagnosis is consistent with all control runs and isolation steps (e.g., does not blame a tokenizer or module when a control run shows that identical input succeeds without the trigger flag, and does not blame a downstream cast when data was already converted upstream).
  - It identifies the mechanism of the failure rather than mistaking an incidental symptom for the underlying cause.

## Scope

- **Where it lives**:
  - *Eval bundle*: In the Candidate Plan's "Scope", "Proposed changes", or "In scope / Not in scope" statements, and the Candidate Plan Comment.
  - *Live mode*: In `plan.md` under "Scope" and in `comment.md`.
- **What good looks like**:
  - The proposed change is tightly bounded to fixing the reproduced defect.
  - In-scope items and out-of-scope boundaries are explicitly defined.
  - The fix is not bundled with drive-by refactorings, unsolicited feature additions, framework or dependency upgrades, cross-runtime architectural overhauls, or while-in-the-area polish.
  - When broader systemic improvements are possible, the plan explicitly defers them to keep the current change reviewable and low-risk.

## Executability

- **Where it lives**:
  - *Eval bundle*: In the Candidate Plan's "Files and areas", "Approach", and "Steps" sections.
  - *Live mode*: In `plan.md` under "Files to touch" and "Approach".
- **What good looks like**:
  - Concrete file paths, functions, or code structures are identified by name.
  - The technical mechanism and approach are clear and actionable; an unfamiliar contributor or stranger could immediately begin implementation without having to guess or ask the author what to do.
  - Crucial architectural decisions (such as which library layer to touch, how errors should be surfaced, or whether to patch upstream vs. downstream) are decided in the plan, rather than deferred with "investigate and see", "look into caching", or "fix whichever is easier".

## Test plan

- **Where it lives**:
  - *Eval bundle*: In the Candidate Plan's "Test plan" section, read in relation to the "Repro evidence" steps and expected behavior.
  - *Live mode*: In `plan.md` under "Test plan".
- **What good looks like**:
  - Specifies concrete, observable verification criteria (e.g., re-running the reproduction commands and asserting specific exit codes, status indicators, or outputs; or adding targeted regression unit tests that assert expected values).
  - Success is defined by concrete, measurable behavior, not subjective sensations ("should feel fast", "looks much better") or vague non-checks ("run the whole test suite and hope nothing broke").

## Honesty

- **Where it lives**:
  - *Eval bundle*: In the Candidate Plan's "Risks", "Unknowns", and any "Deviations" section.
  - *Live mode*: In `plan.md` under "Risks and unknowns" and "Deviations".
- **What good looks like**:
  - Open questions, performance risks, or platform-dependent edge cases are surfaced honestly rather than hidden under false confidence.
  - If the implementation deviates from the initial plan, the differences and rationale are clearly documented under "Deviations" (or if no deviation occurred, "Nothing changed from the plan" is explicitly stated in the author's own words).

## Comms

- **Where it lives**:
  - *Eval bundle*: In the Candidate Plan Comment, read against the "Thread highlights" and "Repo facts" block (especially the bug report requirements, CONTRIBUTING.md, and AI policies).
  - *Live mode*: In `comment.md`, read against the GitHub issue thread, repository contribution guidelines, and `voice-guide.md`.
- **What good looks like**:
  - The comment respects and actively engages with maintainer direction, prior-art PRs, or maintainer diagnoses present in the thread, rather than posting a disconnected workaround that ignores explicit maintainer guidance.
  - If repository contribution policy mandates disclosure of AI assistance (e.g., Ghostty's AI policy), the comment contains the explicit required disclosure (all evaluation packages are evaluated as AI-assisted work; omitting required disclosure is a strict failure).
  - The comment communicates technical substance concisely, sets realistic expectations, and respects maintainer review bandwidth.
