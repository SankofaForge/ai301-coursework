# Contribution: One command to run every CI check locally, plus fork-sync guidance for contributors

Path: `beat-2-contribution/contribution-story.md`

This file is Assignment 5, and it is graded at the path above; a copy kept anywhere else in
the repository is not read. **Keep every section header below under its exact name** — the
format criteria grade exactly that. Your course repo link is the whole submission: no tool
files and no evidence uploads are part of Assignment 5.

**Contribution Number:** 1
**Student:** Olayinka Vaughan
**GitHub Username:** Builder106
**Issue:** https://github.com/tanmayai23/README-Editor-skill/issues/22
**Pull Request:** [GitHub PR link, once opened]

One repository, built across units 5 to 8, telling the whole story of your real
contribution. Fill it as you work, not at the end — the sections below ask for evidence that
is far easier to write down as it happens than to reconstruct in the last weekend.

Contribution Number stays `[1]` unless you make more than one contribution this term; it
just numbers them.

---

## Toolkit

Every story section below, from Why I Chose This Issue through Pull
Request, ends with a Toolkit block: which tool did that phase's work
and how you used it, what it produced, what difficulties or
shortcomings it presented, and what you changed or would change
because of them. Together the blocks are the thread the rubric's
Toolkit points read, and they are the raw material for your unit-9
portfolio, so keep them current as you work rather than
reconstructing them later.

A Toolkit block looks like this (copy it into each story section and
fill it there):

```text
**Toolkit**

- Tool: [which tool did this phase's work, and how you used it]
- What it produced: [described in a sentence or a short excerpt]
- Difficulties: [what fought you or fell short, or "none met"]
- What changed: [the patch, revision, or workaround, what you would
  update, or "nothing"]
```

This section also keeps one short dated entry per week of tool work,
starting below: what you built or changed that week, what broke, and
what you changed because of it. The blocks tell the story where it
happened; these entries are the toolkit's own timeline.

All four entries are graded. Keep every heading below, and fill each
one in the week it belongs to.

**Unit 5: Building and validating the issue-scout across live GitHub searches**

I upgraded the issue-select skill into issue-scout by authoring a multi-query search strategy and metadata ranking filters mapped to my fit profile. In the initial live scan, the scout surfaced 291 candidate issues and correctly filtered down to 5 survivors, accepting 4 bounded automation tasks and rejecting an open-ended test migration. The ranking filters favored zero-comment issues so heavily that one active repository took four of the top slots, demonstrating the need for an eventual per-repo diversity limit.

**Unit 6: Authoring repo-memory and standing up the voice-guard**

I authored the target repository's memory file (`CLAUDE.local.md`) from `CONTRIBUTING.md` and standing CI workflows, and installed the voice-guard to gate outgoing issue comments against my extended voice guide. The initial orientation extraction pulled verbose workflow runs that exceeded my line budget, so I pruned the command transcripts to keep the memory file under 60 lines focused strictly on local verification steps and contributor conventions. The voice-guard passed the drafted claim comment on its first run because my voice guide rules against unverified delivery promises and assignment demands already held in the text.

**Unit 7: [one line on the tool work]**

[2-4 sentences: the ship-gate and your gate manifest. What it produced
on your real branch, what fought you, what changed because of it.]

**Unit 8: [one line on the tool work]**

[2-4 sentences: the PR-monitor and your playbook. What it read, what it
drafted, what you did with the draft.]

---

## Why I Chose This Issue

I searched across active GitHub repositories using a three-query search strategy focused on beginner-friendly Python and TypeScript newcomer opportunities. The initial scan surfaced 291 candidate issues, which the ranking pipeline narrowed down to 270 unassigned candidates active within the past 90 days before evaluating the top survivors against the five-check rubric. Issue #22 on `tanmayai23/README-Editor-skill` earned an unequivocal accept verdict: the repository is actively maintained, the issue has zero existing assignees or comments, the project has an AI-compatible contribution policy, and the deliverable is strictly bounded. The task requires writing a standard-library `scripts/check_all.py` script that replicates the repository's 10-step CI pipeline locally, alongside updating `CONTRIBUTING.md` and the PR template with fork-synchronization guidance.

This issue matches my interest in developer tooling, continuous integration verification, and Python automation. Because first-time contributors currently face delayed CI execution pending maintainer approval, providing a single cross-platform command that reproduces CI locally solves an immediate contributor friction point. Working on this issue will help me build deeper proficiency with cross-platform standard library automation across Windows, macOS, and Linux, and practice drafting clear contributor documentation. In evaluating the issue-scout during this wild scan, I noticed that its zero-comment ranking heuristic clustered four issues from this single repository into the top five slots; while each issue passed rubric checks individually, adding a per-repository diversity cap will prevent single-repo dominance in future scans.

**Claim Status:** `claim pending (2026-10-21)`

Guarded claim draft verified by `voice_guard.py`:
> "Hi! I would like to investigate issue #22 to implement the local CI check runner in `scripts/check_all.py` and document fork-sync guidelines in `CONTRIBUTING.md`. I will prototype the standard-library runner against local environments and verify all checks before submitting a PR."

**Toolkit**

