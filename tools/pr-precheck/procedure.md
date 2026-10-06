# Procedure: how this tool grades a PR package

This procedure defines the systematic operational steps for evaluating a PR package. Execute each stage in sequence to produce deterministic, reproducible evaluations.

## Read order

Before grading any individual check, inspect the package components in this strict five-step order:

1. **Issue and Thread Highlights**:
   Read the reported issue title, description, and thread highlights. Note the specific defect, symptom, reproduction conditions, and any explicit direction from maintainers.
2. **Repo Facts**:
   Read the repository facts block. Extract all mandatory submission rules: required PR template sections, checklist items, documentation asks (e.g. changelog or whatsnew entries), and contribution policies (especially mandatory AI usage disclosure).
3. **Accepted Plan Context**:
   Read the accepted implementation plan and any recorded deviation notes. Note the exact scope boundaries, files intended to touch, explicit non-goals (out-of-scope items), and the planned test plan.
4. **Candidate PR Description and Commits**:
   Read the candidate PR title, description, and commit messages. Check whether required template sections and checklists are completed, whether AI disclosure is included when required, and whether the description claims fidelity or discloses planned shortfalls.
5. **Candidate PR Diff and Test Evidence**:
   Conduct a side-by-side review:
   - Compare the unified diff against the plan's scope and touched files.
   - Compare the test evidence section against the issue reproduction steps and the plan's test plan.

This sequence guarantees that repository requirements, plan boundaries, and defect targets are fully established before the code diff and evidence are judged.

## Evidence gathering

For each check defined in `rubric.md`, execute the specific evidence gathering move and record the findings:

1. **Standards Compliance (`standards-compliance`)**:
   - Check the repo facts for required template sections, checklists, and AI disclosure policies.
   - Inspect the candidate PR description to determine whether all template sections are filled, whether checklist boxes are checked, and whether the repository's stated AI disclosure rules are satisfied (all packages are treated as AI-assisted).
   - Record the exact missing section, unchecked item, or missing disclosure if any.
2. **Plan Fidelity (`plan-fidelity`)**:
   - Compare every file and hunk in the diff against the plan's scope boundary and touched files list.
   - Check whether the diff introduces unrequested new configuration options, CLI flags, renamings, or refactorings outside the plan.
   - If the diff does less than the plan (e.g. deferred edge case), check if an explicit deviation note was recorded in the plan and acknowledged in the PR description.
   - Compare description claims against the diff: verify that every claim in the description actually exists in the diff, and that claims of "exact plan implementation" are not contradicted by scope creep.
   - Record any unannounced scope additions, silent omissions, or inaccurate description claims.
3. **Test Evidence (`test-evidence`)**:
   - Locate the specific defect behavior from the issue and plan repro.
   - Check whether the PR test evidence demonstrates observable before-and-after proof on that exact defect scenario (rather than solely on an unaffected control path or unrelated test).
   - Check whether concrete commands and verifiable terminal outputs are shown, rather than bare assertions ("tested locally", "cargo test passes", "works on my machine" without output).
   - Record the missing defect before/after execution or bare unevidenced claim if any.
4. **Diff Quality (`diff-quality`)**:
   - Scan each hunk in the unified diff for debugging leftovers: temporary print/log statements (e.g. `eprintln`, `print`), commented-out code blocks, experimental snippets, dead functions (e.g. behind `allow(dead_code)`), or stray `TODO` comments.
   - Inspect the diff for unnecessary formatting churn, indentation changes, or import restructurings unrelated to the functional fix.
   - Review commit messages for scratch/WIP commits.
   - Record the exact line numbers or contents of any debris found.

## Check execution

Evaluate each rubric check against the gathered evidence in order:

1. Execute `standards-compliance`:
   - If a required checklist, template section, documentation entry, or mandatory AI disclosure is missing or ignored, grade `fail`. Quote the missing requirement in the evidence line.
   - Otherwise, grade `pass`.
2. Execute `plan-fidelity`:
   - If the diff contains unrequested scope (flags, settings, refactors) without an accepted plan deviation, or if the description claims changes not present in the diff or falsely claims exact adherence, grade `fail`. Quote the drifted hunk or false claim in the evidence line.
   - Otherwise, grade `pass`.
3. Execute `test-evidence`:
   - If test evidence is missing, shows only bare assertions without terminal outputs, or exercises only an unaffected control path while omitting the defect reproduction before/after, grade `fail`. Quote the missing repro proof in the evidence line.
   - Otherwise, grade `pass`.
4. Execute `diff-quality`:
   - If the diff contains debug prints, commented-out code, dead probe functions, or formatting churn, grade `fail`. Quote the debris line or construct in the evidence line.
   - Otherwise, grade `pass`.

If evidence for any check is genuinely absent from the package or cannot be verified, grade `fail` (or `unclear`, which evaluates to `fail`). Never assume or invent missing evidence.

## Verdict assembly

Assemble the final verdict according to the rubric's verdict rule:

1. Aggregate check grades:
   - If all required checks (`standards-compliance`, `plan-fidelity`, `test-evidence`, `diff-quality`) receive `pass`, the verdict is `accept`.
   - If one or more required checks receive `fail` or `unclear`, the verdict is `reject`.
2. Output construction:
   - Format a clear textual summary explaining the findings for each check.
   - If the verdict is `reject`, cite the first failing check in rubric order as the primary deciding check.
   - End the reply with the required fenced JSON block, valid and last, matching the schema from `CONTRACT.md` exactly, with no characters or commentary following it.

