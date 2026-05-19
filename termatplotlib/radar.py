import math
from typing import List, Optional

from termatplotlib.utils import COLORS, COLOR_NAMES, write_output, get_terminal_width, get_default


def radar(
    labels: List[str],
    values: List[float],
    width: int = 40,
    title: Optional[str] = None,
    fill: bool = False,
    color: Optional[str] = None,
    colors_list: Optional[List[str]] = None,
    scale_max: Optional[float] = None,
    output_file: Optional[str] = None,
    _return_output: bool = False,
) -> Optional[List[str]]:
    width = get_default('width') or width
    color = get_default('color') or color

    cx = width // 2
    cy = width // 2
    r = cx - 4

    if r < 3:
        r = 3
        cx = r + 4
        cy = r + 4
        width = cx * 2 + 2

    height = width

    output: List[str] = []
    if title:
        output.append(f"\n{title.center(width)}\n")

    n = len(labels)
    if n < 3:
        output.append("Error: Need at least 3 categories.")
        write_output(output, output_file)
        return (output if _return_output else None)

    if len(values) != n:
        output.append("Error: labels/values length mismatch.")
        write_output(output, output_file)
        return (output if _return_output else None)

    mx = scale_max if scale_max is not None else max(values) if values else 1
    if mx <= 0:
        mx = 1

    grid = [[' ' for _ in range(width)] for _ in range(height)]

    ring_colors = COLORS.get('white', '')
    ring_reset = COLORS['reset'] if ring_colors else ''

    for ring_pct in [0.25, 0.5, 0.75, 1.0]:
        ring_r = int(r * ring_pct)
        for angle_i in range(72):
            a = 2 * math.pi * angle_i / 72
            cr = int(cx + ring_r * math.sin(a))
            cc = int(cy + ring_r * math.cos(a))
            if 0 <= cr < height and 0 <= cc < width:
                ch = '·'
                if ring_pct == 1.0:
                    ch = 'o'
                grid[cr][cc] = ring_colors + ch + ring_reset if ring_colors else ch

    angles = [2 * math.pi * i / n - math.pi / 2 for i in range(n)]
    for i in range(n):
        a1 = angles[i]
        a2 = angles[(i + 1) % n]
        step = 36
        for t in range(step + 1):
            frac = t / step
            a = a1 + (a2 - a1) * frac
            rr = int(cx + r * math.sin(a))
            cc = int(cy + r * math.cos(a))
            if 0 <= rr < height and 0 <= cc < width:
                if grid[rr][cc] == ' ' or grid[rr][cc] == '·' or 'o' in grid[rr][cc]:
                    grid[rr][cc] = ring_colors + '+' + ring_reset if ring_colors else '+'

    if colors_list is None:
        colors_list = [color] * n if color else [COLOR_NAMES[i % len(COLOR_NAMES)] for i in range(n)]

    for s_idx in range(1):
        pts = []
        for i in range(n):
            frac = values[i] / mx if mx else 0
            dist = r * frac
            a = angles[i]
            rr = int(cx + dist * math.sin(a))
            cc = int(cy + dist * math.cos(a))
            rr = max(0, min(height - 1, rr))
            cc = max(0, min(width - 1, cc))
            pts.append((rr, cc))

        if fill:
            for i in range(n):
                x1, y1 = pts[i][1], pts[i][0]
                x2, y2 = pts[(i + 1) % n][1], pts[(i + 1) % n][0]
                steps = max(abs(x2 - x1), abs(y2 - y1)) * 2
                if steps < 1:
                    steps = 1
                for t in range(steps + 1):
                    frac = t / steps
                    x = int(x1 + (x2 - x1) * frac)
                    y = int(y1 + (y2 - y1) * frac)
                    if 0 <= y < height and 0 <= x < width:
                        clr = COLORS.get(colors_list[i % len(colors_list)], '')
                        rcc = COLORS['reset'] if clr else ''
                        grid[y][x] = clr + '░' + rcc if clr else '░'

        for i in range(n):
            a = angles[i]
            dist = values[i] / mx * r if mx else 0
            rr = int(cx + dist * math.sin(a))
            cc = int(cy + dist * math.cos(a))
            rr = max(0, min(height - 1, rr))
            cc = max(0, min(width - 1, cc))
            clr = COLORS.get(colors_list[i % len(colors_list)], '')
            rcc = COLORS['reset'] if clr else ''
            grid[rr][cc] = clr + '●' + rcc if clr else '●'

    for i in range(n):
        x1, y1 = pts[i][1], pts[i][0]
        x2, y2 = pts[(i + 1) % n][1], pts[(i + 1) % n][0]
        steps = max(abs(x2 - x1), abs(y2 - y1))
        if steps < 1:
            steps = 1
        clr = COLORS.get(colors_list[i % len(colors_list)], '')
        rcc = COLORS['reset'] if clr else ''
        for t in range(steps + 1):
            frac = t / steps
            x = int(x1 + (x2 - x1) * frac)
            y = int(y1 + (y2 - y1) * frac)
            if 0 <= y < height and 0 <= x < width:
                if grid[y][x] == ' ' or grid[y][x] == '·':
                    grid[y][x] = clr + '─' + rcc if clr else '─'

    for row in grid:
        output.append('  ' + ''.join(row))

    max_ll = max(len(str(l)) for l in labels)
    for i in range(n):
        a = angles[i]
        dist = r + 2
        rr = int(cx + dist * math.sin(a))
        cc = int(cy + dist * math.cos(a))
        rr = max(0, min(height - 1, rr))
        cc = max(0, min(width - 1, cc))
        clr = COLORS.get(colors_list[i % len(colors_list)], '')
        rcc = COLORS['reset'] if clr else ''
        line = grid[rr] if rr < len(grid) else []
        label = f" {labels[i]} ({values[i]})"
        label_str = clr + label + rcc if clr else label
        if isinstance(line, list) and cc < len(line):
            pass

    output.append("")
    for i in range(n):
        clr = COLORS.get(colors_list[i % len(colors_list)], '')
        rcc = COLORS['reset'] if clr else ''
        output.append(f"  {clr}●{rcc} {labels[i]}: {values[i]}")

    output.append("")
    write_output(output, output_file)
    return (output if _return_output else None)
