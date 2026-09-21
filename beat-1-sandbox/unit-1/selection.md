# Unit 1 — Issue Selection

Path: `beat-1-sandbox/unit-1/selection.md`

Record of the issue carried into Unit 2, and of the evaluation runs that produced
`eval-run.txt`. This file is graded at the path above; a copy kept anywhere else in
the repository is not read.

Complete every labelled field below. Each is graded on its own; content placed under the
wrong label is not graded.

---

## Selected issue

**Issue link**

Issue #69: [Output parser crashes on a top-level JSON array fallback](https://github.com/codepath/pathreview-ai301-fa26-s3/issues/69)

**Verdict output**

The direct live-mode review ranked three current Path Review candidates. It selected
The live-mode review using Claude Code ranked three current Path Review candidates. It selected
issue #69 because it best matches the fit profile: Python, retrieval-augmented
generation, and a focused behavior-plus-test change. The repository was active on
2026-09-20, with `archived: false` and a latest push on 2026-09-16. The contributor
guide contains no AI-contribution restriction. Path Review's house rule says to
ignore other students' claim comments when grading availability.

Ranked accepted candidates:

1. Issue #69: the parser bug is concrete, the affected implementation and test files
   are named, and the estimate is 2–4 hours.
2. Issue #68: the empty-index bug is similarly bounded, but it is a lower fit than
   #69 for my interest in AI-backed application behavior.
3. Issue #73: the documentation mismatch is the smallest task, but it offers less
   practice with Python tests and service behavior.

**The verdict must record `accept` for this issue.** Choose an issue your own skill
accepts. If your skill rejects every candidate you try, that is a signal about your
rubric rather than about the issues: revise it and re-run — retries are unlimited and a
partial re-run costs about $0.20 — or run the skill on different candidates. Output
recording `reject` for the issue you chose earns no credit for this field.

```json
[
  {
    "item": "https://github.com/codepath/pathreview-ai301-fa26-s3/issues/69",
    "checks": [
      {
        "name": "Active repository",
        "grade": "pass",
        "evidence": "The repository is not archived and its latest push was 2026-09-16, four days before the 2026-09-20 live review."
      },
      {
        "name": "Bounded first-issue scope",
        "grade": "pass",
        "evidence": "The issue names one parser failure, two relevant files, removal of one xfail marker, and a 2–4 hour estimate."
      },
      {
        "name": "No active claim",
        "grade": "pass",
        "evidence": "No assignee or linked pull request is listed; student claim comments are ignored under the Path Review house rule."
      },
      {
        "name": "AI-compatible contribution policy",
        "grade": "pass",
        "evidence": "The repository contributor guide contains no statement that bans AI-assisted contributions."
      },
      {
        "name": "Maintainer response signal",
        "grade": "unclear",
        "evidence": "The current thread has no maintainer response, and no five-issue response sample was available in the live evidence."
      }
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/codepath/pathreview-ai301-fa26-s3/issues/68",
    "checks": [
      {
        "name": "Active repository",
        "grade": "pass",
        "evidence": "The repository is not archived and its latest push was 2026-09-16, four days before the 2026-09-20 live review."
      },
      {
        "name": "Bounded first-issue scope",
        "grade": "pass",
        "evidence": "The issue names one empty-index failure, two relevant files, removal of one xfail marker, and a 2–4 hour estimate."
      },
      {
        "name": "No active claim",
        "grade": "pass",
        "evidence": "No assignee or linked pull request is listed; the student claim comment is ignored under the Path Review house rule."
      },
      {
        "name": "AI-compatible contribution policy",
        "grade": "pass",
        "evidence": "The repository contributor guide contains no statement that bans AI-assisted contributions."
      },
      {
        "name": "Maintainer response signal",
        "grade": "unclear",
        "evidence": "The current thread has no maintainer response, and no five-issue response sample was available in the live evidence."
      }
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/codepath/pathreview-ai301-fa26-s3/issues/73",
    "checks": [
      {
        "name": "Active repository",
        "grade": "pass",
        "evidence": "The repository is not archived and its latest push was 2026-09-16, four days before the 2026-09-20 live review."
      },
      {
        "name": "Bounded first-issue scope",
        "grade": "pass",
        "evidence": "The issue limits the work to reconciling README.md and .env.example and estimates 1–2 hours."
      },
      {
        "name": "No active claim",
        "grade": "pass",
        "evidence": "No assignee, linked pull request, or claim comment is listed."
      },
      {
        "name": "AI-compatible contribution policy",
        "grade": "pass",
        "evidence": "The repository contributor guide contains no statement that bans AI-assisted contributions."
      },
      {
        "name": "Maintainer response signal",
        "grade": "unclear",
        "evidence": "The current thread has no maintainer response, and no five-issue response sample was available in the live evidence."
      }
    ],
    "verdict": "accept"
  }
]
```

---

## Eval iterations

Quote source text directly in each field below. Paraphrase does not satisfy them.

**Run history**

Claude Code eval run (claude-3-7-sonnet), one full pass: **20/20**. The score matches the agreement line
in `eval-run.txt`.

**Issue analysis**

For `issue-12`, my rubric returns **reject**, and the gold label is **reject**. The
bundle quotes BookWyrm's policy: “We do not accept AI-generated code or documentation.”
That fails the required AI-compatible contribution policy. The issue is otherwise
bounded, but it is not a viable first contribution for this course workflow.

**Check rationale**

> Pass when there is no assignee, no open linked PR, and no maintainer-confirmed current
> claim in the thread. A closed or merged linked PR alone does not fail. In live Path
> Review mode, follow `scope.md` and ignore other students' claim comments.

I wrote this check to separate active work from abandoned history. It rejects issues
with an assignee, an open linked pull request, or a maintainer-confirmed claim. It
keeps issues with only closed or merged attempts available, and it follows the course
rule that classmates' claims do not block a Path Review issue.

**Trade-offs**

The check can accept an issue that another student has started because it ignores
student claim comments in the Path Review repository. That is intentional: the course
house rule says shared claims are allowed, and credit attaches to the pull request.
The check still blocks an assignee, an open linked pull request, or a maintainer's
current claim, so formal ownership remains visible.

---

## Selection rationale

Graded on whether all three are answered, in your own words. Not on how good the
reasoning is, and not on length — a short honest answer to each earns the full marks.
This is also the basis for the claim comment you write in Unit 2.

**Selection rationale**

1. Issue #69 fits my interest in Python services, AI-backed behavior, and focused tests.
   Its stated 2–4 hour estimate fits the time available for a first contribution.

2. The verdict correctly identified a concrete failure, named the parser and test
   files, and required the existing xfail marker to be removed. I also weighed the
   seeded-test workflow and the two current student claim comments, which the rubric
   cannot use as blocking signals because of the Path Review house rule.

3. The main difficulty will be claiming it early enough to coordinate with the other
   interested students. The technical change should stay contained, but I will need to
   understand the parser's fallback contract before changing the test and implementation.

---

Related paths: `eval-run.txt` in this directory; your skill's files in
`tools/issue-select/`.
