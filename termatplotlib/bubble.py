import math
from typing import List, Optional

from termatplotlib.utils import (
    COLORS, COLOR_NAMES, write_output, get_terminal_width, get_default,
)


def bubble(
    data: List[dict],
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
    _return_output: bool = False,
) -> Optional[List[str]]:
    width = get_default('width') or width or get_terminal_width()
    height = get_default('height') or height

    output: List[str] = []
    if title:
        output.append(f"\n{title.center(width)}\n")

    if not data:
        output.append("Error: Empty data.")
        write_output(output, output_file)
        return (output if _return_output else None)

    all_x: List[float] = []
    all_y: List[float] = []
    all_sizes: List[float] = []

    for i, series in enumerate(data):
        if 'x' not in series or 'y' not in series:
            output.append(f"Error: Series {i} missing 'x' or 'y'.")
            write_output(output, output_file)
            return (output if _return_output else None)
        xs = series['x']
        ys = series['y']
        sizes = series.get('size', [5] * len(xs))
        if not (len(xs) == len(ys) == len(sizes)):
            output.append(f"Error: Series {i} x/y/size length mismatch.")
            write_output(output, output_file)
            return (output if _return_output else None)
        all_x.extend(xs)
        all_y.extend(ys)
        all_sizes.extend(sizes)

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

    x_range = max_x - min_x
    y_range = max_y - min_y

    base_grid = [[' ' for _ in range(width)] for _ in range(height)]

    BUBBLE_CHARS = ['·', 'o', 'O', '@']
    max_size = max(all_sizes) if all_sizes else 1

    for s_idx, series in enumerate(data):
        xs = series['x']
        ys = series['y']
        sizes = series.get('size', [5] * len(xs))
        mkr = series.get('marker', '')
        s_color = series.get('color', '')
        if not s_color:
            s_color = COLOR_NAMES[s_idx % len(COLOR_NAMES)]
        clr = COLORS.get(s_color, '')
        rc = COLORS['reset'] if clr else ''

        for i in range(len(xs)):
            c = int((xs[i] - min_x) / x_range * (width - 1)) if x_range else 0
            r = int((max_y - ys[i]) / y_range * (height - 1)) if y_range else 0
            c = max(0, min(width - 1, c))
            r = max(0, min(height - 1, r))

            size_frac = sizes[i] / max_size if max_size else 1
            bubble_r = max(1, int(size_frac * 3))

            idx = min(int(size_frac * 3), 3)
            ch = mkr if mkr else BUBBLE_CHARS[idx]
            base_grid[r][c] = clr + ch + rc if clr else ch

            if bubble_r > 1:
                for dr in range(-bubble_r, bubble_r + 1):
                    for dc in range(-bubble_r, bubble_r + 1):
                        dist = math.sqrt(dr * dr + dc * dc)
                        if dist <= bubble_r + 0.3:
                            nr = r + dr
                            nc = c + dc
                            if 0 <= nr < height and 0 <= nc < width:
                                if base_grid[nr][nc] == ' ':
                                    edge = abs(dist - bubble_r) < 0.8
                                    base_grid[nr][nc] = clr + ('o' if edge else '·') + rc if clr else ('o' if edge else '·')

    from termatplotlib.utils import format_plot_lines
    lines = format_plot_lines(
        base_grid, width, height, min_x, max_x, min_y, max_y,
        xlabel, ylabel, grid,
    )
    output.extend(lines)

    if legend:
        for s_idx, series in enumerate(data):
            s_color = series.get('color', '') or COLOR_NAMES[s_idx % len(COLOR_NAMES)]
            clr = COLORS.get(s_color, '')
            rc = COLORS['reset'] if clr else ''
            label = series.get('label', f"Series {s_idx + 1}")
            output.append(f"  {clr}●{rc} {label}")

    write_output(output, output_file)
    return (output if _return_output else None)
