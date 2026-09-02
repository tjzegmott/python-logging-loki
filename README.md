# 🚀 tjzegmott-python-logging-loki

[![CI](https://github.com/tjzegmott/python-logging-loki/actions/workflows/continuous-integration.yml/badge.svg)](https://github.com/tjzegmott/python-logging-loki/actions/workflows/continuous-integration.yml)
[![PyPI version](https://badge.fury.io/py/logging_loki.svg)](https://badge.fury.io/py/logging_loki)
[![PyPI version](https://img.shields.io/pypi/v/tjzegmott-python-logging-loki.svg)](https://pypi.org/project/tjzegmott-python-logging-loki/)
[![codecov](https://codecov.io/gh/tjzegmott/python-logging-loki/branch/main/graph/badge.svg)](https://codecov.io/gh/tjzegmott/python-logging-loki)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Python](https://img.shields.io/badge/python-3.8.1+-blue.svg)](https://www.python.org/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![ty](https://img.shields.io/badge/type--checked-ty-blue?labelColor=orange)](https://github.com/astral-sh/ty)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/tjzegmott/python-logging-loki/blob/main/LICENSE)

Send Python logs directly to [Grafana Loki](https://grafana.com/loki) with minimal configuration.

|   What   |                            Where                            |
| :------: | :---------------------------------------------------------: |
|  Source  |     <https://github.com/tjzegmott/python-logging-loki>      |
|   PyPI   |         `pip install tjzegmott-python-logging-loki`         |
| Releases | <https://github.com/tjzegmott/python-logging-loki/releases> |

---

## ✨ Features

- 📤 **Direct Integration** - Send logs straight to Loki
- 🔐 **Authentication Support** - Basic auth and custom headers
- 🏷️ **Custom Labels** - Flexible tagging system
- ⚡ **Async Support** - Non-blocking queue handler included
- 🔒 **SSL Verification** - Configurable SSL/TLS settings
- 🎯 **Multi-tenant** - Support for Loki multi-tenancy

---

## 📦 Installation

```bash
pip install tjzegmott-python-logging-loki
```

Or using uv (recommended):

```bash
uv add logging_loki

```

---

## 🎯 Quick Start

### Basic Usage

```python
import logging
import logging_loki

handler = logging_loki.LokiHandler(
    url="https://loki.example.com/loki/api/v1/push",
    tags={"app": "my-application"},
    auth=("username", "password"),
    version="2"
)

logger = logging.getLogger("my-app")
logger.addHandler(handler)
logger.info("Application started", extra={"tags": {"env": "production"}})
```

### Async/Non-blocking Mode

For high-throughput applications, use the queue handler to avoid blocking:

```python
import logging.handlers
import logging_loki
from multiprocessing import Queue

handler = logging_loki.LokiQueueHandler(
    Queue(-1),
    url="https://loki.example.com/loki/api/v1/push",
    tags={"app": "my-application"},
    version="2"
)

logger = logging.getLogger("my-app")
logger.addHandler(handler)
logger.info("Non-blocking log message")
```

---

## ⚙️ Configuration Options

| Parameter    | Type    | Default    | Description                                   |
| ------------ | ------- | ---------- | --------------------------------------------- |
| `url`        | `str`   | _required_ | Loki push endpoint URL                        |
| `tags`       | `dict`  | `{}`       | Default labels for all logs                   |
| `auth`       | `tuple` | `None`     | Basic auth credentials `(username, password)` |
| `headers`    | `dict`  | `None`     | Custom HTTP headers (e.g., for multi-tenancy) |
| `version`    | `str`   | `"1"`      | Loki API version (`"0"`, `"1"`, or `"2"`)     |
| `verify_ssl` | `bool`  | `True`     | Enable/disable SSL certificate verification   |

---

## 🏷️ Labels

Logs are automatically labeled with:

- **severity** - Log level (INFO, ERROR, etc.)
- **logger** - Logger name
- **Custom tags** - From handler and `extra={"tags": {...}}`

```python
logger.error(
    "Database connection failed",
    extra={"tags": {"service": "api", "region": "us-east"}}
)
```

---

## 🔐 Multi-tenant Setup

```python
handler = logging_loki.LokiHandler(
    url="https://loki.example.com/loki/api/v1/push",
    headers={"X-Scope-OrgID": "tenant-1"},
    tags={"app": "my-app"}
)
```

---

## Development

### Prerequisites

- Python 3.8+
- [uv](https://docs.astral.sh/uv/) for package management

### Setup

```bash
git clone https://github.com/tjzegmott/python-logging-loki.git
cd python-logging-loki
make install
```

### Running Tests

```bash
make test

# With coverage
make test-cov

# Across all Python versions
make test-matrix
```

### Code Quality

```bash
# Run all checks (lint, format, type-check)
make verify

# Auto-fix lint and format issues
make fix
```

### Prek

```bash
prek install
prek run --all-files
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

Based on [python-logging-loki](https://github.com/GreyZmeem/python-logging-loki) by GreyZmeem.
