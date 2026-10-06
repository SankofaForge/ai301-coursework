# Rubric: is this pull request ready to submit?

This rubric defines the checks and decision rules for evaluating candidate PR packages. Every check evaluates verifiable evidence against strict pass conditions.

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| standards-compliance | Candidate PR description, title, and diff read against the repo facts block's PR template asks, checklist items, and contribution policies (including AI disclosure). | All required PR template sections, checklist items, and mandatory documentation entries (such as whatsnew or changelog updates) specified by the repository are present and substantively completed. If the repository policy requires AI usage disclosure (all packages being AI-assisted), the PR description satisfies the repository's stated disclosure rules (disclosing AI assistance and confirming human understanding or naming the tool as required by that repo). | required |
| plan-fidelity | Candidate PR diff, commits, and description read against the accepted plan's scope, boundary, and deviation notes. | The diff implements only what falls within the accepted plan's stated scope and boundary, adding no unrequested features, settings, CLI flags, configuration options, unsolicited renames, or architectural refactorings. Any deferred scope or known limitation is recorded in advance as an explicit deviation note in the plan and honestly stated in the PR description. The description's claims faithfully reflect the diff, neither claiming changes absent from the diff nor claiming exact adherence when unannounced scope is present. | required |
| test-evidence | Candidate PR test evidence section and added test files read against the accepted plan's test plan and the issue's reproduction steps. | The evidence demonstrates decisive, observable before-and-after proof on the specific defect path identified in the reproduction steps and test plan (not merely an unaffected control path or unrelated test case). The evidence shows concrete commands and observable execution outputs rather than bare assertions ('tested locally', 'works on my machine', 'all tests pass' without named commands and outputs). | required |
| diff-quality | Candidate PR unified diff and commit list. | The diff is clean, focused, and reviewable: it is free of debugging debris, including commented-out code or aborted experiments, temporary debug print or logging statements (e.g. eprintln, print), dead or unused probe functions, TODO markers on imports, and distracting formatting, indentation, or import churn unrelated to the fix. | required |

## Verdict rule

A package receives `accept` if and only if every required check passes. If any required check receives `fail` or `unclear`, the verdict is `reject`. Preferred checks never change the verdict. An unverifiable claim receives `unclear`, which counts as `fail`.
