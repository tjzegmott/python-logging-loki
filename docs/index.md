# tjzegmott-python-logging-loki

Python logging handler for Grafana Loki

## Installation

Install using pip:

```bash
pip install logging_loki
```

Or using uv (recommended):

```bash
uv add logging_loki
```

## Quick Start

```python
import logging_loki

print(logging_loki.__version__)
```

## Development

### Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) for package management

### Setup

Clone the repository and install dependencies:

```bash
git clone https://github.com/tjzegmott/python-logging-loki.git
cd python-logging-loki
uv sync --group dev
```

### Running Tests

```bash
uv run pytest
```

### Code Quality

```bash
# Lint
uv run ruff check .

# Format
uv run ruff format .

# Type check
uv run ty check
```

### Prek Hooks

Install prek hooks:

```bash
prek install
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/tjzegmott/python-logging-loki/blob/main/LICENSE) file for details.
