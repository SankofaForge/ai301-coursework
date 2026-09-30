# Procedure: how this skill grades a plan package

This procedure defines the exact execution workflow for grading a plan package in both eval mode and live mode.

## Read order

1. **Read the issue and maintainer context first**:
   - In eval mode, read the package bundle's "Issue" description and "Thread highlights" to understand the reported problem and maintainer reactions.
   - In live mode, verify the issue repo against `scope.md`, then fetch the issue description and thread comments from GitHub.
2. **Read the repository facts and policies**:
   - Note the stated bug-reporting requirements, contribution guidelines, and especially any AI usage and disclosure policies from the "Repo facts" block (or `CONTRIBUTING.md` / `AI_POLICY.md` live).
3. **Read the reproduction evidence to establish ground truth**:
   - Carefully read the "Repro evidence" block (or live reproduction comment). Note the exact reproduction steps, the observed failure artifact/stack trace, and critically, the control runs and isolation checks. This establishes the objective technical baseline against which the plan will be judged.
4. **Read the candidate plan and candidate plan comment**:
   - Read the candidate plan's diagnosis, scope boundaries, files/areas, approach, test plan, and risks/unknowns.
   - Read the candidate plan comment to see how the author proposes the work to the repository and maintainers.

## Evidence gathering

1. **Gather diagnosis grounding evidence**:
   - Locate the plan's stated cause or problem statement.
   - Cross-reference with the repro evidence's control runs and stack traces. Record whether the diagnosis accounts for the observed defect or contradicts control runs (e.g., blaming a component that control runs prove works).
2. **Gather scope bounding evidence**:
   - Locate the plan's scope, approach, and proposed changes.
   - Record whether the changes are bounded to the defect, or whether they bundle unrelated refactors, dependency upgrades, multi-runtime redesigns, or unsolicited features.
3. **Gather executability evidence**:
   - Locate the files/areas and approach steps.
   - Record whether concrete file paths and an actionable technical mechanism are specified, or whether key decisions are deferred to build time ("investigate", "profile and see", "fix whichever is easier").
4. **Gather test plan evidence**:
   - Locate the plan's test plan section.
   - Compare with the repro evidence steps and artifacts. Record whether the test plan names concrete, observable outcomes (e.g. exit code 0, specific state change, regression assertions) or subjective sensations ("should feel fast").
5. **Gather thread alignment evidence**:
   - Check thread highlights (or live thread) for maintainer direction, maintainer-provided diagnostic leads, or maintainer test requests.
   - Record whether the candidate plan and comment engage and align with that direction, or propose a conflicting/uncoordinated workaround.
6. **Gather policy compliance evidence**:
   - Check repo facts for contribution rules and AI disclosure mandates.
   - Record whether the candidate plan comment satisfies those rules, specifically checking for explicit AI disclosure when required (all packages are evaluated as AI-assisted work).

## Check execution

1. Execute the rubric checks in order:
   - `grounded-cause`
   - `bounded-scope`
   - `stranger-executable`
   - `decisive-test-plan`
   - `thread-alignment`
   - `policy-compliance`
2. For each check, compare the gathered evidence directly against the pass condition in `rubric.md` and the criteria in `references/evidence-guide.md`.
3. Grade each check as `pass` if the evidence satisfies the pass condition, or `fail` if the evidence fails the condition. If essential evidence is missing (e.g. no files named, no test plan, or missing AI disclosure when required), grade `fail`.
4. Record a concise, factual one-line evidence summary for each check citing the specific finding.

## Verdict assembly

1. Apply the rubric's verdict rule:
   - If every required check passes (`pass`), assign the final verdict `accept`.
   - If any required check fails (`fail`) or is `unclear`, assign the final verdict `reject`.
2. Preferred checks do not alter the final verdict.
3. In live mode, check `comment.md` against `voice-guide.md` and report any rule violations in the commentary.
4. Emit a concise summary followed by the required fenced JSON block as the very last element of the response:
   ```json
   {
     "item": "<issue URL or bundle id>",
     "checks": [
       {"name": "<check name>", "grade": "pass|fail|unclear", "evidence": "<one line fact or quote>"}
     ],
     "verdict": "accept|reject"
   }
   ```
