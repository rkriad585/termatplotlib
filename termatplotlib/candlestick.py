import math
from typing import List, Optional, Tuple

from termatplotlib.utils import COLORS, write_output, get_terminal_width, get_default


def candlestick(
    data: List[dict],
    width: int = 50,
    height: int = 20,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    output_file: Optional[str] = None,
    color_up: Optional[str] = None,
    color_down: Optional[str] = None,
    _return_output: bool = False,
) -> Optional[List[str]]:
    width = get_default('width') or width
    height = get_default('height') or height
    color_up = get_default('color') or color_up or 'green'
    color_down = get_default('color_secondary') or color_down or 'red'

    output: List[str] = []
    if title:
        output.append(f"\n{title.center(width)}\n")

    if not data:
        output.append("Error: Empty data.")
        write_output(output, output_file)
        return (output if _return_output else None)

    all_high = [d['high'] for d in data]
    all_low = [d['low'] for d in data]
    min_val = min(all_low)
    max_val = max(all_high)
    val_range = max_val - min_val if max_val != min_val else 1

    grid = [[' ' for _ in range(width)] for _ in range(height)]
    n = len(data)
    col_w = max(3, width // n)
    cu = COLORS.get(color_up, '')
    cd = COLORS.get(color_down, '')
    rc = COLORS['reset'] if (cu or cd) else ''

    for i, d in enumerate(data):
        o, h, l, c_val = d['open'], d['high'], d['low'], d['close']
        cx = i * col_w + col_w // 2
        is_up = c_val >= o
        clr = cu if is_up else cd
        styled = clr + '│' + rc if clr else '│'

        def yrow(v):
            return int((max_val - v) / val_range * (height - 1))

        top = yrow(h)
        bot = yrow(l)
        open_r = yrow(o)
        close_r = yrow(c_val)
        body_top = min(open_r, close_r)
        body_bot = max(open_r, close_r)

        for r in range(top, bot + 1):
            if 0 <= r < height and 0 <= cx < width:
                grid[r][cx] = styled

        for r in range(body_top, body_bot + 1):
            left = max(0, cx - col_w // 4)
            right = min(width - 1, cx + col_w // 4)
            for c in range(left, right + 1):
                if 0 <= r < height and 0 <= c < width:
                    grid[r][c] = clr + '█' + rc if clr else '█'

    from termatplotlib.utils import format_plot_lines
    lines = format_plot_lines(grid, width, height, 0, n, min_val, max_val, xlabel, ylabel)
    output.extend(lines)

    write_output(output, output_file)
    return (output if _return_output else None)
