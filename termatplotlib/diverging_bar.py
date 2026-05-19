from typing import List, Optional

from termatplotlib.utils import COLORS, COLOR_NAMES, write_output, get_terminal_width, get_default


def diverging_bar(
    labels: List[str],
    values: List[float],
    baseline: float = 0,
    max_width: Optional[int] = None,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    colors: Optional[List[str]] = None,
    output_file: Optional[str] = None,
    _return_output: bool = False,
) -> Optional[List[str]]:
    max_width = get_default('max_width') or max_width or get_terminal_width()
    colors = get_default('colors') or colors

    output: List[str] = []
    if title:
        output.append(f"\n{title.center(max_width)}\n")

    if not labels or not values or len(labels) != len(values):
        output.append("Error: Invalid input.")
        write_output(output, output_file)
        return (output if _return_output else None)

    if colors is None:
        colors = ['green', 'red']

    above = [max(0, v - baseline) for v in values]
    below = [max(0, baseline - v) for v in values]
    max_abs = max(max(above), max(below)) if above or below else 1

    max_label_len = max(len(str(l)) for l in labels)
    avail = max_width - max_label_len - 5
    if avail < 10:
        avail = 10
    scale = avail / max_abs

    c_above = COLORS.get(colors[0], '')
    c_below = COLORS.get(colors[1] if len(colors) > 1 else colors[0], '')
    r = COLORS['reset']
    ca_r = c_above + r if c_above else ''
    cb_r = c_below + r if c_below else ''

    if ylabel:
        output.append(f"{ylabel.rjust(max_label_len)}")

    midline = max_label_len + 3
    for i, label in enumerate(labels):
        a_len = int(above[i] * scale)
        b_len = int(below[i] * scale)
        prefix = str(label).ljust(max_label_len) + " | "
        left = (c_below + '█' * b_len + r) if b_len else ""
        right = (c_above + '█' * a_len + r) if a_len else ""
        val_str = f"{values[i]:+}"
        output.append(f"{prefix}{left}{'│' if a_len and b_len else ' '}{right} {val_str}")

    if xlabel:
        output.append(f"\n{xlabel.center(max_width)}")

    output.append("")
    output.append(f"  {ca_r} Above {baseline}{COLORS['reset']}")
    output.append(f"  {cb_r} Below {baseline}{COLORS['reset']}")
    output.append("")

    write_output(output, output_file)
    return (output if _return_output else None)
