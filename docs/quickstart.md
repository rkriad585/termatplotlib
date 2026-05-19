# Quick Start

## Bar chart

```python
import termatplotlib as tpl

tpl.bar(
    ["A", "B", "C", "D"],
    [10, 20, 15, 5],
    title="My Chart",
    xlabel="Value",
    color="red",
)
```

## Scatter plot

```python
import termatplotlib as tpl

data = [
    {
        "x": [1, 2, 3, 4, 5],
        "y": [2, 4, 6, 8, 10],
        "color": "blue",
        "marker": "o",
        "label": "Linear",
    },
]
tpl.scatter(data, title="Scatter", legend=True, grid=True)
```

## Line chart

```python
import termatplotlib as tpl

data = [
    {"x": [0, 1, 2, 3, 4], "y": [0, 1, 4, 9, 16], "color": "green", "label": "x²"},
]
tpl.line(data, title="Line Plot", width=40, height=15, legend=True)
```

## Pie chart

```python
tpl.pie(
    ["Apples", "Bananas", "Oranges"],
    [30, 50, 20],
    title="Fruit Distribution",
)
```

## Histogram

```python
tpl.hist(
    [1, 2, 2, 3, 3, 3, 4, 5, 5, 6],
    bins=5,
    title="Histogram",
    color="magenta",
    width=40,
)
```

## Box plot

```python
tpl.boxplot(
    [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]],
    labels=["A", "B", "C"],
    title="Distribution Comparison",
    color="cyan",
)
```

## Heatmap

```python
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
tpl.heatmap(
    data,
    row_labels=["Row1", "Row2", "Row3"],
    col_labels=["X", "Y", "Z"],
    title="Heatmap",
    color="red",
)
```

## Area chart

```python
tpl.area(
    [{"x": [0, 1, 2, 3], "y": [0, 2, 1, 3], "color": "green", "label": "Area"}],
    title="Area Under Curve",
    legend=True,
)
```

## Grouped bar chart

```python
tpl.grouped_bar(
    ["Apples", "Bananas", "Oranges"],
    [[30, 20, 25], [20, 35, 15]],
    title="Fruit Sales by Region",
    colors=["red", "blue"],
)
```

## Stacked bar chart

```python
tpl.stacked_bar(
    ["Q1", "Q2", "Q3"],
    [[100, 120, 110], [80, 90, 95]],
    title="Quarterly Revenue",
    colors=["cyan", "magenta"],
)
```

## Save output to file

```python
tpl.bar(["A", "B"], [10, 20], color="red", output_file="chart.txt")
# Saved to chart.txt — ANSI codes automatically stripped
```

## Multi-chart figure

```python
fig = tpl.Figure(title="Dashboard")
fig.add_chart(tpl.bar, ["A", "B"], [10, 20], max_width=40, color="red")
fig.add_chart(tpl.pie, ["X", "Y"], [30, 70])
fig.render()
fig.savefig("dashboard.txt")
```
