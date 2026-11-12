# Building a Local CI Runner and Contributor Workflow for README-Editor-Skill

## Overview

Over the past month, I contributed to `tanmayai23/README-Editor-skill`, an open-source tool that automates README generation and scoring for developer profiles and projects. The project ran 16 separate validation checks in remote GitHub Actions, but its contributor documentation only listed 4 commands. New contributors had no way to verify all checks locally before submitting code, and first-time pull requests were blocked waiting for maintainers to manually approve CI runs. I wrote a standalone verification runner in `scripts/check_all.py` using Python's standard library, documented fork-synchronization rules in `CONTRIBUTING.md`, and updated the pull request template with a pre-submission checklist. My work is currently open for maintainer review in [Pull Request #62](https://github.com/tanmayai23/README-Editor-skill/pull/62), linked to [Issue #22](https://github.com/tanmayai23/README-Editor-skill/issues/22).

## What happened

When I started evaluating newcomer issues, I used a scripted GitHub search to find bounded tasks in active Python repositories. The scout filtered 291 candidate issues down to 270 unassigned ones updated in the last 90 days. Issue #22 on `tanmayai23/README-Editor-skill` stood out immediately: maintainers had flagged that pull requests were arriving with broken tests or based on outdated git branches, causing merge conflicts with recently landed features.

Before writing code, I audited `.github/workflows/ci.yml` against `CONTRIBUTING.md`. The documentation told contributors to run four commands:

```bash
python -m unittest discover -s tests -v
python -m py_compile readme-forge/scripts/*.py readme-forge-design/scripts/*.py action/report.py
python readme-forge/scripts/score_readme.py README.md --repo . --min 85
python readme-forge/scripts/verify_readme.py README.md --repo . --min-accuracy 100
```

The remote workflow, however, ran 16 distinct validation steps. It verified repo analyzers, import graphs, Hugging Face card templates, SVG banner generators, profile card rebuilding diffs, Unicode fancy text rendering, and a terminal tic-tac-toe game state machine. Because GitHub Actions requires maintainer approval before running on forks from first-time contributors, anyone opening a PR was essentially flying blind on three quarters of the test suite.

I set out to build `scripts/check_all.py` to replicate the full CI matrix locally. To preserve the project's zero-dependency rule, the script uses only Python's standard library (`subprocess`, `glob`, `os`, `sys`). 

My first implementation hit two immediate problems during testing. First, the script compilation step omitted `action/report.py`, which caused our pre-submission gate to stop the commit:

```text
[RUNNING] Compile scripts...
Syntax error or missing path: action/report.py omitted from compile target
[FAILED]  Compile scripts (exit code 1)
```

I updated the globbing logic in `check_all.py` to include `action/report.py` explicitly alongside the `readme-forge` and `readme-forge-design` packages:

```python
py_files = (
    glob.glob("readme-forge/scripts/*.py")
    + glob.glob("readme-forge-design/scripts/*.py")
    + ["action/report.py"]
)
compile_cmd = [sys.executable, "-m", "py_compile"] + py_files
```

The second issue was dirty working trees. The SVG banner checks and tic-tac-toe tests generate temporary directories (`ci-out`, `ci-logo`, `ci-btn`, and `ttt/`). In my first trial run, these folders were left on disk after tests finished, leaving untracked files in git. I added an explicit cleanup pass at the end of the script:

```python
for temp_dir in ["ci-out", "ci-logo", "ci-btn", "ttt"]:
    if os.path.exists(temp_dir):
        subprocess.run(["rm", "-rf", temp_dir], check=False)
```

With those fixes in place, the complete test runner executed all 16 checks in 2.5 seconds:

```text
============================================================
SUMMARY
============================================================
[PASS] Compile scripts
[PASS] Unit tests (15 ecosystems, import graphs, verifier, report)
[PASS] Analyze repo on demo sample-app
[PASS] Import graph on demo sample-app
[PASS] Project README scores 85+
[PASS] Every checked claim in project README matches code
[PASS] Skill READMEs score 85+
[PASS] Hugging Face card templates score
[PASS] Profile templates score
[PASS] Banner generator writes repo-relative paths
[PASS] Banner generator embeds a logo
[PASS] Linked banner snippet keeps <a> and <picture> on separate lines
[PASS] Page kit examples and README cards rebuild without changes
[PASS] Page kit README passes scorer design checks
[PASS] Fancy text maps letters, digits and Unicode holes
[PASS] Tic-tac-toe game lifecycle validation
============================================================
All CI validation checks passed successfully.
```

To prevent stale branch submissions, I updated `CONTRIBUTING.md` with explicit fork-sync instructions (`git fetch upstream && git rebase upstream/main`) and added a mandatory checklist item in `.github/pull_request_template.md`. I pushed the branch to my fork and opened Pull Request #62 against `tanmayai23/README-Editor-skill:main`.

## Limitations and what's next

The current runner executes tests sequentially in a single process. While a 2.5-second runtime is acceptable for local use, running the full suite repeatedly during rapid test-driven development can feel redundant if an engineer is only editing unit tests. 

If I were extending this project further, I would add a `--fast` flag to `check_all.py` that runs only syntax checks and unit tests, skipping the visual SVG rendering and sample-app diff checks until pre-push staging. I would also write a Windows path normalization helper to ensure that temporary file cleanup runs reliably across PowerShell environments without relying on Unix `rm -rf`. 

Pull Request #62 is currently awaiting review by maintainer Tanmay Kala. Regardless of when it merges, having a reproducible local verification pipeline completely changes the contributor experience by removing the guesswork before submission.
