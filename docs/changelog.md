# Changelog

## v0.3.0 (2026-05-19)

### Added
- **Logarithmic axes** — `log_x` / `log_y` for scatter, line, and area charts
- **Error bars** — `error_y` parameter on bar charts; per-series `error_y` key for scatter and line
- **Heatmap** — new `heatmap()` chart type with intensity-based ASCII shading, color palettes, and row/col labels
- **Figure API** — `Figure` class with `add_chart()`, `render()`, and `savefig()` for multi-chart composition
- **Configuration system** — `set_default()`, `get_default()`, and `reset_defaults()` for global styling
- **CI/CD** — GitHub Actions workflows for automated testing (Python 3.6–3.12 matrix) and PyPI publishing
- **`_return_output`** — private parameter on all chart functions enabling output capture for the Figure API

### Changed
- All chart functions now return `Optional[List[str]]` when `_return_output=True`
- `format_plot_lines()` accepts `log_x` / `log_y` flags for log-scale tick labels

---

## v0.2.0 (2026-05-19)

### Added
- Full type hints on all modules (bar, scatter, line, pie, hist, boxplot, utils)
- 71 tests across 14 test classes

### Fixed
- ANSI escape codes bleeding into output files → `write_output()` calls `strip_ansi()`
- `scatter()` and `line()` color shadowing → renamed to `series_color`
- `pie()` and `hist()` missing `output_file` parameter
- `bar()` negative values hidden → absolute value with `<` indicator
- `grouped_bar()` and `stacked_bar()` ignoring negative values → uses `abs()`
- `stacked_bar()` redundant color reset → removed
- `hist()` missing y-axis labels → sparse tick marks at ~5 positions
- `hist()` O(n×bins) → O(n) int-indexed bin look-up

### Added
- Input validation via `validate_data()`
- Edge case handling: single points, zero ranges, empty data, identical values
- `legend=True` parameter for scatter, line, area
- `grid=True` parameter for scatter, line, area
- `xlim` / `ylim` axis limits for scatter, line, area
- `grouped_bar()` — side-by-side bars
- `stacked_bar()` — stacked horizontal bars
- `area()` — filled area under line, with `stacked=True`
- `boxplot()` — box-and-whisker with quartiles

### Changed
- Migrated from `setup.py` to `pyproject.toml`
- Split monolithic `__init__.py` into 7 modules
- Extracted `format_plot_lines()` to eliminate scatter/line duplication

---

## v0.1.0 (2026-05-18)

### Initial Release

- Bar, scatter, line, pie, and histogram chart types
- ANSI color support (8 named colors)
- File output with ANSI stripping
- Terminal width auto-detection
- Single-file prototype (`__init__.py`)
- Basic examples in `examples.py`
