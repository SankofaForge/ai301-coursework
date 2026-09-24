# Rubric: is this reproduction package ready to post?

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| environment-recorded | Repro report environment section read against the issue's stated target and context. | Names the operating system and relevant software/runtime versions (or execution context such as browser, container, or distribution) matching the issue's target or explicitly explaining any version/environment difference. Fails if environment details are missing entirely or if there are unacknowledged environment deviations from the issue's target. | required |
| steps-rerunnable | Repro report steps section read against the starting state and reproduction trigger. | Gives complete, self-contained, followable steps and exact commands/inputs that a stranger can execute without relying on unshared private repositories, hidden configs, or missing setup details. | required |
| behavior-evidenced | Repro report artifacts (command outputs, logs, error transcripts, or screenshots) read against the issue description. | Includes concrete, verifiable artifacts (command outputs, logs, traces, or terminal output) showing the outcome of running the steps, rather than merely asserting that a bug happened or that an unevidenced race condition occurred. | required |
| target-matched | Repro report artifacts and observations read against the specific defect described in the issue. | The artifacts demonstrate the specific failure mode, error, or contract violation described in the issue (or, in an honest cannot-reproduce, document the exact failure condition tested), rather than triggering an adjacent symptom, graceful validation error, CLI syntax error, or normal alive behavior. | required |
| honest-conclusion | Repro report actual-versus-expected observations and stated outcome read against the captured artifacts. | The narrative accurately and honestly reflects what the artifacts actually demonstrate without overclaiming, fabricating a reproduction, or misrepresenting a graceful error or active process as a crash. An honest, evidenced report that the issue could not be reproduced passes. | required |
| substantive-claim | Candidate claim comment read against the issue and thread context. | Specifically references the issue's defect or files and states concrete next investigation steps, without using generic interchangeable boilerplate, demanding assignment, or guaranteeing unrealistic delivery dates. | required |
| policy-conventions | Claim comment and repro report read against the repo-facts block (contribution policy and AI use guidelines). | Complies with all stated repository policies. When a repository's policy requires disclosing AI assistance, the comments must explicitly include that required disclosure (packages are evaluated as AI-assisted work; silence or lack of disclosure when required is a fail). | required |

## Verdict rule

Accept if every required check passes; preferred checks never change the verdict; unclear counts as fail. In live mode with a claim-only draft, checks that require reproduction artifacts report unclear as not yet applicable and are excluded from the verdict rule, so the verdict depends only on the claim and policy checks.
