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
**Pull Request:** https://github.com/tanmayai23/README-Editor-skill/pull/24

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

This section also keeps one short dated entry per week of tool work,
starting below: what you built or changed that week, what broke, and
what you changed because of it. The blocks tell the story where it
happened; these entries are the toolkit's own timeline.

All four entries are graded. Keep every heading below, and fill each
one in the week it belongs to.

**Unit 5: Building and validating the issue-scout across live GitHub searches**

I upgraded the issue-select skill into issue-scout by authoring a multi-query search strategy and metadata ranking filters mapped to my fit profile. In the initial live scan, the scout surfaced 291 candidate issues, filtered down to 270 unassigned candidates active within 90 days, and evaluated the top 5 survivors with our rubric, accepting 4 bounded automation tasks and rejecting an open-ended test migration. The ranking filters favored zero-comment issues so heavily that one active repository took four of the top slots, demonstrating the need for an eventual per-repo diversity limit.

**Unit 6: Authoring repo-memory and standing up the voice-guard**

I authored the target repository's memory file (`CLAUDE.local.md`) from `CONTRIBUTING.md` and standing CI workflows, and installed the voice-guard to gate outgoing issue comments against my extended voice guide. The initial orientation extraction pulled verbose workflow runs that exceeded my line budget, so I pruned the command transcripts to keep the memory file under 60 lines focused strictly on local verification steps and contributor conventions. The voice-guard passed the drafted claim comment on its first run because my voice guide rules against unverified delivery promises and assignment demands already held in the text.

**Unit 7: Implementing ship-gate verification and writing the gate manifest**

I configured the ship-gate hook and authored `ship-manifest.md` for `README-Editor-skill`, mapping its 16-step CI workflow steps into pre-submission gates. The ship-gate caught that our initial script compilation check omitted `action/report.py`, allowing me to fix the script inclusion before running the test suite. Gating local commits through the manifest ensured that all 112 unit tests, claim verifications, and README scoring checks passed cleanly before staging changes.

**Unit 8: Standing up PR-monitor and executing automated playbook checks**

I deployed the PR-monitor tool with an automated monitoring playbook to track upstream repository events, pull request CI status, and maintainer feedback. Running the monitor against our branch verified that all local checks passed and generated the pull request summary template. Because the pull request is awaiting maintainer triage, the playbook correctly evaluated the review threshold and held back any speculative nudges, maintaining professional contribution etiquette.

---

## Why I Chose This Issue

I searched across active GitHub repositories using a three-query search strategy focused on beginner-friendly Python and TypeScript newcomer opportunities. The initial scan surfaced 291 candidate issues, which the ranking pipeline narrowed down to 270 unassigned candidates active within the past 90 days before evaluating the top survivors against the five-check rubric. Issue #22 on `tanmayai23/README-Editor-skill` earned an unequivocal accept verdict: the repository is actively maintained, the issue has zero existing assignees or comments, the project has an AI-compatible contribution policy, and the deliverable is strictly bounded. The task requires writing a standard-library `scripts/check_all.py` script that replicates the repository's 16-step CI pipeline locally, alongside updating `CONTRIBUTING.md` and the PR template with fork-synchronization guidance.

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

The `README-Editor-skill` repository runs 16 distinct validation steps across its GitHub Actions CI workflow (`.github/workflows/ci.yml`), covering script compilation, 15 ecosystem unit tests, repository analyzers, README scoring, claim verification, SVG banner generation, and manifest parity across Python versions. However, `CONTRIBUTING.md` and the pull request template currently document only 4 of these commands (`unittest`, `py_compile`, `score_readme`, `verify_readme`). New contributors only discover the remaining checks when remote CI fails—and because first-time contributors require manual workflow approval from maintainers, feedback cycles are slow. Furthermore, several recent pull requests were branched from outdated forks rather than synced `main`, causing merge conflicts and near-reversions of recently landed features.

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
- What it produced: Mapped the complete list of 16 CI workflow steps in `ci.yml` against the 4 checks documented in `CONTRIBUTING.md`.
- Difficulties: Initial raw extraction exceeded line budgets by including raw bash snippets and matrix definitions.
- What changed: Condensed the extraction into a high-level component map under 60 lines.

---

## Reproduction Process

**Environment Setup**

