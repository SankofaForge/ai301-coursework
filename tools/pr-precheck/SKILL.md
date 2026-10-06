---
name: pr-precheck
description: Grade a PR package (a candidate pull request read against the plan it claims to implement and the issue that plan belongs to) and decide whether it is ready to submit. Use when checking your own branch, draft PR title, and description before opening the pull request, or when grading an eval package bundle.
---

# pr-precheck: rubric-driven PR grading

## The question

This tool answers exactly one question about a candidate PR package: **is this ready to submit?** A PR package consists of a candidate pull request (title, description, commits, unified diff, and test evidence) read against the accepted plan it claims to implement (including scope boundaries, files touched, test plan, and recorded deviation notes) and the issue that plan belongs to. The tool evaluates the package strictly through its defined rubric components and procedure; it never evaluates other questions or guesses beyond the evidence.

## Inputs and modes

The tool operates in two distinct modes:

- **Live mode**: Used to grade the contributor's own pull request before opening it upstream. Inputs:
  1. The accepted plan and deviation notes from `beat-1-sandbox/unit-3/plan.md` (or the house plan file for house-chain contributors).
  2. The working branch diff against the default branch, produced directly from the repository working copy using `git diff main...HEAD`.
  3. The branch commit history, produced via `git log main..HEAD`.
  4. The draft PR title and description.
  5. The captured test execution output and reproduction transcripts.
  6. Repository guidelines and PR templates from `.github/PULL_REQUEST_TEMPLATE.md` and `docs/CONTRIBUTING.md`.
- **Eval mode**: The package bundle is the entire world. All facts come exclusively from the bundle text (`Repo facts`, `Issue`, `Thread highlights`, `Plan context`, and `Candidate PR`). Nothing is fetched from the network or GitHub, and no external files are read. `scope.md` and `voice-guide.md` are ignored entirely. Every check is evaluated with the full verdict rule.

## The scope seam (live mode only)

In live mode, read `scope.md` before performing any grading. The scope file identifies the authorized target repository and local house rules. If the repository line contains an unfilled placeholder (e.g. `<ORG>/<PATH-REVIEW-REPO>`), halt execution immediately and instruct the contributor to obtain the scoped repository link from the instructor. Refuse to grade pull requests targeting any repository outside the scoped Path Review repository. In eval mode, ignore `scope.md` completely.

## The voice seam (live mode only)

In live mode, read `voice-guide.md` to review the draft PR title and description against the contributor's communication guidelines and rules for upstream interaction. Report any guideline violations in the human-readable summary. The voice guide does not alter the binary accept/reject verdict unless a check in `rubric.md` explicitly references it. In eval mode, ignore `voice-guide.md` completely.

## Component reads

The tool executes its components according to the defined contract:
- `rubric.md` defines the evaluation checks and the binary verdict rule.
- `references/evidence-guide.md` maps where each evidence family resides and defines observable pass criteria.
- `procedure.md` provides the sequential operational steps that must be executed as written.
If `procedure.md` is silent on a particular situation, report the procedural gap rather than improvising unwritten steps. Under the refusal rule, if `rubric.md` or `procedure.md` lacks substantive content, refuse to grade and report the missing component.

## Verdict and output

The tool operates strictly in a binary verdict space: `accept` (ready to submit) or `reject` (hold). There are no intermediate or qualified verdicts.

The tool provides a human-readable summary of the evaluation findings, followed by the mandatory fenced JSON block. The reply must end with this fenced JSON block, valid and last, with no characters or commentary following it:

```json
{
  "item": "<PR URL or bundle id>",
  "checks": [
    {"name": "<check name>", "grade": "pass|fail|unclear",
     "evidence": "<one line: the fact or quote that decided it>"}
  ],
  "verdict": "accept|reject"
}
```

## Grading discipline

Every execution must adhere to these standing guarantees:

1. **Evidence first**: Every check grade must cite the specific fact, command output, or verbatim text that decided it. Unsubstantiated impressions or vague statements are never acceptable evidence.
2. **Grade the thing, not the polish**: Evaluate the technical substance of the diff, evidence, and compliance against the plan and repository requirements, not aesthetic length or rhetorical confidence.
3. **The rubric decides**: If an artifact satisfies the pass condition stated in `rubric.md`, it passes. If it violates the pass condition, it fails. Rubric definitions govern outcomes, not runtime intuition.
4. **The procedure decides how**: Follow the order and steps in `procedure.md` precisely.
5. **Unclear defaults to fail**: Any claim that cannot be verified from the package or gathered evidence receives `unclear`, which evaluates to `fail` under the verdict rule. An unverifiable PR is not ready to submit.

