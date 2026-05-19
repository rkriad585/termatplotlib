from typing import Callable, List, Optional

from termatplotlib.utils import (
    COLORS, COLOR_NAMES, write_output, get_terminal_width, get_default,
    format_plot_lines,
)


def step(
    data: List[dict],
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
    tick_formatter: Optional[Callable[[float], str]] = None,
    output_file: Optional[str] = None,
    _return_output: bool = False,
) -> Optional[List[str]]:
    width = get_default('width') or width or get_terminal_width()
    height = get_default('height') or height
    color = get_default('color') or color

    output: List[str] = []
    if title:
        output.append(f"\n{title.center(width)}\n")

    if not data:
        output.append("Error: Empty data.")
        write_output(output, output_file)
        return (output if _return_output else None)

    all_x: List[float] = []
    all_y: List[float] = []
    for i, series in enumerate(data):
        if 'x' not in series or 'y' not in series:
            output.append(f"Error: Series {i} missing 'x' or 'y'.")
            write_output(output, output_file)
            return (output if _return_output else None)
        if len(series['x']) != len(series['y']):
            output.append(f"Error: Series {i} length mismatch.")
            write_output(output, output_file)
            return (output if _return_output else None)
        all_x.extend(series['x'])
        all_y.extend(series['y'])

    if not all_x:
        output.append("Error: No data.")
        write_output(output, output_file)
        return (output if _return_output else None)

    min_x = xlim[0] if xlim and len(xlim) > 0 else min(all_x)
    max_x = xlim[1] if xlim and len(xlim) > 1 else max(all_x)
    min_y = ylim[0] if ylim and len(ylim) > 0 else min(all_y)
    max_y = ylim[1] if ylim and len(ylim) > 1 else max(all_y)
    if max_x == min_x:
        max_x = min_x + 1
    if max_y == min_y:
        max_y = min_y + 1

    grid_chart = [[' ' for _ in range(width)] for _ in range(height)]
    x_range = max_x - min_x
    y_range = max_y - min_y

    for s_idx, series in enumerate(data):
        xs = series['x']
        ys = series['y']
        mkr = series.get('marker', '')
        s_color = series.get('color', '')
        if not s_color:
            s_color = color if color else COLOR_NAMES[s_idx % len(COLOR_NAMES)]
        clr = COLORS.get(s_color, '')
        rc = COLORS['reset'] if clr else ''

        for i in range(len(xs) - 1):
            x1 = xs[i]
            y1 = ys[i]
            x2 = xs[i + 1]
            y2 = ys[i + 1]

            c1 = int((x1 - min_x) / x_range * (width - 1)) if x_range else 0
            r1 = int((max_y - y1) / y_range * (height - 1)) if y_range else 0
            c2 = int((x2 - min_x) / x_range * (width - 1)) if x_range else 0
            r2 = int((max_y - y2) / y_range * (height - 1)) if y_range else 0
            c1 = max(0, min(width - 1, c1))
            c2 = max(0, min(width - 1, c2))
            r1 = max(0, min(height - 1, r1))
            r2 = max(0, min(height - 1, r2))

            step_dir = 1 if c2 >= c1 else -1
            for c in range(c1, c2 + step_dir, step_dir):
                if 0 <= c < width and 0 <= r1 < height:
                    grid_chart[r1][c] = clr + '─' + rc if clr else '─'

            step_dir_r = 1 if r2 >= r1 else -1
            for r in range(r1, r2 + step_dir_r, step_dir_r):
                if 0 <= c2 < width and 0 <= r < height:
                    grid_chart[r][c2] = clr + '│' + rc if clr else '│'

        for i in range(len(xs)):
            c = int((xs[i] - min_x) / x_range * (width - 1)) if x_range else 0
            r = int((max_y - ys[i]) / y_range * (height - 1)) if y_range else 0
            c = max(0, min(width - 1, c))
            r = max(0, min(height - 1, r))
            ch = mkr if mkr else '●' if i == 0 else '○'
            grid_chart[r][c] = clr + ch + rc if clr else ch

    lines = format_plot_lines(
        grid_chart, width, height, min_x, max_x, min_y, max_y,
        xlabel, ylabel, grid, custom_xticks=custom_xticks,
        custom_yticks=custom_yticks, tick_formatter=tick_formatter,
        thresholds=thresholds,
    )
    output.extend(lines)

    if legend:
        for s_idx, series in enumerate(data):
            s_color = series.get('color', '') or (color if color else COLOR_NAMES[s_idx % len(COLOR_NAMES)])
            clr = COLORS.get(s_color, '')
            rc = COLORS['reset'] if clr else ''
            label = series.get('label', f"Series {s_idx + 1}")
            output.append(f"  {clr}─{rc} {label}")

    write_output(output, output_file)
    return (output if _return_output else None)
