import math
from typing import Callable, List, Optional

from termatplotlib.utils import COLORS, write_output, get_terminal_width, get_default


def pareto(
    labels: List[str],
    values: List[float],
    width: Optional[int] = None,
    height: int = 15,
    title: Optional[str] = None,
    color_bar: Optional[str] = None,
    color_line: Optional[str] = None,
    show_80_line: bool = True,
    output_file: Optional[str] = None,
    _return_output: bool = False,
) -> Optional[List[str]]:
    width = get_default('width') or width or get_terminal_width()
    height = get_default('height') or height
    color_bar = get_default('color') or color_bar or 'cyan'
    color_line = get_default('color_secondary') or color_line or 'red'

    output: List[str] = []
    if title:
        output.append(f"\n{title.center(width)}\n")

    if not labels or not values or len(labels) != len(values):
        output.append("Error: Invalid input.")
        write_output(output, output_file)
        return (output if _return_output else None)

    pairs = sorted(zip(labels, values), key=lambda x: -x[1])
    sorted_labels = [p[0] for p in pairs]
    sorted_values = [p[1] for p in pairs]

    total = sum(sorted_values)
    cumulative = []
    running = 0
    for v in sorted_values:
        running += v
        cumulative.append(running / total * 100 if total else 0)

    max_val = max(sorted_values) if sorted_values else 1
    bar_w = width - 12
    if bar_w < 10:
        bar_w = 10

    clr_bar = COLORS.get(color_bar, '')
    clr_line = COLORS.get(color_line, '')
    rc = COLORS['reset'] if (clr_bar or clr_line) else ''

    sorted_labels_str = [str(l) for l in sorted_labels]
    max_label = max(len(l) for l in sorted_labels_str)
    chart_area_w = bar_w

    grid = [[' ' for _ in range(chart_area_w + max_label + 4)] for _ in range(height + 1)]

    for i, (lb, v, cum) in enumerate(zip(sorted_labels, sorted_values, cumulative)):
        bar_len = int(v / max_val * chart_area_w) if max_val else 0
        bar_len = max(1, bar_len)
        r = height - 1 - i * (height - 1) // max(len(sorted_labels) - 1, 1)
        if r < 0:
            r = 0
        label_str = str(lb).ljust(max_label)
        line = f"  {label_str} "
        for c in range(chart_area_w):
            if c < bar_len:
                grid[r][c + max_label + 2] = clr_bar + '█' + rc if clr_bar else '█'

        cum_c = int(cum / 100 * chart_area_w) if chart_area_w else 0
        cum_c = min(chart_area_w - 1, cum_c)
        if 0 <= cum_c < chart_area_w + max_label + 4:
            ch = clr_line + '◆' + rc if clr_line else '◆'
            if r < len(grid) and cum_c + max_label + 2 < len(grid[r]):
                grid[r][cum_c + max_label + 2] = ch

    for r in range(height):
        line = ''
        for c in range(chart_area_w + max_label + 4):
            line += grid[r][c]
        output.append(line)

    y_axis = ' '.join(f"{pct:3.0f}%" for pct in [0, 25, 50, 75, 100])
    output.append(f"  {' ' * max_label}  0%{' ' * (chart_area_w - 4)}100%")
    output.append(f"  Cum%: {y_axis}")

    if show_80_line:
        s_line = ' ' * (max_label + 2) + '-' * chart_area_w
        eight_idx = int(0.8 * chart_area_w)
        s_line = s_line[:max_label + 2 + eight_idx] + (clr_line + '┼' + rc if clr_line else '┼') + s_line[max_label + 2 + eight_idx + 1:]
        output.append(f"  {' ' * max_label}  80% line at column {eight_idx}")
        output.append(f"  {clr_line}◆{rc} = cumulative percentage point")

    output.append("")
    write_output(output, output_file)
    return (output if _return_output else None)
