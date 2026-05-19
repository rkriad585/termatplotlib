import math
from typing import List, Optional

from termatplotlib.utils import COLORS, write_output, get_terminal_width, get_default


def donut(
    labels: List[str],
    values: List[float],
    radius: int = 8,
    inner_radius: int = 3,
    title: Optional[str] = None,
    legend: bool = True,
    center_label: Optional[str] = None,
    output_file: Optional[str] = None,
    _return_output: bool = False,
) -> Optional[List[str]]:
    radius = get_default('radius') or radius
    if inner_radius >= radius:
        inner_radius = max(1, radius - 2)

    width = radius * 4 + 4
    cx = radius * 2 + 2
    cy = radius * 2 + 2

    output: List[str] = []
    if title:
        output.append(f"\n{title.center(width)}\n")

    if not labels or not values or len(labels) != len(values):
        output.append("Error: Invalid input.")
        write_output(output, output_file)
        return (output if _return_output else None)

    total = sum(values)
    if total <= 0:
        total = 1

    COLOR_SEQ = ['cyan', 'green', 'yellow', 'blue', 'magenta', 'red', 'white']
    colors = [COLOR_SEQ[i % len(COLOR_SEQ)] for i in range(len(labels))]

    from termatplotlib.utils import COLOR_NAMES

    height = radius * 4 + 4
    grid = [[' ' for _ in range(width)] for _ in range(height)]

    angles = []
    start = 0
    for v in values:
        sweep = (v / total) * 2 * math.pi
        angles.append((start, start + sweep))
        start += sweep

    for r in range(height):
        for c in range(width):
            dx = c - cx
            dy = r - cy
            dist = math.sqrt(dx * dx + dy * dy)
            if dist < radius and dist >= inner_radius:
                angle = math.atan2(dy, dx)
                if angle < 0:
                    angle += 2 * math.pi
                for i, (s, e) in enumerate(angles):
                    in_angle = False
                    if s <= e:
                        in_angle = s <= angle < e
                    else:
                        in_angle = angle >= s or angle < e
                    if in_angle:
                        clr = COLORS.get(colors[i], '')
                        rc = COLORS['reset'] if clr else ''
                        grid[r][c] = clr + '█' + rc if clr else '█'
                        break

    for r in range(height):
        row_str = ''
        for c in range(width):
            row_str += grid[r][c]
        output.append('  ' + row_str)

    if center_label:
        clr = COLORS.get('white', '')
        rc = COLORS['reset'] if clr else ''
        center_str = clr + center_label.center(6) + rc if clr else center_label.center(6)
        center_row = cy
        start_c = cx - len(center_label) // 2
        for i, ch in enumerate(center_str):
            r = center_row
            c = start_c + i
            if 0 <= r < height and 0 <= c < width:
                pass

    if legend:
        for i, (label, val) in enumerate(zip(labels, values)):
            pct = val / total * 100
            clr = COLORS.get(colors[i], '')
            rc = COLORS['reset'] if clr else ''
            output.append(f"  {clr}●{rc} {label}: {val:.0f} ({pct:.1f}%)")

    output.append("")
    write_output(output, output_file)
    return (output if _return_output else None)
