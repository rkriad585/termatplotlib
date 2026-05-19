# termatplotlib

A lightweight and elegant Python library for rendering stunning ASCII plots directly in your terminal. Zero dependencies.

## Features

- **10+ Chart Types** — Bar, grouped bar, stacked bar, scatter, line, pie, histogram, area (stacked too), box plot, and heatmap.
- **Logarithmic Axes** — `log_x` / `log_y` for scatter, line, and area charts.
- **Error Bars** — `error_y` for bar, scatter, and line charts.
- **Multi-Figure Layout** — `Figure` class to compose multiple charts together.
- **Configuration System** — `set_default()` / `get_default()` / `reset_defaults()` for global styling.
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

### Figure (Multi-Chart Layout)
```python
fig = tpl.Figure(title="Dashboard")
fig.add_chart(tpl.bar, ["A", "B"], [10, 20], max_width=40, color="red")
fig.add_chart(tpl.pie, ["X", "Y"], [30, 70])
fig.render()
fig.savefig("dashboard.txt")
```

## Parameters

| Parameter | Used By | Description |
|-----------|---------|-------------|
| `title` | All | Chart title centered at top |
| `xlabel` | bar, scatter, line, hist, boxplot | X-axis label |
| `ylabel` | bar, scatter, line, hist, boxplot | Y-axis label |
| `color` | bar, scatter, line, hist, boxplot, heatmap | Chart color (named) |
| `colors` | grouped_bar, stacked_bar | List of colors per series |
| `output_file` | All | Save to file (no ANSI codes) |
| `legend` | scatter, line, area, pie | Show data legend |
| `width` | scatter, line, area, boxplot, heatmap | Plot width in chars |
| `height` | scatter, line, area, hist, boxplot | Plot height in chars |
| `max_width` | bar, grouped_bar, stacked_bar | Max chart width |
| `bins` | hist | Number of histogram bins |
| `marker` | scatter, line, area (per series) | Point marker character |
| `stacked` | area | Stack series on top of each other |
| `log_x`, `log_y` | scatter, line, area | Logarithmic axes |
| `error_y` | bar (function param), scatter, line (per series) | Error bar magnitude |
| `grid` | scatter, line, area | Show grid lines |
| `xlim`, `ylim` | scatter, line, area | Custom axis limits |
| `palette` | heatmap | List of colors for data range |

## Configuration System

Set global defaults that apply to all subsequent charts:

```python
tpl.set_default(width=80, height=30, color='blue', legend=True)
tpl.get_default('color')   # 'blue'
tpl.reset_defaults()        # clear all defaults
```

## Colors

`black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`

## Markers

Any single character. Common choices: `'o'`, `'x'`, `'*'`, `'.'`, `'+'`, `'#'`

## Running Tests

```bash
pytest
```

## License

MIT
