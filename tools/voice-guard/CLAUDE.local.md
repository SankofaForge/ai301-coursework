# Repository Guidelines: README-Editor-skill

Local contributor memory and operational guide derived from CONTRIBUTING.md and ci.yml.

## Local Verification Commands

Run all checks locally before pushing or opening a PR:

- Unit tests: `python -m unittest discover -s tests -v`
- Script syntax compile: `python -m py_compile readme-forge/scripts/*.py readme-forge-design/scripts/*.py action/report.py`
- Analyze repo demo: `python readme-forge/scripts/analyze_repo.py demo/sample-app --compact`
- Import graph demo: `python readme-forge/scripts/import_graph.py demo/sample-app`
- Score project README: `python readme-forge/scripts/score_readme.py README.md --repo . --min 85`
- Verify project README: `python readme-forge/scripts/verify_readme.py README.md --repo . --min-accuracy 100`
- Score skill READMEs: `python readme-forge/scripts/score_readme.py readme-forge/README.md --min 85`

## Development Constraints & Conventions

- Standard Library Only: Python 3.8+ stdlib only; do not add external pip dependencies.
- Ground Truth: Never guess or invent facts; unverified claims must output TODO.
- Scope Discipline: Keep changes focused strictly on the assigned issue.
- Atomic Commits: Write imperative, conventional commits (`feat:`, `fix:`, `docs:`).
- Branching: Always branch from updated `main`; sync fork via `git fetch upstream && git rebase upstream/main`.
- Changelog: Add an entry to `CHANGELOG.md` under `## [Unreleased]` for user-facing changes.
