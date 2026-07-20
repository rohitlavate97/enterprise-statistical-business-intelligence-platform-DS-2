# Architecture — Directory Layout

This project is organized as a set of top-level, independently importable Python packages
rather than one wrapping package, matching the structure fixed in the master prompt:

| Package | Responsibility |
|---|---|
| `config/` | Pydantic Settings + YAML configuration management |
| `core/` | Shared domain types, seeded RNG utilities, cross-cutting infrastructure |
| `analytics/` | Business analytics (KPIs, rankings) |
| `statistics/` | Statistical layer: `tests/` (hypothesis test implementations), `assumptions/` (assumption-checking utilities), `experiments/` (A/B testing framework) |
| `forecasting/` | Time series decomposition, ARIMA/SARIMA, exponential smoothing, walk-forward validation |
| `streaming/` | Simulated live feed, online (Welford's) statistics, streaming anomaly detection |
| `visualization/` | Plotly dashboards and chart builders |
| `services/` | Application/orchestration layer wiring the modules above together |
| `pipelines/` | Data loading, validation, and cleaning (Polars) |
| `tests/` | Cross-cutting/integration tests; each package also owns tests close to its own code where noted above |

## Why this shape

- **Flat top-level packages, no wrapper package.** Keeps import paths short (`from statistics.assumptions import normality`) and matches the structure specified for this project. Each directory is independently a Python package (`__init__.py` present).
- **`statistics/` shadows the stdlib `statistics` module.** Because these packages are imported by absolute path from the repo root (not nested under a project-wide package), any code that does `import statistics` from within this repo will resolve to *this* package, not the standard library one. This is a deliberate accepted trade-off to match the required structure; anywhere the stdlib `statistics` module is actually needed, it must be imported via `importlib` or aliased explicitly to avoid confusion.
- **pytest `--import-mode=importlib`** is set in `pyproject.toml` because multiple packages (e.g. `statistics/tests/`, top-level `tests/`) can otherwise collide under pytest's default `prepend` import mode when test module basenames repeat across directories.
