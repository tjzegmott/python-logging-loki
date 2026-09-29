# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `suppress_errors` option on `LokiHandler`/`LokiQueueHandler` to silently swallow
  delivery failures (e.g. connection errors or non-2xx Loki responses) instead of
  printing the standard logging `--- Logging error ---` traceback to stderr.
- Initial project structure
- Basic package setup with logging_loki
- GitHub Actions CI/CD pipelines
- Prek hooks for code quality
