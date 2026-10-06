# Unit 4 — Test and Submit

Path: `beat-1-sandbox/unit-4/pull-request.md`

Record of the pull request you opened against the Path Review repo, and of the evaluation
runs that produced `eval-run.txt`. This file is graded at the path above; a copy kept
anywhere else in the repository is not read.

Complete every labelled field below. Each is graded on its own; content placed under the wrong
label is not graded.

---

## Your pull request

**Pull request**

https://github.com/codepath/pathreview-ai301-fa26-s3/pull/101

**Branch**

fix/69-json-array-fallback

## Eval iterations

Answer all four sections. Quote source text directly; paraphrase does not satisfy these
fields.

**Run history**

Evaluation run 1 (initial full run with 20 scored packages): **19/20** (clear-accept 6/7, not-tested 4/4, silent-drift 4/4, standards-wall 2/2, unreviewable 3/3; bar: 18/20: PASS). Package `pkg-11` failed on `standards-compliance` because our initial check strictly demanded naming the specific tool used, whereas ripgrep's contribution policy only required disclosing that AI was used with human comprehension and in the author's own words.

Canary run on `pkg-11`, `pkg-20`, `pkg-01`: **3/3** agreement after clarifying that the disclosure must satisfy the repository's stated disclosure rules.

Evaluation run 2 (confirming full run with 20 scored packages saved to `eval-run.txt`): **20/20** (clear-accept 7/7, not-tested 4/4, silent-drift 4/4, standards-wall 2/2, unreviewable 3/3; bar: 18/20: PASS). The last score matches the agreement line in `eval-run.txt`: `agreement: 20/20 scored items  (bar: 18/20: PASS)`.

**Package analysis**

For `pkg-20`, my rubric recorded **reject**, and the gold label is **reject**. The package bundles ghostty-org/ghostty#13604, where terminal emulator query responses (`CSI ? 996 n`) fail to reflect theme changes under single non-conditional themes. The candidate PR provides an accurate code patch in `src/config/Config.zig` implementing the maintainer's diagnosis with decisive before/after test evidence. However, Ghostty's stated repository contribution policy (`CONTRIBUTING.md` + `AI_POLICY.md` recorded in the Repo facts) strictly mandates: "All AI usage in any form must be disclosed, stating the tool used and the extent of the assistance; the human in the loop must fully understand the work; AI-assisted issues and comments must be reviewed and edited by a human before submission". The candidate PR description contains no AI-use disclosure whatsoever. Per the contract's rule that all eval packages represent AI-assisted work, my rubric's `standards-compliance` check evaluated the PR description against the repository's stated policy, identified the complete omission of the mandatory AI disclosure, graded `standards-compliance` as `fail`, and correctly reached the `reject` verdict, satisfying the category floor for `standards-wall`.

**Check rationale**

> | standards-compliance | Candidate PR description, title, and diff read against the repo facts block's PR template asks, checklist items, and contribution policies (including AI disclosure). | All required PR template sections, checklist items, and mandatory documentation entries (such as whatsnew or changelog updates) specified by the repository are present and substantively completed. If the repository policy requires AI usage disclosure (all packages being AI-assisted), the PR description satisfies the repository's stated disclosure rules (disclosing AI assistance and confirming human understanding or naming the tool as required by that repo). | required |

I authored and refined this check to evaluate repository-specific standards compliance rather than imposing an artificial, uniform disclosure format across diverse projects. In our initial draft, the pass condition required "naming the tool used and the nature of assistance". While that matched strict policies like Ghostty's (`pkg-20`), it incorrectly failed ripgrep (`pkg-11`), where BurntSushi's stated policy welcomes AI assistance as long as comments are in the contributor's own words and the author understands the code, which the author explicitly affirmed without citing a specific tool name. Conversely, projects like pandas (`pkg-01`) enforce mandatory issue-closing syntax, comprehensive PR checklists, and release documentation (`whatsnew`) entries that casual contributors often skip. By conditioning pass criteria strictly on satisfying the repository's own stated template asks, checklist items, and specific AI policy rules, the check reliably separates compliant PRs from those that ignore maintainer instructions.

**Trade-offs**

Every check gives something up. A trade-off of framing `standards-compliance` around repository-specific policy text is that it requires evaluating semantic policy compliance in context rather than enforcing a rigid keyword pattern (such as requiring a literal model name). On canary re-run with `--only pkg-11,pkg-20,pkg-01`, this refined check flipped `pkg-11` from reject to accept while maintaining necessary rigor on `pkg-01` (where pandas' required checklist and whatsnew documentation entry were omitted) and `pkg-20` (where Ghostty's mandatory disclosure was completely missing). A second trade-off is that in repositories without an explicit AI policy, an unstated AI contribution is not penalized by this check alone, keeping focus on repository-stated constraints.

---

Related paths: `eval-run.txt` in this directory; your skill's files in
`tools/pr-precheck/`.
