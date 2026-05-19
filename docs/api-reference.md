# API Reference

## Module Contents

```python
import termatplotlib as tpl
```

### Chart Functions

| Function | Description |
|----------|-------------|
| `tpl.bar()` | Horizontal bar chart |
| `tpl.grouped_bar()` | Side-by-side grouped bar chart |
| `tpl.stacked_bar()` | Stacked horizontal bar chart |
| `tpl.scatter()` | Scatter plot |
| `tpl.line()` | Line chart |
| `tpl.area()` | Filled area chart |
| `tpl.pie()` | Pie chart |
| `tpl.hist()` | Histogram |
| `tpl.boxplot()` | Box-and-whisker plot |
| `tpl.heatmap()` | 2D heatmap grid |
| `tpl.vertical_bar()` | Vertical column chart |
| `tpl.diverging_bar()` | Diverging bar chart from baseline |
| `tpl.sparkline()` | Inline mini sparkline |
| `tpl.candlestick()` | OHLC financial candlestick chart |
| `tpl.violinplot()` | Violin distribution plot |
| `tpl.calendar_heatmap()` | Year calendar heatmap grid |
| `tpl.radar()` | Polar radar/spider chart |
| `tpl.waterfall()` | Sequential waterfall bridge chart |
| `tpl.gantt()` | Project timeline Gantt chart |
| `tpl.step()` | Stair-step chart |
| `tpl.bubble()` | Bubble chart with variable sizes |
| `tpl.strip()` | 1D strip/dot distribution plot |

### Figure API

| Function | Description |
|----------|-------------|
| `tpl.Figure(title)` | Create a multi-chart figure container |
| `fig.add_chart(func, *args, **kwargs)` | Add a chart to the figure |
| `fig.render(output_file)` | Render all charts (stacked) |
| `fig.savefig(path)` | Render and save to file |

### Utilities

| Function | Description |
|----------|-------------|
| `tpl.COLORS` | Dict of color name → ANSI escape codes |
| `tpl.get_terminal_width()` | Auto-detect terminal width |
| `tpl.strip_ansi(text)` | Remove ANSI escape codes |
| `tpl.set_default(**kwargs)` | Set global default parameter |
| `tpl.get_default(key)` | Get current default value |
| `tpl.reset_defaults()` | Clear all global defaults |

### Constants

```python
tpl.COLORS = {
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'reset': '\033[0m',
}
```

## Conditional Parameters

### Parameters available on most chart types

| Parameter | Type | Default | Applies To | Description |
|-----------|------|---------|------------|-------------|
| `title` | `Optional[str]` | `None` | All | Centered chart title |
| `output_file` | `Optional[str]` | `None` | All | File path for output (ANSI stripped) |
| `color` | `Optional[str]` | `None` | bar, scatter, line, area, hist, boxplot, heatmap | Primary color name |
| `width` | `int` | varies | scatter, line, area, boxplot, heatmap | Plot width in characters |
| `height` | `int` | varies | scatter, line, area, hist, boxplot | Plot height in characters |

### Scatter / Line / Area specific

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `legend` | `bool` | `False` | Show per-series legend |
| `grid` | `bool` | `False` | Overlay grid lines |
| `xlim` | `Optional[Tuple[float,float]]` | `None` | X-axis range `(min, max)` |
| `ylim` | `Optional[Tuple[float,float]]` | `None` | Y-axis range `(min, max)` |
| `log_x` | `bool` | `False` | Logarithmic X-axis |
| `log_y` | `bool` | `False` | Logarithmic Y-axis |

### Bar chart specific

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `max_width` | `Optional[int]` | terminal width | Maximum chart width |
| `xlabel` | `Optional[str]` | `None` | X-axis label |
| `ylabel` | `Optional[str]` | `None` | Y-axis label |
| `error_y` | `Optional[Union[float, List[float]]]` | `None` | Error bar magnitude |

### Per-series keys (scatter, line, area)

Each series dictionary can contain:

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `x` | `List[float]` | required | X data points |
| `y` | `List[float]` | required | Y data points |
| `color` | `str` | function-level `color` | Series color |
| `marker` | `str` | `'*'` | Marker character |
| `label` | `str` | `'Series N'` | Legend label |
| `error_y` | `float` or `list` | `None` | Error bar magnitude (scatter, line) |
