# termatplotlib

A lightweight and elegant Python library for rendering stunning ASCII plots directly in your terminal. Zero dependencies.

## Features

- **16 Chart Types** — Bar, grouped bar, stacked bar, diverging bar, vertical bar, scatter, line, pie, histogram, area, box plot, violin plot, heatmap, calendar heatmap, candlestick, sparkline.
- **Logarithmic Axes** — `log_x` / `log_y` for scatter, line, and area charts.
- **Error Bars** — `error_y` for bar, scatter, and line charts.
- **Threshold Lines** — Horizontal/vertical reference lines on scatter/line charts.
- **Custom Ticks & Formatters** — `custom_xticks`, `custom_yticks`, `tick_formatter` for full axis control.
- **Theme Presets** — 7 built-in themes (default, dark, light, monokai, ocean, forest, sunset).
- **Multi-Figure Layout** — `Figure` class to compose multiple charts together.
- **Configuration System** — `set_default()` / `get_default()` / `reset_defaults()` for global styling.
- **CLI Tool** — Pipe data from stdin directly into charts via `termtplotlib` command.
- **Customization** — Titles, axis labels, colors, markers, legends, axis limits, grid lines.
- **File Output** — Save plots to text files (ANSI codes automatically stripped).
- **Terminal Auto-Detect** — Automatically fits to your terminal width.
- **Multi-Series** — Plot multiple data series on the same chart.
- **No Dependencies** — Pure Python, no external packages required.

## Installation

```bash
pip install termatplotlib
```

Or from source:

```bash
git clone https://github.com/rkriad585/termatplotlib
cd termatplotlib
pip install .
```

## Quick Start

```python
import termatplotlib as tpl

# Bar chart
tpl.bar(["A", "B", "C", "D"], [10, 20, 15, 5],
        title="My Chart", xlabel="Value", color="red")
```

## Chart Types

### Bar Chart
```python
tpl.bar(labels, values, title=None, xlabel=None, ylabel=None,
        color=None, max_width=None, output_file=None, error_y=None)
```

### Grouped Bar Chart
```python
tpl.grouped_bar(labels, values, title=None, xlabel=None, ylabel=None,
                colors=None, max_width=None, output_file=None)
```

### Stacked Bar Chart
```python
tpl.stacked_bar(labels, values, title=None, xlabel=None, ylabel=None,
                colors=None, max_width=None, output_file=None)
```

### Scatter Plot
```python
data = [
    {'x': [1, 2, 3], 'y': [4, 5, 6], 'color': 'red', 'marker': 'o',
     'label': 'Series 1', 'error_y': 0.5},
]
tpl.scatter(data, title="My Plot", xlabel="X", ylabel="Y",
            legend=True, grid=True, log_y=True, output_file="plot.txt")
```

### Line Chart
```python
data = [
    {'x': [0, 1, 2], 'y': [0, 1, 4], 'color': 'green',
     'marker': '*', 'label': 'Quadratic', 'error_y': 0.2},
]
tpl.line(data, title="Line Plot", width=50, height=20, legend=True, grid=True)
```

### Area Chart
```python
tpl.area(data, title="Area Under Curve", stacked=False, legend=True, log_y=True)
```

### Pie Chart
```python
tpl.pie(labels, values, title="My Pie", radius=10, legend=True)
```

### Histogram
```python
tpl.hist(data, bins=10, title="Histogram", xlabel="Value", ylabel="Frequency",
         color="magenta", width=None, height=10)
```

### Box Plot
```python
tpl.boxplot(data, labels=["Group A", "Group B"], title="Comparison",
            color="cyan", width=50, height=20)
```

### Heatmap
```python
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
tpl.heatmap(data, row_labels=["A", "B", "C"], col_labels=["X", "Y", "Z"],
            title="Heatmap", color="red")
```

### Vertical Bar Chart
```python
tpl.vertical_bar(["A", "B", "C"], [10, 20, 15], height=15, title="Vertical")
```

### Diverging Bar Chart
```python
tpl.diverging_bar(["Profit", "Loss"], [100, -30], baseline=0, colors=["green", "red"])
```

### Sparkline (inline mini-chart)
```python
tpl.sparkline([1, 5, 22, 13, 5], title="Trend", color="green")
```

### Candlestick Chart (OHLC)
```python
data = [
    {'open': 100, 'high': 110, 'low': 95, 'close': 105},
    {'open': 105, 'high': 115, 'low': 100, 'close': 102},
]
tpl.candlestick(data, width=40, height=15, title="AAPL")
```

