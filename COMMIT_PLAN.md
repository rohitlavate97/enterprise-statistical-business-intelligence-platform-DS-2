# Commit-Wise Development Plan
*(derived from `statistical-bi-platform-master-prompt-v2.md` — Git & Commit-Wise Development section)*

This document expands the 15-phase roadmap into concrete branches → commits → PR/tag
checkpoints, so progress can be tracked commit-by-commit against the master prompt's rules.

**How to read this doc:** each phase = one feature branch = one PR into `main`. Each commit
inside a phase is sequential, atomic, and must leave the repo in a working state (per the
Definition of Done). Nothing skips ahead to a future phase's code.

---

## Legend

- `feat` / `fix` / `refactor` / `docs` / `test` / `chore` / `perf` / `ci` — Conventional Commit type
- **Branch** — `phase-<number>-<short-name>`
- **Tag** — applied to `main` after PR merge + approval
- Every commit implicitly includes: tests for its scope, doc updates, manual verification steps,
  and a stop-and-review checkpoint (per master prompt rule #8 and the Per-Commit Process).

---

## Phase 1 — Project Setup
**Branch:** `phase-01-project-setup` · **Tag:** `v0.0-project-setup`

| # | Type | Commit | Objective |
|---|------|--------|-----------|
| 1 | chore | init repo structure & `pyproject.toml` | Scaffold `config/ core/ analytics/ statistics/ forecasting/ streaming/ visualization/ services/ pipelines/ tests/ docs/ assets/ scripts/ docker/ .github/` |
| 2 | chore | pre-commit hooks | Ruff, Black, MyPy wired to mirror CI |
| 3 | ci | GitHub Actions skeleton | lint + type-check + test on push/PR |
| 4 | chore | Dockerfile + docker-compose.yml | Base dev/runtime image |
| 5 | docs | README + branching convention + CHANGELOG.md init | Document `main`/`phase-*` workflow |

---

## Phase 2 — Synthetic Dataset Generator
**Branch:** `phase-02-synthetic-data-generator` · **Tag:** `v0.1-data-pipeline` (shared with Phase 3)

| # | Type | Commit | Objective |
|---|------|--------|-----------|
| 1 | feat | seeded RNG core + config | Central seed management for reproducibility |
| 2 | feat | dimension tables | Customers, Products, Stores, Employees |
| 3 | feat | calendar tables | Holiday calendar, Weather, seasonal patterns |
| 4 | feat | transactional tables | Orders/Daily Transactions with engineered promotion + weather effects |
| 5 | feat | remaining tables | Marketing Campaigns, Discounts, Returns, Inventory, Promotions |
| 6 | docs | data-generating process doc | Document true relationships & effect sizes (ground truth) |
| 7 | test | generator reproducibility tests | Same seed → identical output; schema/row-count checks |

---

## Phase 3 — Data Pipeline
**Branch:** `phase-03-data-pipeline` · **Tag:** `v0.1-data-pipeline`

| # | Type | Commit | Objective |
|---|------|--------|-----------|
| 1 | feat | Polars LazyFrame loaders | Ingest synthetic tables, inspect query plans |
| 2 | feat | validation & cleaning pipeline | Schema checks, null handling, dedup |
| 3 | perf | Polars vs Pandas benchmark suite | Time + memory, real operations, real scale |
| 4 | docs | benchmark results write-up | Honest trade-offs, incl. where Pandas wins |

---

## Phase 4 — Descriptive Statistics & Assumption-Checking
**Branch:** `phase-04-assumption-checking` · **Tag:** `v0.2-descriptive-stats`

| # | Type | Commit | Objective |
|---|------|--------|-----------|
| 1 | feat | descriptive statistics module | Central tendency, dispersion, distributions |
| 2 | feat | normality tests | Shapiro-Wilk, Kolmogorov-Smirnov |
| 3 | feat | variance homogeneity + correlation selector | Levene's test; Pearson vs Spearman decision logic |
| 4 | test | assumption-check validation | Correct flagging on known normal/non-normal fixtures |

---

## Phase 5 — Hypothesis Testing Module
**Branch:** `phase-05-hypothesis-testing-module` · **Tag:** `v0.4-hypothesis-testing`

| # | Type | Commit | Objective |
|---|------|--------|-----------|
| 1 | feat | t-test module | Independent/paired, with Mann-Whitney/Wilcoxon fallback |
| 2 | feat | ANOVA module | + Kruskal-Wallis fallback, post-hoc correction |
| 3 | feat | chi-square module | Expected-frequency < 5 flagging |
| 4 | feat | multiple-comparison correction | Bonferroni, Benjamini-Hochberg utilities |
| 5 | test | ground-truth validation | Detect known injected effects; false-positive rate ≤ nominal alpha across simulated trials |

---

## Phase 6 — A/B Testing Framework
**Branch:** `phase-06-ab-testing-framework` · **Tag:** `v0.5-ab-testing`

| # | Type | Commit | Objective |
|---|------|--------|-----------|
| 1 | feat | power analysis & sample-size calculator | Pre-registered MDE, computed before results |
| 2 | feat | test-selection engine | Chooses test by metric distribution |
| 3 | feat | experiment reporting | Multi-metric correction, correct CI framing |
| 4 | feat | experiment dashboard data layer | Feeds Plotly experiment dashboard (Phase 12) |
| 5 | test | framework validation | Verified against generator's known effect sizes |

---

## Phase 7 — Regression Module
**Branch:** `phase-07-regression-module` · **Tag:** `v0.6-regression`

| # | Type | Commit | Objective |
|---|------|--------|-----------|
| 1 | feat | OLS regression | Residual analysis, Q-Q, Durbin-Watson, heteroskedasticity |
| 2 | feat | multiple regression | VIF/multicollinearity checks |
| 3 | feat | logistic regression | Diagnostics appropriate to classification |
| 4 | test | regression tests | vs. hand-computed/fixture expected values |

---

## Phase 8 — Time Series & Forecasting
**Branch:** `phase-08-forecasting-module` · **Tag:** `v0.7-forecasting`

| # | Type | Commit | Objective |
|---|------|--------|-----------|
| 1 | feat | decomposition | Trend/seasonality (STL or classical) |
| 2 | feat | chronological split utility | No-lookahead train/test splitting, walk-forward scaffold |
| 3 | feat | ARIMA/SARIMA | Walk-forward validation |
| 4 | feat | exponential smoothing | Holt-Winters variants |
| 5 | feat | evaluation + intervals | MAE/RMSE/MAPE, confidence/prediction intervals, AIC/BIC model comparison |
| 6 | test | lookahead-bias tests | Assert no future data leaks into training at any fold |

---

## Phase 9 — Real-Time/Streaming Statistics
**Branch:** `phase-09-streaming-statistics` · **Tag:** `v0.8-streaming`

| # | Type | Commit | Objective |
|---|------|--------|-----------|
| 1 | feat | simulated live transaction feed | Background generator, defined emission rate |
| 2 | feat | online statistics | Welford's algorithm for streaming mean/variance |
| 3 | feat | streaming anomaly detection | Z-score / EWMA control-chart flagging |
| 4 | feat | live dashboard data panel | Short-interval refresh, separated from batch dashboards |
| 5 | docs | honest scope note | "Near-real-time simulation" caveat + what real Kafka/stream engine would add |
| 6 | test | streaming vs batch equivalence | Incremental result matches full recompute within float tolerance |

---

## Phase 10 — Business Analytics Module
**Branch:** `phase-10-business-analytics` · **Tag:** `v0.9-business-analytics`

| # | Type | Commit | Objective |
|---|------|--------|-----------|
| 1 | feat | core KPIs | Revenue, Profit, Margin, AOV, Retention, CLV, Repeat Rate, Conversion Rate |
| 2 | feat | sample-size-aware ranking | Store/Regional ranking with caveats (small-n guard) |
| 3 | feat | inventory & risk indicators | Turnover, risk metrics |
| 4 | test | KPI validation | Hand-calculated expected values on fixtures |

---

## Phase 11 — Advanced Analytics
**Branch:** `phase-11-advanced-analytics` · **Tag:** `v0.95-advanced-analytics`

| # | Type | Commit | Objective |
|---|------|--------|-----------|
| 1 | feat | RFM & segmentation | Customer Segmentation, RFM Analysis |
| 2 | feat | ABC/Pareto analysis | |
| 3 | feat | price sensitivity analysis | |
| 4 | feat | promotion impact | Quasi-experimental methodology (not naive before/after) |
| 5 | feat | store performance analysis | |
| 6 | test | advanced analytics validation | Against known ground-truth relationships |

---

## Phase 12 — Visualization Layer
**Branch:** `phase-12-visualization-layer` · **Tag:** `v0.97-visualization`

| # | Type | Commit | Objective |
|---|------|--------|-----------|
| 1 | feat | Plotly theme & base utilities | Dark theme, export, shared chart building blocks |
| 2 | feat | Executive + Revenue dashboards | |
| 3 | feat | Forecast + Statistical dashboards | CI bands, residual plots, decomposition views |
| 4 | feat | Correlation + Experiment dashboards | A/B results with visualized CIs |
| 5 | feat | interactivity + captions | Filters, drill-down, cross-filtering; plain-language interpretation captions |
| 6 | test | chart smoke tests | All chart functions return valid figures on fixtures |

---

## Phase 13 — Testing Hardening
**Branch:** `phase-13-testing-hardening` · **Tag:** `v0.99-test-hardening`

| # | Type | Commit | Objective |
|---|------|--------|-----------|
| 1 | test | close ground-truth validation gaps | Any module missing ground-truth checks gets them |
| 2 | test | coverage closure | Full coverage pass on statistics/forecasting modules |

---

## Phase 14 — Documentation & Interview Preparation
**Branch:** `phase-14-documentation` · **Tag:** `v1.0-rc-docs`

| # | Type | Commit | Objective |
|---|------|--------|-----------|
| 1 | docs | Statistical Methodology doc | Every test, its assumptions, how checked |
| 2 | docs | Business Assumptions doc | Every KPI formula + where it could mislead |
| 3 | docs | Architecture + Data Flow diagrams | |
| 4 | docs | Performance Benchmarks doc | Consolidated from Phase 3/others |
| 5 | docs | Interview Preparation doc | Polars vs Pandas, SciPy vs Statsmodels vs Scikit-Learn, assumptions, pitfalls, Q&A |

---

## Phase 15 — Final Production Polish
**Branch:** `phase-15-production-hardening` · **Tag:** `v1.0-production-hardening`

| # | Type | Commit | Objective |
|---|------|--------|-----------|
| 1 | perf | performance pass | Profiling + optimization across modules |
| 2 | ci | CI green end-to-end | Full pipeline passes clean |
| 3 | docs | deployment guide | |
| 4 | chore | v1.0 tag prep | Final review, changelog finalization |

---

## Checkpoints Recap (from master prompt rules)

- Every commit → local commit, then `git push origin phase-<number>-<short-name>`
- End of phase → PR into `main` (summary, methodology, benchmark/validation results, test evidence) → wait for explicit approval → merge → tag
- `CHANGELOG.md` updated continuously, not just at phase end
- No phase starts before the previous phase's Definition of Done is fully checked off
