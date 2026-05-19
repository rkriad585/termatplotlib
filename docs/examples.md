# Examples

## Basic Examples

### 1. Simple bar chart

```python
import termatplotlib as tpl

tpl.bar(["A", "B", "C", "D"], [10, 20, 15, 5],
        title="My Bar Chart", xlabel="Value", ylabel="Category", color="red")
```

### 2. Scatter plot with legend

```python
data = [
    {'x': [1, 2, 3, 4, 5], 'y': [1, 4, 9, 16, 25], 'color': 'green', 'marker': 'o', 'label': 'x²'},
    {'x': [1, 2, 3, 4, 5], 'y': [25, 16, 9, 4, 1], 'color': 'red', 'marker': 'x', 'label': '25-x²'},
]
tpl.scatter(data, title="Multi-Series Scatter", legend=True)
```

### 3. Line chart with grid

```python
import math
x = [i * 0.5 for i in range(13)]
y_sin = [math.sin(v) for v in x]
y_cos = [math.cos(v) for v in x]
data = [
    {'x': x, 'y': y_sin, 'color': 'blue', 'marker': '.', 'label': 'sin(x)'},
    {'x': x, 'y': y_cos, 'color': 'red', 'marker': '.', 'label': 'cos(x)'},
]
tpl.line(data, title="Trigonometric Waves", legend=True, grid=True)
```

### 4. Pie chart

```python
tpl.pie(["Sales", "Marketing", "R&D", "Support"],
        [40, 25, 20, 15], title="Budget Allocation")
```

### 5. Histogram

```python
data = [1, 1, 2, 3, 3, 3, 4, 5, 5, 6, 7, 7, 7, 7, 8, 9, 10]
tpl.hist(data, bins=5, title="Data Distribution", color="magenta")
```

### 6. Box plot

```python
import random
random.seed(42)
data = [
    [random.gauss(50, 10) for _ in range(50)],
    [random.gauss(60, 15) for _ in range(50)],
    [random.gauss(45, 8) for _ in range(50)],
]
tpl.boxplot(data, labels=["Group A", "Group B", "Group C"],
            title="Distribution Comparison", color="cyan")
```

### 7. Stacked area chart

```python
x = [0, 1, 2, 3, 4, 5]
data = [
    {'x': x, 'y': [1, 2, 3, 4, 5, 6], 'color': 'blue', 'label': 'Series A'},
    {'x': x, 'y': [1, 2, 1, 2, 1, 2], 'color': 'red', 'label': 'Series B'},
]
tpl.area(data, title="Stacked Area", stacked=True, legend=True)
```

### 8. Grouped bar chart

```python
tpl.grouped_bar(
    ["Apples", "Bananas", "Oranges"],
    [[30, 20, 25], [20, 35, 15]],
    title="Fruit Sales by Region",
    colors=["red", "blue"],
)
```

### 9. Stacked bar chart

```python
tpl.stacked_bar(
    ["Q1", "Q2", "Q3", "Q4"],
    [[100, 120, 110, 130], [80, 90, 95, 100], [60, 70, 65, 80]],
    title="Quarterly Revenue by Product",
    colors=["cyan", "magenta", "yellow"],
)
```

### 10. Save all charts to file

```python
tpl.scatter([{'x': [1, 2, 3], 'y': [4, 5, 6]}], output_file="scatter.txt")
tpl.bar(["A", "B"], [10, 20], color="blue", output_file="bar.txt")
tpl.pie(["X", "Y", "Z"], [30, 50, 20], output_file="pie.txt")
```

---

## Advanced Examples

### 11. Log-scale scatter

```python
tpl.scatter([{'x': [1, 2, 3, 4, 5], 'y': [1, 10, 100, 1000, 10000], 'marker': 'o'}],
            width=40, height=15, title="Log Scale", log_y=True)
```

### 12. Log-log line with grid

```python
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [v**2 for v in x]
tpl.line([{'x': x, 'y': y, 'color': 'blue', 'marker': '.'}],
         title="Quadratic (Log-Log)", log_x=True, log_y=True, grid=True, width=40, height=15)
```

### 13. Bar with error bars

```python
tpl.bar(["A", "B", "C"], [10, 20, 15], max_width=40, color="green", error_y=[1, 2, 1.5])
```

### 14. Scatter with error bars

```python
tpl.scatter([{'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10], 'error_y': 0.5, 'marker': 'o'}],
            width=30, height=15, title="With Error Bars")
```

### 15. Heatmap

```python
data = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
tpl.heatmap(data, row_labels=["Row1", "Row2", "Row3"],
            col_labels=["Col1", "Col2", "Col3", "Col4"],
            title="Basic Heatmap", color="cyan")
```

### 16. Heatmap with palette

```python
tpl.heatmap([[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]],
            title="Heatmap with Palette", palette=["red", "yellow", "green"])
```

### 17. Figure dashboard

```python
fig = tpl.Figure(title="Dashboard")
fig.add_chart(tpl.bar, ["Q1", "Q2", "Q3", "Q4"], [150, 200, 175, 250],
              max_width=40, color="blue")
fig.add_chart(tpl.hist, [1, 2, 2, 3, 3, 3, 4, 5], bins=4, width=40)
fig.add_chart(tpl.pie, ["Sales", "Marketing", "R&D", "Support"], [40, 25, 20, 15], radius=8)
fig.render()
```

### 18. Config system

```python
tpl.set_default(width=60, height=20, color='cyan', legend=True, grid=True)
tpl.scatter([{'x': [1, 2, 3], 'y': [4, 5, 6]}])
tpl.line([{'x': [0, 1, 2], 'y': [0, 1, 4]}])
tpl.reset_defaults()
```

### 19. Bar with negative values

```python
tpl.bar(["Profit", "Loss", "Tax", "Revenue"],
        [100, -30, -20, 150], title="Financials", color="cyan")
```

### 20. Scatter with zoom (axis limits)

```python
tpl.scatter([{'x': [1, 2, 3, 4, 5], 'y': [10, 20, 15, 30, 25]}],
            title="Zoomed View", xlim=(0, 6), ylim=(0, 40))
```
