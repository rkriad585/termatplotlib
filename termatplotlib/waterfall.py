from typing import List, Optional

from termatplotlib.utils import COLORS, write_output, get_terminal_width, get_default


def waterfall(
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
    _return_output: bool = False,
) -> Optional[List[str]]:
    width = get_default('width') or width or get_terminal_width()
    color_up = get_default('color') or color_up or 'green'
    color_down = get_default('color_secondary') or color_down or 'red'
    color_total = get_default('color_accent') or color_total or 'blue'

    output: List[str] = []
    if title:
        output.append(f"\n{title.center(width)}\n")

    if not labels or not values or len(labels) != len(values):
        output.append("Error: Invalid input.")
        write_output(output, output_file)
        return (output if _return_output else None)

    running = 0
    bars = []
    for i, v in enumerate(values):
        is_total = (i == len(values) - 1)
        if is_total:
            bars.append({'start': 0, 'end': v, 'is_total': True})
        elif v >= 0:
            bars.append({'start': running, 'end': running + v, 'is_total': False})
            running += v
        else:
            bars.append({'start': running + v, 'end': running, 'is_total': False})
            running += v

    all_vals = [v for b in bars for v in (b['start'], b['end'])]
    if not all_vals:
        all_vals = [0, 1]
    min_val = min(all_vals)
    max_val = max(all_vals)
    val_range = max_val - min_val if max_val != min_val else 1

    chart_height = 16
    chart_w = width - 10
    if chart_w < 10:
        chart_w = 10

    grid = [[' ' for _ in range(chart_w)] for _ in range(chart_height)]
    n = len(bars)
    col_w = chart_w // n if n else 1
    if col_w < 1:
        col_w = 1

    for i, b in enumerate(bars):
        if b['is_total']:
            clr_code = COLORS.get(color_total, '')
        elif values[i] >= 0:
            clr_code = COLORS.get(color_up, '')
        else:
            clr_code = COLORS.get(color_down, '')
        rc = COLORS['reset'] if clr_code else ''
        styled = clr_code + '█' + rc if clr_code else '█'

        top_r = int((max_val - b['start']) / val_range * (chart_height - 1))
        bot_r = int((max_val - b['end']) / val_range * (chart_height - 1))
        if top_r > bot_r:
            top_r, bot_r = bot_r, top_r
        top_r = max(0, min(chart_height - 1, top_r))
        bot_r = max(0, min(chart_height - 1, bot_r))
        left = i * col_w
        right = min(chart_w - 1, left + col_w - 1)

        for r in range(top_r, bot_r + 1):
            for c in range(left, right + 1):
                if 0 <= r < chart_height and 0 <= c < chart_w:
                    grid[r][c] = styled

        conn = COLORS.get('white', '')
        conn_r = COLORS['reset'] if conn else ''
        for c in range(left, left + col_w):
            if 0 <= top_r < chart_height and 0 <= c < chart_w:
                grid[top_r][c] = conn + '─' + conn_r if conn else '─'
            if 0 <= bot_r < chart_height and 0 <= c < chart_w:
                grid[bot_r][c] = conn + '─' + conn_r if conn else '─'

    y_label_width = 6
    display = [[' ' for _ in range(chart_w + y_label_width)] for _ in range(chart_height)]

    for r in range(chart_height):
        y_val = min_val + (chart_height - 1 - r) * (val_range / max(chart_height - 1, 1))
        label = f"{y_val:.1f}"
        for i, ch in enumerate(label):
            if i < y_label_width:
                display[r][i] = ch

    for r in range(chart_height):
        for c in range(chart_w):
            display[r][c + y_label_width] = grid[r][c]

    output.append('+' + '-' * (chart_w + y_label_width) + '+')
    for row in display:
        output.append('|' + ''.join(row) + '|')
    output.append('+' + '-' * (chart_w + y_label_width) + '+')

    label_line = " " * y_label_width
    for i, lb in enumerate(labels):
        left = i * col_w + y_label_width
        if left + len(lb) < len(label_line) or i == n - 1:
            pass
    output.append("")

    for i, lb in enumerate(labels):
        b = bars[i]
        if b['is_total']:
            clr = COLORS.get(color_total, '')
        elif values[i] >= 0:
            clr = COLORS.get(color_up, '')
        else:
            clr = COLORS.get(color_down, '')
        rc = COLORS['reset'] if clr else ''
        sign = "+" if values[i] >= 0 else ""
        total_mark = " = " if b['is_total'] else "  "
        output.append(f"  {clr}█{rc} {lb}{total_mark}{sign}{values[i]:.0f} (cumulative: {b['end']:.0f})")

    if xlabel:
        output.append(f"\n{xlabel.center(chart_w + y_label_width)}")
    output.append("")

    write_output(output, output_file)
    return (output if _return_output else None)
