# Rubric: is this a good first issue?

<!--
THIS IS THE PART YOU WRITE. The skill in SKILL.md executes whatever checks
you define here. It ships empty on purpose: the judgment is your work.

A filled rubric must contain:

1. At least one row in the checks table. Each row needs all four columns:
   - Check: a short name (used in the output JSON).
   - Evidence: exactly what to look at, and where. Name the source
     (repo-facts block, issue body, comment thread, or the locations in
     references/evidence-guide.md). "The repo" is not a source; "the last
     5 default-branch commit dates" is.
   - Pass condition: a condition someone else could apply and get your
     answer. Prefer thresholds with numbers ("a maintainer commented
     within 30 days") over adjectives ("maintainer is responsive").
   - Weight: `required` (a fail here rejects the issue) or `preferred`
     (never changes the verdict; a nice-to-have that helps rank the
     issues you accept).

2. A verdict rule below the table: how the check grades combine into
   accept or reject, including how `unclear` is treated. The verdict
   space is binary. If you write no rule for `unclear`, the skill treats
   it as fail.

Cover what actually kills first contributions. The lecture named four
families: the maintainer is alive, the repo is in use, the scope fits a
newcomer, and nobody else is already on it. A rubric that ignores a family
will fail eval issues designed around that family.
-->

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| Active repository | Repo facts: `archived`, `last push to any branch`, and the capture date; in live mode, the repository page and current date | The repository is not archived and its last push to any branch is no more than 365 days before the bundle capture date (or today in live mode). | required |
| Bounded first-issue scope | Issue body, checklist, and comment thread | The issue asks for one bounded contribution with a concrete behavior, documentation location, test/fixture change, or narrowly specified feature. Fail an explicit umbrella or tracking issue, codebase-wide effort, unresolved design debate, pure usage question, or underspecified product request. | required |
| No active claim | Repo facts for assignees and linked PRs, plus the issue comment thread | Pass when there is no assignee, no open linked PR, and no maintainer-confirmed current claim in the thread. A closed or merged linked PR alone does not fail. In live Path Review mode, follow `scope.md` and ignore other students' claim comments. | required |
| AI-compatible contribution policy | The contribution-policy line in Repo facts; in live mode, `CONTRIBUTING.md`, linked contributor docs, dedicated AI policy files, and templates | Pass when the policy is silent or permits AI-assisted work, including conditions such as disclosure, human review, testing, or personal understanding. Fail only an outright ban on AI-generated code or documentation. | required |
| Maintainer response signal | Repo facts: the five-issue maintainer first-response sample, and the current issue thread | Preferred pass when at least one sampled issue has an owner, member, or collaborator response within 90 days, or the current thread has a maintainer response. Otherwise grade fail or unclear, but never use this check to reject an issue. | preferred |

## Verdict rule

Accept if every required check passes. Preferred checks never change the
verdict and only help rank accepted candidates. Treat `unclear` as fail for
required checks because a first issue that cannot be verified is not ready to
take; treat it as fail for the preferred check without changing acceptance.
