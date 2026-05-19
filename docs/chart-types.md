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

---

## radar

Polar radar/spider chart for multi-dimensional comparison. Renders a circular grid with labeled axes radiating from center.

```python
tpl.radar(
    labels: List[str],
    values: List[float],
    width: int = 40,
    title: Optional[str] = None,
    fill: bool = False,
    color: Optional[str] = None,
    colors_list: Optional[List[str]] = None,
    scale_max: Optional[float] = None,
    output_file: Optional[str] = None,
)
```

Requires at least 3 categories. Each axis is labeled with its value. Optional `fill=True` shades the polygon interior.

---

## waterfall

Sequential bridge chart for financial or cumulative analysis. Shows running total as each value adds or subtracts.

```python
tpl.waterfall(
    labels: List[str],
    values: List[float],
    width: Optional[int] = None,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    color_up: Optional[str] = None,
    color_down: Optional[str] = None,
    color_total: Optional[str] = None,
    output_file: Optional[str] = None,
)
```

Uses green for positive, red for negative, and blue for the final total bar. Running cumulative value shown per bar.

---

## gantt

Timeline/Gantt chart for project scheduling and task tracking.

```python
tpl.gantt(
    tasks: List[dict],      # [{label, start, end, color}]
    width: Optional[int] = None,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    bar_char: str = '█',
    colors: Optional[List[str]] = None,
    output_file: Optional[str] = None,
)
```

Each task has a `start` and `end` (numeric time units), an optional `label` and `color`. Tasks render as colored horizontal bars on a dotted timeline.

---

## step

Step chart connecting points with horizontal-then-vertical transitions (stair-step). Useful for discrete changes over time.

```python
tpl.step(
    data: List[dict],       # [{x, y, color, marker, label}]
    width: Optional[int] = None,
    height: int = 15,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    legend: bool = False,
    grid: bool = False,
    xlim: Optional[List[float]] = None,
    ylim: Optional[List[float]] = None,
    color: Optional[str] = None,
    thresholds: Optional[List[dict]] = None,
    custom_xticks: Optional[List[float]] = None,
    custom_yticks: Optional[List[float]] = None,
    tick_formatter: Optional[Callable] = None,
    output_file: Optional[str] = None,
)
```

Supports multi-series, grid, thresholds, custom ticks, and legends via the same interface as scatter/line.

---

## bubble

Scatter plot enhanced with a size dimension. Each point's marker scales according to its `size` value.

```python
tpl.bubble(
    data: List[dict],       # [{x, y, size, color, marker, label}]
    width: Optional[int] = None,
    height: int = 18,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    legend: bool = False,
    grid: bool = False,
    xlim: Optional[List[float]] = None,
    ylim: Optional[List[float]] = None,
    output_file: Optional[str] = None,
)
```

The `size` key per series controls bubble radius. Uses characters `·`, `o`, `O`, `@` to represent increasing sizes. Surrounding halos drawn for larger bubbles.

---

## strip

One-dimensional strip/dot plot showing distribution of values along a single axis. Dots are stacked vertically at each bucket to show density.

```python
tpl.strip(
    data: List[float],
    width: Optional[int] = None,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    color: Optional[str] = None,
    jitter: bool = True,
    output_file: Optional[str] = None,
)
```

Shows summary statistics (n, min, max, range) below the chart. Quick distribution visualization without binning parameters.

---

## sankey

Flow diagram with colored links between source and target nodes.

```python
tpl.sankey(
    nodes: List[str],
    links: List[dict],       # [{source, target, value}]
    width: Optional[int] = None,
    title: Optional[str] = None,
    colors: Optional[List[str]] = None,
    output_file: Optional[str] = None,
)
```

Nodes are arranged in two columns (sources left, targets right). Links are drawn as shaded bands proportional to `value`. A legend shows in/out totals per node.

---

## funnel

Sales/conversion pipeline with centered bars decreasing proportionally.

```python
tpl.funnel(
    labels: List[str],
    values: List[float],
    width: Optional[int] = None,
    title: Optional[str] = None,
    color: Optional[str] = None,
    show_percent: bool = True,
    output_file: Optional[str] = None,
)
```

Bars are centered and widths scale with value. When `show_percent=True`, each stage shows its percentage relative to the first stage.

---

## bullet

Compact single-measure KPI gauge showing actual value, target marker, and qualitative ranges.

```python
tpl.bullet(
    labels: List[str],
    actuals: List[float],
    targets: List[float],
    ranges: Optional[List[dict]] = None,
    width: Optional[int] = None,
    title: Optional[str] = None,
    color_actual: Optional[str] = None,
    color_target: Optional[str] = None,
    output_file: Optional[str] = None,
)
```

Each metric renders as a horizontal bar with background shading (bad/satisfactory/good), an actual bar, and a target marker (▼). Optional `ranges` parameter overrides default thresholds per metric.

---

## donut

Ring/pie variant with a hollow center. Optional center label and legend.

```python
tpl.donut(
    labels: List[str],
    values: List[float],
    radius: int = 8,
    inner_radius: int = 3,
    title: Optional[str] = None,
    legend: bool = True,
    center_label: Optional[str] = None,
    output_file: Optional[str] = None,
)
```

Uses polar rendering with an inner radius cutout. Slices are colored from the standard color sequence. Shows percentage breakdown in legend.

---

## pareto

Priority chart combining sorted descending bars with a cumulative percentage line.

```python
tpl.pareto(
    labels: List[str],
    values: List[float],
    width: Optional[int] = None,
    height: int = 15,
    title: Optional[str] = None,
    color_bar: Optional[str] = None,
    color_line: Optional[str] = None,
    show_80_line: bool = True,
    output_file: Optional[str] = None,
)
```

Values are automatically sorted descending. Cumulative percentage markers (◆) are plotted at each category. The optional 80% reference line helps identify the vital few.

---

## wordcloud

Text visualization placing weighted words onto a grid, sized by frequency.

```python
tpl.wordcloud(
    word_weights: Dict[str, float],
    width: Optional[int] = None,
    height: int = 10,
    title: Optional[str] = None,
    colors: Optional[List[str]] = None,
    output_file: Optional[str] = None,
)
```

Words are placed randomly with collision avoidance. Larger weights use wider display. A ranked legend shows top words with bar-length indicators.
