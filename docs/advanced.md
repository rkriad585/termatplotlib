# Advanced Features

## Logarithmic Axes

Scatter, line, and area charts support `log_x` and `log_y` parameters for logarithmic axis scaling.

```python
import termatplotlib as tpl

data = [{'x': [1, 10, 100, 1000], 'y': [1, 2, 3, 4]}]
tpl.scatter(data, log_x=True, title="Log X Scale")

data2 = [{'x': [1, 2, 3, 4], 'y': [1, 10, 100, 1000]}]
tpl.scatter(data2, log_y=True, title="Log Y Scale")

# Log-log plot
import math
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [v**2 for v in x]
tpl.line([{'x': x, 'y': y}], log_x=True, log_y=True, title="Log-Log", grid=True)
```

### Behavior

- Data values are transformed to `log10()` space for positioning
- Axis tick labels show the actual (untransformed) values
- Tick labels use scientific notation for very large/small values
- Zero or negative values raise a clear error

### With axis limits

```python
tpl.scatter(data, log_x=True, xlim=(1, 200))
```

Both `xlim` and `ylim` are interpreted in the original (untransformed) scale.

---

## Error Bars

### Bar charts

```python
# Single error value for all bars
tpl.bar(["A", "B", "C"], [10, 20, 15], error_y=2)

# Per-bar error values
tpl.bar(["A", "B", "C"], [10, 20, 15], error_y=[1, 3, 2])
```

### Scatter and line charts

```python
data = [
    {
        'x': [1, 2, 3, 4, 5],
        'y': [2, 4, 6, 8, 10],
        'error_y': 0.5,          # uniform error
        'marker': 'o',
    },
]
tpl.scatter(data, title="With Error Bars")
```

```python
# Per-point error values
data = [
    {
        'x': [1, 2, 3, 4, 5],
        'y': [2, 4, 6, 8, 10],
        'error_y': [0.3, 0.5, 0.7, 0.5, 0.3],
        'marker': 'o',
    },
]
tpl.scatter(data, title="Variable Error Bars")
```

Error bars render as vertical `|` characters at each data point.

---

## Figure API (Multi-Chart Layout)

The `Figure` class lets you compose multiple charts into a single output.

```python
fig = tpl.Figure(title="Multi-Chart Dashboard")

# Add charts using add_chart(func, *args, **kwargs)
fig.add_chart(tpl.bar, ["A", "B", "C"], [10, 20, 15], max_width=40, color="red")
fig.add_chart(tpl.pie, ["X", "Y", "Z"], [30, 50, 20])
fig.add_chart(
    tpl.scatter,
    [{'x': [1, 2, 3], 'y': [4, 5, 6]}],
    width=30, height=10, color="blue",
)

# Render to terminal
fig.render()

# Save to file
fig.savefig("dashboard.txt")
```

### Chaining

```python
fig = tpl.Figure().add_chart(tpl.bar, ["A"], [5], max_width=40)
fig.render()
```

### How it works

Each chart function accepts a private `_return_output` parameter. When `True`, the function returns its output lines as a list instead of printing/writing them. The `Figure` class uses this internally to collect and compose outputs.

---

## Grid Lines

Scatter, line, and area charts support grid overlay with `grid=True`.

```python
tpl.scatter(data, grid=True)
tpl.line(data, grid=True)
tpl.area(data, grid=True)
```

Grid lines use `+` at intersections, `-` for horizontal, and `|` for vertical lines at approximately 5-tick intervals.

---

## Axis Limits

```python
tpl.scatter(data, xlim=(0, 10), ylim=(-5, 20))
tpl.line(data, xlim=(-1, 5), ylim=(0, 50))
```

Axis limits clip the visible range. Data outside the limits is not shown.

---

## Terminal Width Auto-Detect

Bar charts, histograms, and heatmaps default to the current terminal width.

```python
# Uses terminal width automatically
tpl.bar(["A", "B"], [10, 20])

# Override with explicit width
tpl.bar(["A", "B"], [10, 20], max_width=40)
```

---

## Input Validation

All chart functions validate their inputs:

- Mismatched x/y lengths
- Empty data lists
- Missing series keys
- Non-positive values in log scale

Errors are reported as printed messages (not exceptions) to keep CLI tools robust.

```python
tpl.bar(["A"], [10, 20])   # prints error: mismatched lengths
tpl.scatter([], width=20)  # prints error: empty data
```
