# termatplotlib

**Version:** 0.3.0  
**License:** MIT  
**Author:** RK Riad Khan  
**Repository:** [github.com/rkriad585/termatplotlib](https://github.com/rkriad585/termatplotlib)

A lightweight, zero-dependency Python library for rendering ASCII plots directly in the terminal. Visualize data with bar charts, scatter plots, line charts, pie charts, histograms, area charts, box plots, and heatmaps — all with ANSI color support, grid lines, legends, and file output.

## Features

- **10+ chart types** — bar, grouped bar, stacked bar, scatter, line, pie, histogram, area, box plot, heatmap
- **Zero dependencies** — pure Python, stdlib only, Python >=3.6
- **Logarithmic axes** — `log_x` / `log_y` for scatter, line, area
- **Error bars** — `error_y` on bar charts, and per-series on scatter/line
- **Multi-figure layout** — `Figure` class to compose multiple charts
- **Configuration system** — `set_default()` / `reset_defaults()` for global styling
- **ANSI colors** — 8 named colors for all chart elements
- **Grid lines** — optional `+`, `-`, `|` grid overlay
- **Legends** — auto-generated per-series legends
- **Axis limits** — custom `xlim` / `ylim` for zooming
- **File output** — save to `.txt` files with ANSI codes automatically stripped
- **Terminal auto-detect** — fits to terminal width by default
- **Multi-series** — any number of series on scatter, line, area
- **Type hints** — full PEP 484 type annotations

## Table of Contents

- [Installation](installation.md)
- [Quick Start](quickstart.md)
- [Chart Types](chart-types.md)
- [API Reference](api-reference.md)
- [Configuration](configuration.md)
- [Advanced Features](advanced.md)
- [Output & Formatting](output.md)
- [Examples](examples.md)
- [Contributing](contributing.md)
- [Changelog](changelog.md)
