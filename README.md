# dev-toolkit

A lightweight, zero-dependency Python utility suite for system diagnostics, benchmarking, and structured data formatting.

## Features
- **Benchmarking**: High-resolution latency profiling and memory tracking decorators.
- **Formatting**: Terminal-friendly table layouts and string utilities.
- **Diagnostics**: Environment inspection and telemetry helpers.

## Installation

```bash
pip install -e .
```

## Quick Start

```python
from toolkit.benchmarks import timer

@timer
def compute():
    return sum(i * i for i in range(1_000_000))

compute()
```

## License
MIT
