from typing import List, Optional

from termatplotlib.utils import COLORS, write_output, get_terminal_width, get_default


def strip(
    data: List[float],
    labels: Optional[List[str]] = None,
    width: Optional[int] = None,
    height: int = 5,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    color: Optional[str] = None,
    jitter: bool = True,
    output_file: Optional[str] = None,
    _return_output: bool = False,
) -> Optional[List[str]]:
    width = get_default('width') or width or get_terminal_width()
    color = get_default('color') or color or 'cyan'

    output: List[str] = []
    if title:
        output.append(f"\n{title.center(width)}\n")

    if not data:
        output.append("Error: Empty data.")
        write_output(output, output_file)
        return (output if _return_output else None)

    min_v = min(data)
    max_v = max(data)
    v_range = max_v - min_v if max_v != min_v else 1

    chart_w = width - 8
    if chart_w < 10:
        chart_w = 10

    grid = [[' ' for _ in range(chart_w + 2)] for _ in range(height)]
    clr = COLORS.get(color, '')
    rc = COLORS['reset'] if clr else ''
    dot = clr + '●' + rc if clr else '●'

    counts = [0] * chart_w
    for v in data:
        c = int((v - min_v) / v_range * (chart_w - 1))
        c = max(0, min(chart_w - 1, c))
        counts[c] += 1

    bin_max = max(counts) if counts else 1
    for c in range(chart_w):
        n = counts[c]
        col_height = max(1, int(n / bin_max * height)) if n > 0 else 0
        for r in range(height - col_height, height):
            if 0 <= r < height and 0 <= c < chart_w + 2:
                grid[r][c + 1] = dot

    y_label = f"{min_v:.1f}".rjust(6)
    output.append(f"  {y_label} +{'-' * chart_w}+")
    for row in grid:
        output.append("  " + ''.join(row))
    y_label2 = f"{max_v:.1f}".rjust(6)
    output.append(f"  {y_label2} +{'-' * chart_w}+")

    if xlabel:
        output.append(f"\n{xlabel.center(width)}")
    output.append(f"\n  n={len(data)}  min={min_v:.1f}  max={max_v:.1f}  range={v_range:.1f}")
    output.append("")

    write_output(output, output_file)
    return (output if _return_output else None)
