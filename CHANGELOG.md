# Changelog

All notable changes to this project are documented in this file, in commit order,
grouped by phase branch.

## phase-01-project-setup

### commit 1 — chore: init repo structure & pyproject.toml
- Scaffolded top-level package layout: `config/ core/ analytics/ statistics/ forecasting/ streaming/ visualization/ services/ pipelines/`, with `statistics/` split into `tests/ assumptions/ experiments/` subpackages.
- Added `pyproject.toml` (setuptools build backend, runtime deps: Polars, Plotly, SciPy, Statsmodels, NumPy, Pandas, Pydantic/Pydantic Settings, PyYAML; dev deps: Pytest, Ruff, Black, MyPy, pre-commit).
- Added `.gitignore` excluding generated datasets, `.env`, virtual environments, and build artifacts.
- Added `docs/architecture.md` describing the directory layout.
- Added `tests/test_project_structure.py` as a scaffolding smoke test.

### commit 2 — chore: pre-commit hooks
- Added `.pre-commit-config.yaml` to wire up `ruff`, `black`, and `mypy` to mirror CI.
- Configured hooks for trailing whitespace, end-of-file fixer, yaml checks, and large files.
