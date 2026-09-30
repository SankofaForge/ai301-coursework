# Rubric: is this plan ready to post and build from?

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| grounded-cause | Candidate plan's diagnosis and cause read against the repro evidence (steps, actual/expected outputs, control runs, and stack traces). | The stated cause directly accounts for the failure demonstrated in the repro evidence and does not contradict any control run, timing measurement, error log, or stack trace (e.g., does not blame an unaffected tokenizer when a control run shows identical inputs parse fine without the flag, and does not blame an inactive or missing module when control runs prove it active). | required |
| bounded-scope | Candidate plan's scope, proposed changes, files/areas, and plan comment read against the specific defect in the issue and repro evidence. | Tightly bounded to fixing the reproduced defect without bundling unrelated drive-by refactorings, framework/dependency upgrades, cross-runtime abstractions, unsolicited new features/options, or redesigns of adjacent systems. Broader potential work or redesigns are explicitly excluded or deferred. | required |
| stranger-executable | Candidate plan's files/areas, approach, and implementation steps. | Names concrete files or components and defines a specific, actionable technical mechanism that an unfamiliar contributor could immediately start executing without having to guess the layer, investigate from scratch, or resolve deferred architectural choices. | required |
| decisive-test-plan | Candidate plan's test plan read against the repro evidence and expected behavior. | Specifies an observable, verifiable outcome resulting from concrete commands, test cases, or re-run repro steps (such as specific exit codes, state transitions, or assertion passes), rather than subjective sensations ("feels faster", "looks better") or vague non-checks ("run the full test suite"). | required |
| thread-alignment | Candidate plan comment and plan read against the issue's thread highlights and maintainer direction. | Directly engages with and respects explicit maintainer direction, maintainer requests for testing, or maintainer diagnosis provided in the thread, rather than advancing a conflicting or uncoordinated workaround that ignores maintainer guidance. | required |
| policy-compliance | Candidate plan comment read against the repo-facts block (contribution policy and AI use guidelines). | Complies with all stated repository contribution policies and guidelines. When a repository's policy requires disclosing AI assistance, the comment must explicitly include that required disclosure (packages are evaluated as AI-assisted work; silence or lack of disclosure when required is a fail). | required |

## Verdict rule

Accept if every required check passes; preferred checks never change the verdict; unclear counts as fail.
