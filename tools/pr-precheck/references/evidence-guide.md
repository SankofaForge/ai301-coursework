# Evidence guide: where evidence lives in a PR package

This guide maps where evidence lives in a candidate PR package and defines observable standards for evaluating each evidence family. Use this map during evidence gathering and check execution.

## Plan fidelity (harness category: silent-drift)

### Where it lives
- **Eval mode**: Compare the package's `Plan context` block (specifically the stated scope, files to touch, out-of-scope boundaries, and deviation notes) against the candidate PR's `Diff`, `Commits`, and `Description`.
- **Live mode**: Compare your accepted plan file (`beat-1-sandbox/unit-3/plan.md`) and any recorded deviation notes against the working branch diff (`git diff main...HEAD`), commit history (`git log main..HEAD`), and draft PR title/description.

### What good looks like
- Every file touched and every code hunk in the diff implements the accepted plan and falls strictly within its stated boundary and scope.
- The diff adds no unrequested features, settings, CLI flags, configuration options, unsolicited renames, or architectural refactorings outside the plan.
- If a shortfall, limitation, or deferred edge case exists, it was recorded in advance as an explicit deviation note in the plan and is honestly stated in the PR description so reviewers can assess it.
- The PR description makes accurate, verifiable claims: it never claims changes absent from the diff (such as documentation updates or tests not present in the diff), and never claims "implements plan exactly" or "no changes beyond the plan" when unannounced scope is present in the diff.

## Test evidence (harness category: not-tested)

### Where it lives
- **Eval mode**: The candidate PR's `Test evidence` section and any test files added or modified in the `Diff`, read against the `Issue` description and the `Plan context`'s repro evidence and test plan.
- **Live mode**: Terminal transcripts of re-running the issue's reproduction command before and after the fix, test execution output (`make test-unit`, `pytest`, `cargo test`), and updated test files in the working directory.

### What good looks like
- The evidence provides concrete, observable before-and-after proof on the specific defect path identified in the reproduction report and plan (e.g. demonstrating the fix on the affected input/flag/behavior, rather than merely re-running an unaffected control path or unrelated test).
- Test execution shows actual terminal commands, exit statuses, and verbatim execution outputs rather than bare, unevidenced text assertions ("tested locally", "works on my machine", "all tests pass" without named commands and outputs).
- Added or updated automated tests exercise the reported defect behavior, and any corresponding `@pytest.mark.xfail` markers are removed.

## Diff quality (harness category: unreviewable)

### Where it lives
- **Eval mode**: The candidate PR's `Diff` and `Commits` sections.
- **Live mode**: The unified diff from `git diff main...HEAD` and the commit log from `git log main..HEAD`.

### What good looks like
- The diff is concise, focused, and reviewable: every hunk directly implements the planned fix.
- The code is free of debugging debris: no temporary print or logging statements (e.g. `eprintln`, `console.log`, `print`), no commented-out code blocks or aborted experiments, no dead or unused functions (e.g. behind `#[allow(dead_code)]`), and no stray `TODO` markers.
- The diff contains no unnecessary whitespace churn, reformatting, indentation rewrites, or whole-file import reorganizations that obscure the substantive change.
- Commits are atomic and structured with descriptive messages, without temporary "wip", "fix", or "cleanup" scratch commits.

## Standards and comms (harness category: standards-wall)

### Where it lives
- **Eval mode**: The `Repo facts` block (PR template requirements, checklists, documentation asks like whatsnew or changelog entries, and contribution policy / AI usage policy), read against the candidate PR's `Description`, `Title`, and `Diff`.
- **Live mode**: `.github/PULL_REQUEST_TEMPLATE.md` and repository guidelines (`docs/CONTRIBUTING.md`, `AI_POLICY.md`), read against your draft PR title, description, and branch.

### What good looks like
- All required PR template sections, checklist items, and mandatory repository asks (such as issue reference keywords `Closes #xxxx` or documentation release notes) are present and substantively filled out rather than omitted or ignored.
- Where repository policy mandates AI usage disclosure (every eval package is treated as AI-assisted work), the PR description explicitly satisfies the repository's stated disclosure rules (e.g. disclosing AI assistance and confirming human comprehension or stating the tool per the repo's policy).
- Any explicit maintainer direction or thread convention highlighted in the repository context is respected.

