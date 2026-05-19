# Chart Types

## bar

Horizontal bar chart for categorical data with one value per category.

```python
tpl.bar(
    labels: List[str],
    values: List[float],
    max_width: Optional[int] = None,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    color: Optional[str] = None,
    output_file: Optional[str] = None,
    error_y: Optional[Union[float, List[float]]] = None,
)
```

Negative values render as absolute-length bars with a `<` indicator. Error bars show as `±N` in the value suffix.

---

## grouped_bar

Side-by-side bars for comparing multiple series across categories.

```python
tpl.grouped_bar(
    labels: List[str],
    values: List[List[float]],
    max_width: Optional[int] = None,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    colors: Optional[List[str]] = None,
    output_file: Optional[str] = None,
)
```

---

## stacked_bar

Stacked horizontal bars where each series is a segment of the total bar.

```python
tpl.stacked_bar(
    labels: List[str],
    values: List[List[float]],
    max_width: Optional[int] = None,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    colors: Optional[List[str]] = None,
    output_file: Optional[str] = None,
)
```

---

## scatter

Scatter plot with customizable markers, colors, and per-series styling.

```python
tpl.scatter(
    data: List[dict],       # series: {x, y, color, marker, label, error_y}
    width: int = 50,
    height: int = 20,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    output_file: Optional[str] = None,
    color: Optional[str] = None,    # fallback color for all series
    legend: bool = False,
    grid: bool = False,
    xlim: Optional[Tuple[float, float]] = None,
    ylim: Optional[Tuple[float, float]] = None,
    log_x: bool = False,
    log_y: bool = False,
)
```

**Per-series keys:**

| Key | Type | Description |
|-----|------|-------------|
| `x` | `List[float]` | X coordinates |
| `y` | `List[float]` | Y coordinates |
| `color` | `str` (optional) | Series color name |
| `marker` | `str` (optional) | Single-character marker |
| `label` | `str` (optional) | Legend label |
| `error_y` | `float` or `List[float]` (optional) | Error bar magnitude |

---

## line

Line chart connecting data points using Bresenham's line algorithm.

```python
tpl.line(
    data: List[dict],
    width: int = 50,
    height: int = 20,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    output_file: Optional[str] = None,
    color: Optional[str] = None,
    legend: bool = False,
    grid: bool = False,
    xlim: Optional[Tuple[float, float]] = None,
    ylim: Optional[Tuple[float, float]] = None,
    log_x: bool = False,
    log_y: bool = False,
)
```

Supports the same per-series keys as scatter.

---

## area

Filled area chart. Optionally stacks multiple series.

```python
tpl.area(
    data: List[dict],
    width: int = 50,
    height: int = 20,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    output_file: Optional[str] = None,
    color: Optional[str] = None,
    stacked: bool = False,
    legend: bool = False,
    grid: bool = False,
    xlim: Optional[Tuple[float, float]] = None,
    ylim: Optional[Tuple[float, float]] = None,
    log_x: bool = False,
    log_y: bool = False,
)
```

---

## pie

Radial pie chart with polar-coordinate rendering.

```python
tpl.pie(
    labels: List[str],
    values: List[float],
    radius: int = 10,
    title: Optional[str] = None,
    legend: bool = True,
    output_file: Optional[str] = None,
)
```

Colors cycle through `COLOR_NAMES` automatically.

---

## hist

Vertical histogram with automatic binning and sparse y-axis labels.

```python
tpl.hist(
    data: List[float],
    bins: int = 10,
    width: Optional[int] = None,
    height: int = 10,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    color: Optional[str] = None,
    char: str = '█',
    output_file: Optional[str] = None,
)
```

Uses O(n) integer-indexed bin look-up.

---

## boxplot

Box-and-whisker plot showing quartiles, median, whiskers, and outliers.

```python
tpl.boxplot(
    data: List[List[float]],
    labels: Optional[List[str]] = None,
    width: int = 50,
    height: int = 20,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    output_file: Optional[str] = None,
    color: Optional[str] = None,
)
```

Box spans Q1–Q3 with a median line. Whiskers extend to 1.5×IQR.

---

## heatmap

2D grid heatmap with intensity-based ASCII shading and optional color palette.

```python
tpl.heatmap(
    data: List[List[float]],
    row_labels: Optional[List[str]] = None,
    col_labels: Optional[List[str]] = None,
    title: Optional[str] = None,
    color: Optional[str] = None,
    palette: Optional[List[str]] = None,
    width: Optional[int] = None,
    output_file: Optional[str] = None,
)
```

Uses 5 intensity levels (space → `░` → `▒` → `▓` → `█`). Supports custom color palettes with multi-color gradients.
