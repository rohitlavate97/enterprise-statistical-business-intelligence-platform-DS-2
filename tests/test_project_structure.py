"""Scaffolding smoke test for phase-01 commit 1: verifies the top-level
package layout is importable before any real logic is added to it."""

import importlib

import pytest

TOP_LEVEL_PACKAGES = [
    "config",
    "core",
    "analytics",
    "statistics",
    "forecasting",
    "streaming",
    "visualization",
    "services",
    "pipelines",
]

STATISTICS_SUBPACKAGES = [
    "statistics.tests",
    "statistics.assumptions",
    "statistics.experiments",
]


@pytest.mark.parametrize("package_name", TOP_LEVEL_PACKAGES)
def test_top_level_package_imports(package_name):
    module = importlib.import_module(package_name)
    assert module is not None


@pytest.mark.parametrize("package_name", STATISTICS_SUBPACKAGES)
def test_statistics_subpackage_imports(package_name):
    module = importlib.import_module(package_name)
    assert module is not None