### Violin Plot
```python
tpl.violinplot([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]],
               labels=["A", "B"], title="Distribution")
```

### Calendar Heatmap
```python
tpl.calendar_heatmap({"2026-01-01": 5, "2026-06-15": 10}, title="Activity")
```

### Figure (Multi-Chart Layout)
```python
fig = tpl.Figure(title="Dashboard")
fig.add_chart(tpl.bar, ["A", "B"], [10, 20], max_width=40, color="red")
fig.add_chart(tpl.pie, ["X", "Y"], [30, 70])
fig.render()
fig.savefig("dashboard.txt")
```

### Threshold Lines
```python
tpl.scatter([{'x': [1, 2, 3], 'y': [4, 5, 6]}],
            thresholds=[{'axis': 'y', 'value': 5, 'color': 'red'}])
```

### Custom Ticks & Formatters
```python
tpl.scatter([{'x': [1, 2, 3], 'y': [4, 5, 6]}],
            custom_xticks=[1, 2, 3],
            tick_formatter=lambda v: f"${v:.0f}")
```

### Themes
```python
tpl.apply_theme('monokai')
tpl.bar(["A", "B"], [10, 20])
```

### CLI (stdin pipeline)
```bash
echo "1,5,22,13,5" | termatplotlib --type sparkline --color green
echo "10,20,15,30,25" | termatplotlib --type bar --labels "A B C D E" --title "Data"
```

## Parameters

| Parameter | Used By | Description |
|-----------|---------|-------------|
| `title` | All | Chart title centered at top |
| `color` | bar, scatter, line, hist, boxplot, heatmap, sparkline | Chart color (named) |
| `colors` | grouped_bar, stacked_bar, diverging_bar | List of colors per series |
| `output_file` | All | Save to file (no ANSI codes) |
| `legend` | scatter, line, area, pie | Show data legend |
| `width` | scatter, line, area, boxplot, heatmap, vertical_bar | Plot width in chars |
| `height` | scatter, line, area, hist, boxplot, vertical_bar, violin, candlestick | Plot height in chars |
| `max_width` | bar, grouped_bar, stacked_bar, diverging_bar | Max chart width |
| `bins` | hist | Number of histogram bins |
| `marker` | scatter, line, area (per series) | Point marker character |
| `stacked` | area | Stack series on top of each other |
| `log_x`, `log_y` | scatter, line, area | Logarithmic axes |
| `error_y` | bar (function param), scatter, line (per series) | Error bar magnitude |
| `grid` | scatter, line, area | Show grid lines |
| `xlim`, `ylim` | scatter, line, area | Custom axis limits |
| `thresholds` | scatter, line | Reference lines `[{axis, value, color, char}]` |
| `custom_xticks`, `custom_yticks` | scatter, line, area | Explicit tick positions |
| `tick_formatter` | scatter, line, area | Custom tick label formatter |
| `palette` | heatmap, calendar_heatmap | List of colors for data range |
| `baseline` | diverging_bar | Center value for divergence |

## Configuration System

```python
tpl.apply_theme('monokai')                # apply built-in theme
tpl.set_default(width=80, height=30, color='blue', legend=True)
tpl.get_default('color')                  # 'blue'
tpl.reset_defaults()                      # clear all defaults
```

## Themes

`default`, `dark`, `light`, `monokai`, `ocean`, `forest`, `sunset`

## Colors

`black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`

## Markers

Any single character. Common choices: `'o'`, `'x'`, `'*'`, `'.'`, `'+'`, `'#'`

## CLI Examples

```bash
# Bar chart from stdin
echo "10,20,15,30" | termatplotlib --type bar --labels "A B C D" --title "Sales" --color blue

# Sparkline from stdin
echo "1,5,22,13,5,8,3,10" | termatplotlib --type sparkline --color green

# Histogram from stdin
echo "1 2 2 3 3 3 4 5 5 6" | termatplotlib --type hist --bins 5 --title "Distribution"
```

## Running Tests

```bash
pytest
```

## Documentation

Full documentation is available in the `docs/` folder:

- [Overview](docs/index.md)
- [Installation](docs/installation.md)
- [Quick Start](docs/quickstart.md)
- [Chart Types](docs/chart-types.md)
- [API Reference](docs/api-reference.md)
- [Configuration](docs/configuration.md)
- [Advanced Features](docs/advanced.md)
- [Output & Formatting](docs/output.md)
- [Examples](docs/examples.md)
- [Contributing](docs/contributing.md)
- [Changelog](docs/changelog.md)

## License

MIT
