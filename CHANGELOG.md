# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.1] - 2026-09-02

### Added
- Flask web app factory with a `/health` endpoint
- CLI via argparse, including a `serve` subcommand to start the development server
  (`uv run aicreators serve --dev --port 5001`)
- Dark dashboard shell with sidebar navigation and stub pages for the content pipeline

## [0.1.0] - 2026-09-02

### Added
- Initial project scaffolding for AICreators
- MIT license (`LICENSE.txt`)
- README with project overview, contribution link, and license notes
- Contribution guide (`CONTRIBUTING.md`) with GitHub/GitLab workflow guidance
- `pyproject.toml` packaging with Hatchling, Python 3.14, and Ruff configuration
- `aicreators` package with a `main` CLI entry point stub
- `.gitignore` and `uv.lock` for local development with uv
