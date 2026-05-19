from typing import List, Optional

from termatplotlib.utils import COLORS, write_output, get_terminal_width, get_default


def funnel(
    labels: List[str],
    values: List[float],
    width: Optional[int] = None,
    title: Optional[str] = None,
    color: Optional[str] = None,
    show_percent: bool = True,
    output_file: Optional[str] = None,
    _return_output: bool = False,
) -> Optional[List[str]]:
    width = get_default('width') or width or get_terminal_width()
    color = get_default('color') or color or 'cyan'

    output: List[str] = []
    if title:
        output.append(f"\n{title.center(width)}\n")

    if not labels or not values or len(labels) != len(values):
        output.append("Error: Invalid input.")
        write_output(output, output_file)
        return (output if _return_output else None)

    max_val = max(values) if values else 1
    if max_val <= 0:
        max_val = 1

    max_label = max(len(str(l)) for l in labels)
    bar_w = width - max_label - 12
    if bar_w < 10:
        bar_w = 10

    clr = COLORS.get(color, '')
    rc = COLORS['reset'] if clr else ''
    first_val = values[0] if values else 1

    for i, (label, val) in enumerate(zip(labels, values)):
        pct = val / max_val if max_val else 0
        bar_len = max(1, int(pct * bar_w))
        left_pad = (bar_w - bar_len) // 2
        right_pad = bar_w - bar_len - left_pad

        from_prev = (val / first_val * 100) if first_val else 0
        pct_str = f"  ({from_prev:.0f}%)" if show_percent else ""
        label_str = str(label).ljust(max_label)

        line = "  " + label_str + " "
        line += " " * left_pad
        line += clr + '█' * bar_len + rc if clr else '█' * bar_len
        line += " " * right_pad
        line += f" {val:.0f}{pct_str}"
        output.append(line)

    if show_percent:
        output.append(f"\n  Percentages show value relative to first stage ({labels[0] if labels else ''})")

    output.append("")
    write_output(output, output_file)
    return (output if _return_output else None)
