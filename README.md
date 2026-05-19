# termatplotlib

A lightweight and elegant Python library for rendering stunning ASCII plots directly in your terminal. Visualize your data with beautiful scatter, line, bar, pie, histogram, area, and box plots — bringing the power of matplotlib to your command line.

## Features

- **Terminal-based Visualization** — Generate plots directly in your terminal using ASCII and Unicode characters.
- **Multiple Chart Types** — Bar, grouped bar, stacked bar, scatter, line, pie, histogram, area (stacked too), and box plots.
- **Customization** — Titles, axis labels, colors, markers, legends, and axis limits.
- **File Output** — Save plots to text files for sharing (ANSI codes automatically stripped).
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
        color=None, max_width=None, output_file=None)
```

### Grouped Bar Chart (multiple series side-by-side)
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
    {'x': [1, 2, 3], 'y': [4, 5, 6], 'color': 'red', 'marker': 'o', 'label': 'Series 1'},
]
tpl.scatter(data, title="My Plot", xlabel="X", ylabel="Y", legend=True, output_file="plot.txt")
```

### Line Chart
```python
data = [
    {'x': [0, 1, 2], 'y': [0, 1, 4], 'color': 'green', 'marker': '*', 'label': 'Quadratic'},
]
tpl.line(data, title="Line Plot", width=50, height=20, legend=True)
```

### Area Chart
```python
tpl.area(data, title="Area Under Curve", stacked=False, legend=True)
```

### Pie Chart
```python
tpl.pie(labels, values, title="My Pie", radius=10, legend=True, output_file=None)
```

### Histogram
```python
tpl.hist(data, bins=10, title="Histogram", xlabel="Value", ylabel="Frequency",
         color="magenta", width=None, height=10, output_file=None)
```

### Box Plot
```python
tpl.boxplot(data, labels=["Group A", "Group B"], title="Comparison",
            color="cyan", width=50, height=20, output_file=None)
```

## Parameters

| Parameter | Used By | Description |
|-----------|---------|-------------|
| `title` | All | Chart title centered at top |
| `xlabel` | bar, scatter, line, hist, boxplot | X-axis label |
| `ylabel` | bar, scatter, line, hist, boxplot | Y-axis label |
| `color` | bar, scatter, line, hist, boxplot | Chart color (named) |
| `colors` | grouped_bar, stacked_bar | List of colors per series |
| `output_file` | All | Save to file (no ANSI codes) |
| `legend` | scatter, line, area, pie | Show data legend |
| `width` | scatter, line, area, boxplot | Plot width in chars |
| `height` | scatter, line, area, hist, boxplot | Plot height in chars |
| `max_width` | bar, grouped_bar, stacked_bar | Max chart width |
| `bins` | hist | Number of histogram bins |
| `marker` | scatter, line, area (per series) | Point marker character |
| `stacked` | area | Stack series on top of each other |

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