- Tool: issue-scout (search strategy with 3 queries, 5-check rubric), executed via GitHub CLI
- What it produced: Live wild scan of 291 candidate issues, ranking `tanmayai23/README-Editor-skill#22` as the #1 accepted survivor.
- Difficulties: Zero-comment ranking bias heavily concentrated top results on a single repository that published several issues simultaneously.
- What changed: Documented the need for an explicit per-repository diversity cap (maximum 2 issues per repo in the top results) for subsequent scan iterations.

---

## Understanding the Issue

**Problem Description**

The `README-Editor-skill` repository runs approximately ten distinct validation checks across its GitHub Actions CI matrix (covering script compilation, 15 ecosystem unit tests, repository analyzers, README scoring, claim verification, SVG banner generation, and manifest parity across Python versions). However, `CONTRIBUTING.md` and the pull request template currently document only three of these commands. New contributors only discover the remaining checks when remote CI fails—and because first-time contributors require manual workflow approval from maintainers, feedback cycles are slow. Furthermore, several recent pull requests were branched from outdated forks rather than synced `main`, causing merge conflicts and near-reversions of recently landed features.

**Expected Behavior**

Contributors should be able to run a single, cross-platform standard-library command (`python scripts/check_all.py`) that mirrors every check executed by `.github/workflows/ci.yml` locally and outputs a clear pass/fail summary. Additionally, `CONTRIBUTING.md` and the PR template should explicitly guide contributors to sync their forks with upstream `main` and branch before writing code.

**Current Behavior**

Contributors must manually locate and run fragmented commands, several CI checks lack local documentation, and pull requests frequently fail remote CI on first submission or arrive out-of-sync with upstream.

**Affected Components**

- `scripts/check_all.py` (new stdlib-only validation runner)
- `CONTRIBUTING.md` (local check commands and fork-sync documentation)
- `.github/pull_request_template.md` (updated pre-submission checklist)
- `.github/workflows/ci.yml` (canonical reference for check steps)

**Toolkit**

- Tool: repo-memory (`CLAUDE.local.md`) and repository analysis
- What it produced: Mapped the complete list of 10+ CI workflow steps in `ci.yml` against the 3 checks documented in `CONTRIBUTING.md`.
- Difficulties: Initial raw extraction exceeded line budgets by including raw bash snippets and matrix definitions.
- What changed: Condensed the extraction into a high-level component map under 60 lines.

---

## Reproduction Process

**Environment Setup**

[What a stranger would need to stand this up: your operating system,
the relevant versions (language, runtime, package manager, the project
itself), and how you set the project up. Then the challenges you faced
and how you solved them, or that none came up.]

**Steps to Reproduce**

1. [Step 1]
2. [Step 2]
3. [Observed result]

**Reproduction Evidence**

- **Commit showing reproduction:** [link to commit in your fork]
- **Screenshots/logs:** [if applicable]
- **My findings:** [what you discovered during reproduction; an
  honest, evidenced cannot-reproduce that led you to re-pick or ask
  the maintainer belongs here and costs you nothing]

**Toolkit**

- Tool:
- What it produced:
- Difficulties:
- What changed:

---

## Solution Approach

**Analysis**

[Your analysis of the root cause: what is causing the issue, traced
to the files and functions involved.]

**Proposed Solution**

[High-level description of your fix approach, and what you are
deliberately NOT changing.]

**Implementation Plan**

1. [Modify file X to do Y]
2. [Add or change Z]
3. [Update tests]

[Record deviations here as they happen: what changed mid-build and
why. A recorded deviation is honest work; silent drift is not.]

**Toolkit**

- Tool:
- What it produced:
- Difficulties:
- What changed:

---

## Testing Strategy

[What observable checks prove the fix: your reproduction steps re-run
against the built change (before and after), and the repo's own test
suite or checks with the outcome shown. "Tests pass" with nothing
observable named is not a strategy.]

**Toolkit**

- Tool:
- What it produced:
- Difficulties:
- What changed:

---

## Implementation Notes

[A running log, added to as you work. Date each entry. What you
built, decisions you made when you made them, wrong turns included.]

**[Date]**

[Entry]

**[Date]**

[Entry]

**Toolkit**

- Tool:
- What it produced:
- Difficulties:
- What changed:

---

## Pull Request

**PR Link:** [GitHub PR URL when opened]

**PR Description:** [what the PR says; much of the content above
adapts into it]

**Maintainer Feedback:**

- [Date]: [feedback received, or "none yet"; silence is a normal
  state and costs you nothing]
- [Date]: [how you addressed it]

**Status:** [Awaiting review / Iterating / Merged / Closed. The
status is a fact you record, never a grade: the PR is graded as
opened.]

**Toolkit**

- Tool:
- What it produced:
- Difficulties:
- What changed:

---

## Learnings and Reflections

**Technical Skills Gained**

[What you learned technically, named concretely.]

**Challenges Overcome**

[What was hard and how you solved it; point at the real events, the
Toolkit blocks above are full of them.]

**What I'd Do Differently Next Time**

[Reflection on your process.]

---

## Resources Used

[What actually helped, not a reading list. List things this story
already shows you using: the doc you followed to set the environment
up, the thread that explained the bug, the person who answered you.
One real entry beats ten plausible ones.]

- [Link to documentation that helped]
- [Discussion, issue, or post that helped]
