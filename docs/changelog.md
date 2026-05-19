# Changelog

## v0.6.0 (2026-05-19)

### Added
- **Sankey diagram** — `sankey()` flow visualization between source/target nodes with colored links
- **Funnel chart** — `funnel()` sales pipeline with centered decreasing bars and % conversion
- **Bullet chart** — `bullet()` compact KPI gauge with qualitative ranges and target marker
- **Donut chart** — `donut()` pie variant with hole, optional center label, and legend
- **Pareto chart** — `pareto()` sorted descending bars with cumulative percentage line and 80% reference
- **Word cloud** — `wordcloud()` text visualization with weighted words placed on a grid
- **`show_percent`** option on funnel for conversion rate display
- **`show_80_line`** option on pareto for 80/20 rule reference
- **`center_label`** option on donut for text in the hole
- **`color_actual` / `color_target`** options on bullet for custom colors

### Changed
- CLI expanded to 18 supported chart types (sankey, funnel, bullet, donut, pareto, wordcloud)
- Updated all docs and README for 28 total chart types

---

## v0.5.0 (2026-05-19)

### Added
- **Radar chart** — `radar()` polar spider chart for multi-dimensional comparison with optional fill
- **Waterfall chart** — `waterfall()` sequential bridge chart with green/red/blue color coding
- **Gantt chart** — `gantt()` project timeline with colored horizontal bars on dotted timeline
- **Step chart** — `step()` stair-step transitions with multi-series, grid, thresholds support
- **Bubble chart** — `bubble()` scatter plot with variable bubble sizes using `· o O @` characters
- **Strip plot** — `strip()` 1D distribution with stacked dots and summary statistics
- **Docker support** — `Dockerfile` and `.dockerignore` for containerized usage
- **Shell scripts** — `run.ps1`, `run.cmd`, `run.sh` launcher scripts for all platforms
- **CLI expanded** — `termtplotlib` now supports `--type step`, `bubble`, `strip`, `waterfall`, `gantt`, `radar`

### Changed
- Updated CLI to support 12 chart types (was 6)
- Updated docs, README, and examples for 22 total chart types

---

## v0.4.0 (2026-05-19)

### Added
- **Vertical bar chart** — `vertical_bar()` with columns growing upward
- **Diverging bar chart** — `diverging_bar()` with bars diverging from a configurable baseline
- **Sparkline** — `sparkline()` tiny inline chart using Unicode block characters
- **Candlestick chart** — `candlestick()` OHLC financial chart with green/red body coloring
- **Violin plot** — `violinplot()` distribution visualization with mirrored KDE density
- **Calendar heatmap** — `calendar_heatmap()` GitHub-style contribution grid with day-of-week rows
- **Threshold lines** — `thresholds` parameter on scatter/line for horizontal/vertical reference lines with color and custom char
- **Custom axis ticks** — `custom_xticks` and `custom_yticks` for explicit tick positioning
- **Tick formatter** — `tick_formatter` callable for custom axis label formatting
- **Theme presets** — `apply_theme()` with 7 built-in themes: default, dark, light, monokai, ocean, forest, sunset
- **CLI stdin pipeline** — `termtplotlib` command that reads data from stdin for bar, scatter, line, pie, hist, and sparkline
- **`THEMES` constant** — exported dict of all theme definitions

### Changed
- Updated `format_plot_lines()` with new rendering helpers: `_render_yticks`, `_render_xticks`, `_draw_thresholds`
- All scatter/line/area signatures extended with `custom_xticks`, `custom_yticks`, `tick_formatter`, `thresholds`

---

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