- Operating System: macOS (Darwin 24.3.0 arm64)
- Python Version: Python 3.13.0 (standard library only)
- Git Version: git version 2.39.5
- Upstream Project: `tanmayai23/README-Editor-skill` cloned into local workspace
- Setup Steps: Cloned the repository and inspected existing CI configurations in `.github/workflows/ci.yml`. Verified environment dependencies by confirming that all core scripts execute without external third-party pip packages.

**Steps to Reproduce**

1. Inspect `CONTRIBUTING.md` and `.github/pull_request_template.md` in a fresh clone of `README-Editor-skill`.
2. Observe documented pre-PR commands: only 4 fragmented checks (`unittest`, `py_compile`, `score_readme`, `verify_readme`) are listed, omitting analyzer runs, import graph runs, banner generators, template validation, and page kit example diff checks.
3. Attempt to run a single command to validate all repository checks locally.
4. Result: No unified command exists; contributors must manually copy and adapt commands from `.github/workflows/ci.yml`. Furthermore, no fork-syncing guidance is documented for new contributors.

**Reproduction Evidence**

- **Commit showing reproduction:** [tanmayai23/README-Editor-skill@main (Clean upstream checkout)](https://github.com/tanmayai23/README-Editor-skill/tree/main)
- **Observed gap & logs:**
  Running the proposed unified runner on a fresh checkout of upstream `main` reproduces the missing script:
  ```text
  $ python3 scripts/check_all.py
  python3: can't open file '.../scripts/check_all.py': [Errno 2] No such file or directory
  ```
  Auditing `CONTRIBUTING.md` against `.github/workflows/ci.yml` confirms that 12 of the 16 checks executed in CI (including `analyze_repo.py`, `import_graph.py`, template scoring, and page kit diff checks) lack local documentation, leaving contributors reliant on remote CI feedback.
- **My findings:** The repository has solid unit tests and a zero-dependency design, but completely lacks local orchestration for its 16 CI checks and provides no fork-sync guidance, causing avoidable CI turnaround delays for first-time contributors.

**Toolkit**

- Tool: repro-check and manual workflow inspection
- What it produced: Complete audit of `.github/workflows/ci.yml` revealing 16 distinct validation steps versus 4 documented checks.
- Difficulties: Some CI steps relied on bash-specific syntax (`for f in ...`) and temporary test directories (`ttt/`).
- What changed: Designed `check_all.py` to handle directory creation, test runs, and automatic cleanup cleanly across platforms.

---

## Solution Approach

**Analysis**

The root cause of contributor friction is that `.github/workflows/ci.yml` is the only place where the full verification pipeline was defined. Because GitHub Actions requires maintainer approval to run for first-time contributors, contributors had no single command to verify their work locally before opening a pull request. Additionally, contributors frequently submitted pull requests based on stale branches due to missing fork-sync guidelines in `CONTRIBUTING.md`.

**Proposed Solution**

1. Implement `scripts/check_all.py` using Python standard library only to execute every CI step sequentially with clear status logging and summary reporting.
2. Update `CONTRIBUTING.md` to feature `python scripts/check_all.py` as the primary pre-submission gate, and add explicit instructions for keeping forks synchronized with upstream `main`.
3. Update `.github/pull_request_template.md` with checklist items for fork synchronization and running `check_all.py`.
4. Deliberately NOT adding external dependencies or modifying existing core skill logic.

**Implementation Plan**

1. Create `scripts/check_all.py` covering all 16 CI checks (py_compile, unittests, analyzers, scoring, claim verifiers, banner generator, page kit examples diff, unicode text, tic-tac-toe game).
2. Add automatic cleanup for test directories (`ci-out`, `ci-logo`, `ci-btn`, `ttt`).
3. Update `CONTRIBUTING.md` with fork-sync instructions and local CI runner usage.
4. Update `.github/pull_request_template.md` checklist.
5. Update `CHANGELOG.md` under `[Unreleased]`.

**Toolkit**

- Tool: plan-check and code authoring
- What it produced: Bounded 4-file implementation plan touching `scripts/check_all.py`, `CONTRIBUTING.md`, `pull_request_template.md`, and `CHANGELOG.md`.
- Difficulties: Ensuring Windows path and platform compatibility without external libraries.
- What changed: Used `os.path.join` and standard library `subprocess` with explicit working directories.

---

## Testing Strategy

All 16 verification checks were executed via `python scripts/check_all.py`:
- Script compilation: `py_compile` succeeded on all scripts across `readme-forge`, `readme-forge-design`, and `action`.
- Unit tests: 112 tests across 15 ecosystems passed in 2.54s (`Ran 112 tests in 2.544s OK`).
- Repository analyzers and import graph: successfully ran against `demo/sample-app`.
- README scoring and verification: scored 85+ and achieved 100% claim accuracy.
- Page kit examples and README cards: rebuilt and verified zero git diff.
- Banner generation and profile game lifecycle: verified SVG output and state machine integrity.

**Toolkit**

- Tool: ship-gate (`scripts/check_all.py` and `unittest`)
- What it produced: 16/16 passing checks with exit code 0.
- Difficulties: Temporary files generated during test runs required explicit cleanup handling.
- What changed: Added post-execution cleanup in `scripts/check_all.py` to prevent untracked file clutter.

---

## Implementation Notes

**2026-10-14**

Initial wild scan executed using `issue-scout`. Evaluated candidate issues and selected issue #22 on `tanmayai23/README-Editor-skill`.

**2026-10-21**

Drafted repository memory `CLAUDE.local.md` and validated claim comment draft using `voice-guard`.

**2026-10-28**

Implemented `scripts/check_all.py`, updated `CONTRIBUTING.md`, `.github/pull_request_template.md`, and `CHANGELOG.md`. Validated all 16 CI checks locally.

**2026-11-01**

Configured `ship-gate` and `pr-monitor`. Finalized contribution story documentation and verified test runs.

**Toolkit**

- Tool: Implementation log and git commit history
- What it produced: Chronological record of technical decisions and milestones across units 5–8.
- Difficulties: Balancing comprehensive CI check replication with fast local execution time.
- What changed: Structured check_all.py to output immediate feedback per step and a clean summary table.

---

## Pull Request

**PR Link:** https://github.com/tanmayai23/README-Editor-skill/pull/24

**PR Description:**

```markdown
## What does this change?

Implements a standard-library `scripts/check_all.py` verification runner that mirrors all CI checks locally, and updates `CONTRIBUTING.md` and the pull request template with fork synchronization instructions. Closes #22.

## How was it tested?

Executed `python scripts/check_all.py` locally: all 16 checks (including 112 unit tests, script compilation, README scoring, claim verification, page kit rebuild diffs, and template validators) passed with zero errors.

## Checklist

- [x] Fork is synced with upstream main
- [x] Scripts still use the Python standard library only
- [x] Local CI checks pass (`python scripts/check_all.py`)
- [x] CHANGELOG.md updated under Unreleased
```

**Maintainer Feedback:**

- 2026-11-01: PR opened and submitted through ship-gate; awaiting initial maintainer triage.
- 2026-11-01: Local test suite verified with all checks passing; monitor set to observe feedback.

**Status:** Awaiting review

**Toolkit**

- Tool: PR-monitor and voice-guard
- What it produced: Guarded pull request description and structured checklist.
- Difficulties: Ensuring the PR description clearly articulated why local CI matters for first-time contributors without sounding demanding.
- What changed: Focused description purely on developer ergonomics and reducing maintainer CI review overhead.

---

## Learnings and Reflections

**Technical Skills Gained**

- Deepened expertise in writing cross-platform Python standard library automation scripts.
- Learned how to structure local test orchestrators that faithfully mirror GitHub Actions multi-job matrices.
- Mastered Git fork synchronization lifecycles and clean branch rebasing strategies.

**Challenges Overcome**

- Mapping diverse CI steps (from unit tests to SVG banner regex checks and profile game state transitions) into a unified, zero-dependency Python script.
- Ensuring test-generated artifacts in temporary directories (`ci-out`, `ttt`) were cleanly removed so git working trees remained pristine.

**What I'd Do Differently Next Time**

- Add an optional `--fast` flag to `check_all.py` to allow running just the unit test and syntax compilation suite during rapid iterative development.

---

## Resources Used

- GitHub Actions documentation on workflow syntax and matrices
- `README-Editor-skill` repository documentation (`CONTRIBUTING.md` and `.github/workflows/ci.yml`)
- Python `subprocess` and `unittest` standard library documentation
