# Evidence guide: where proof lives in a reproduction package

The skill uses this guide as its reference map: for every kind of proof a rubric check names, this guide specifies where to find it in a package and what verifiable good looks like.

## Environment

### Where it lives
- **Eval mode**: The `Environment:` field or opening paragraph in the `Candidate repro report` section, compared directly against the `Issue` description and `Repo facts` block.
- **Live mode**: The environment line of the draft reproduction comment, compared against the issue body, system requirements, and repo documentation (e.g. `README.md`, `pyproject.toml`, or CI workflow configs).

### What good looks like
- The record explicitly lists the operating system and distribution/platform (e.g. macOS 15.0, Ubuntu 24.04, Fedora 42), the runtime or compiler version (e.g. Python 3.11, Rust 1.96, Go 1.21), the package or binary version under test (e.g. bat 0.26.1, minikube v1.38.1), and any relevant driver, browser, or configuration backend.
- If the test was run on a version or configuration differing from the original report (such as testing against `main` or the latest release), the version delta is explicitly acknowledged and explained.
- A report fails this check if it contains no environment details, omits critical platform/driver details on a platform-dependent issue, or silently tests an obsolete version without noting the mismatch.

## Steps

### Where it lives
- **Eval mode**: The numbered or formatted commands under `Steps:` in the `Candidate repro report`.
- **Live mode**: The reproduction procedure in the student's draft reproduction report.

### What good looks like
- The steps provide a complete, self-contained sequence from a clean starting state to the triggering command, using exact commands, scripts, or minimal configuration snippets.
- A stranger on a matching machine can execute the instructions verbatim without needing access to private corporate repositories, unshared local configs, unpublished credentials, or guessing missing flags.
- Any test input, configuration flag, or mock payload is provided inline or through standard accessible public resources.
- A report fails this check if it hand-waves setup ("set up the environment"), omits crucial CLI flags or drivers, or requires proprietary or private code that cannot be inspected or rerun.

## Behavior shown

### Where it lives
- **Eval mode**: The fenced code blocks, command terminal transcripts, logs, and error traces inside the `Candidate repro report`, evaluated directly against the error reported in the `Issue`.
- **Live mode**: The terminal output, stack traces, console logs, or screenshot attachments quoted in the draft repro comment, evaluated against the issue description.

### What good looks like
- The report includes raw, unedited command output, terminal logs, or error traces showing what actually occurred when executing the steps.
- The captured artifact shows the specific error, stack trace, or failure behavior reported in the issue (or, in an honest cannot-reproduce, shows the clean execution output of the triggering command).
- A report fails this check if it contains zero artifacts (pure assertion like "I reproduced this" or "confirmed reproducible"), shows only unrelated startup banners or healthy status messages without demonstrating the failure, or asserts a root cause (such as a race condition) without capturing any supporting trace.

## Honesty

### Where it lives
- **Eval mode**: The `Expected:` and `Actual:` sections and narrative discussion in the `Candidate repro report`, compared directly against the captured artifacts.
- **Live mode**: The summary and analysis in the draft repro comment, compared against the actual terminal output produced.

### What good looks like
- The narrative states faithfully and accurately what the captured artifacts demonstrate, without exaggeration, wishful thinking, or misleading spin.
- If the bug did not reproduce after diligent, documented attempts with matching configurations and control runs, the report honestly states "Could NOT reproduce" and details what was tried, what differed, and hypotheses for why. An honest, evidenced cannot-reproduce passes.
- A report fails this check if it claims a crash when the artifact shows only an argument-validation error, syntax error, or active running process, or if it claims to have reproduced an issue while showing artifacts from an unrelated failure mode.

## Comms

### Where it lives
- **Eval mode**: The `Candidate claim comment` and `Candidate repro report`, compared against the issue description and the `Repo facts` block (specifically `bug reports:` template requirements and `contribution policy:` including AI usage rules).
- **Live mode**: The student's draft claim comment and reproduction comment, compared against the live issue thread, repository `CONTRIBUTING.md`, `README.md`, issue templates, and AI disclosure guidelines.

### What good looks like
- The claim comment specifically references the issue's technical details (e.g. naming the relevant files, functions, or specific error) and states concrete next steps for investigation rather than using generic, interchangeable boilerplate ("Please assign me this issue", "guaranteed fix in 2 days").
- The claim promises only the next investigation or verification step, not a guaranteed fix or an arbitrary completion deadline.
- When the repository's stated contribution policy mandates disclosing AI assistance (such as Ghostty's policy requiring all AI usage to be disclosed with tool and extent, or p5.js's policy), the candidate comments must explicitly include that disclosure. Candidate packages are evaluated as AI-assisted work: if a repository policy mandates AI disclosure, silence or absence of disclosure fails this check.
- A package fails this check if the claim is generic spam/boilerplate, makes unfulfillable promises, or violates repository contribution policies by omitting mandatory AI disclosures.
