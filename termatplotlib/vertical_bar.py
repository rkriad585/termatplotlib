from typing import List, Optional

from termatplotlib.utils import COLORS, write_output, get_terminal_width, get_default


def vertical_bar(
    labels: List[str],
    values: List[float],
    height: Optional[int] = None,
    width: Optional[int] = None,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    color: Optional[str] = None,
    output_file: Optional[str] = None,
    _return_output: bool = False,
) -> Optional[List[str]]:
    height = get_default('height') or height or 15
    width = get_default('width') or width or get_terminal_width(60)
    color = get_default('color') or color

    output: List[str] = []
    if title:
        output.append(f"\n{title.center(width)}\n")

    if not labels or not values or len(labels) != len(values):
        output.append("Error: Invalid input.")
        write_output(output, output_file)
        return (output if _return_output else None)

    max_val = max(abs(v) for v in values)
    if max_val == 0:
        max_val = 1

    n = len(labels)
    col_w = max(3, (width - 2) // n)
    scale = (height - 2) / max_val

    color_code = COLORS.get(color, '')
    reset_code = COLORS['reset'] if color_code else ''

    for r in range(height - 2, -1, -1):
        thresh = r / scale if scale else 0
        line = " "
        for v in values:
            bar_h = int(abs(v) * scale)
            if bar_h > r:
                line += color_code + '█' * col_w + reset_code
            else:
                line += ' ' * col_w
            line += " "
        output.append(line)

    sep = " " + "-" * (n * (col_w + 1))
    output.append(sep)

    label_line = " "
    for lbl in labels:
        label_line += str(lbl).center(col_w + 1)
    output.append(label_line)

    if xlabel:
        output.append(f"\n{xlabel.center(width)}")
    output.append("")

    write_output(output, output_file)
    return (output if _return_output else None)
