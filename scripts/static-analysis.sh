#!/bin/bash
set -e

echo "Running mypy..."
mypy

echo "Running bandit..."
bandit -c pyproject.toml -r realtime_over_websockets

echo "Running semgrep..."
semgrep scan --config auto --error
