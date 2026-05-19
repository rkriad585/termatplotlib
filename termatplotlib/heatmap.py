import math
from typing import List, Optional

from termatplotlib.utils import COLORS, write_output, get_terminal_width, get_default

INTENSITY_CHARS = [' ', '░', '▒', '▓', '█']


def heatmap(
    data: List[List[float]],
    row_labels: Optional[List[str]] = None,
    col_labels: Optional[List[str]] = None,
    title: Optional[str] = None,
    color: Optional[str] = None,
    palette: Optional[List[str]] = None,
    width: Optional[int] = None,
    output_file: Optional[str] = None,
    _return_output: bool = False,
) -> Optional[List[str]]:
    color = get_default('color') or color
    width = get_default('width') or width

    output: List[str] = []

    if not data or not data[0]:
        output.append("Error: Data cannot be empty.")
        write_output(output, output_file)
        return (output if _return_output else None)

    n_rows = len(data)
    n_cols = len(data[0])

    for row in data:
        if len(row) != n_cols:
            output.append("Error: All rows must have the same length.")
            write_output(output, output_file)
            return (output if _return_output else None)

    if row_labels is not None and len(row_labels) != n_rows:
        output.append("Error: row_labels length must match number of data rows.")
        write_output(output, output_file)
        return (output if _return_output else None)

    if col_labels is not None and len(col_labels) != n_cols:
        output.append("Error: col_labels length must match number of data columns.")
        write_output(output, output_file)
        return (output if _return_output else None)

    if title:
        output.append(f"\n{title.center(width if width else 80)}\n")

    flat = [v for row in data for v in row]
    vmin = min(flat)
    vmax = max(flat)
    vrange = vmax - vmin if vmax != vmin else 1

    if palette is None:
        palette = [color] if color else ['white']

    max_label_len = max(
        len(str(l)) for l in (row_labels or [])
    ) if row_labels else 0

    cell_w = 2
    for cl in (col_labels or []):
        cell_w = max(cell_w, len(str(cl)))

    for i, row in enumerate(data):
        line = ""
        if row_labels:
            line += f"{str(row_labels[i]):<{max_label_len}} "
        for val in row:
            norm = (val - vmin) / vrange
            intensity = min(int(norm * 4), 4)
            p = palette[int(norm * (len(palette) - 1))] if len(palette) > 1 else palette[0]
            c = COLORS.get(p, '')
            r = COLORS['reset'] if c else ''
            char = c + INTENSITY_CHARS[intensity] + r
            line += char * cell_w
        output.append(line)

    if col_labels:
        line = ""
        if row_labels:
            line += " " * (max_label_len + 1)
        for cl in col_labels:
            line += str(cl).center(cell_w)
        output.append(line)

    output.append("")

    write_output(output, output_file)
    return (output if _return_output else None)
