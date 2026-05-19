import math
from typing import List, Optional, Tuple

from termatplotlib.utils import COLORS, write_output, get_terminal_width, get_default


def violinplot(
    data: List[List[float]],
    labels: Optional[List[str]] = None,
    width: int = 50,
    height: int = 20,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    color: Optional[str] = None,
    output_file: Optional[str] = None,
    _return_output: bool = False,
) -> Optional[List[str]]:
    width = get_default('width') or width
    height = get_default('height') or height
    color = get_default('color') or color or 'cyan'

    output: List[str] = []
    if title:
        output.append(f"\n{title.center(width)}\n")

    if not data or not all(d for d in data):
        output.append("Error: Invalid or empty data.")
        write_output(output, output_file)
        return (output if _return_output else None)

    if labels is None:
        labels = [f"Set {i+1}" for i in range(len(data))]

    all_vals = [v for d in data for v in d]
    min_val = min(all_vals)
    max_val = max(all_vals)
    val_range = max_val - min_val if max_val != min_val else 1

    n_groups = len(data)
    group_width = max(3, width // n_groups)

    display = [[' ' for _ in range(width + 6)] for _ in range(height)]
    color_code = COLORS.get(color, '')
    reset_code = COLORS['reset'] if color_code else ''

    def yrow(v):
        return int((max_val - v) / val_range * (height - 1))

    for gi, vals in enumerate(data):
        if len(vals) < 2:
            continue
        s = sorted(vals)
        n = len(s)
        cx = 6 + gi * group_width + group_width // 2

        # KDE-like density using hist counts mirrored
        nb = max(5, height // 3)
        bin_min, bin_max = min(s), max(s)
        bin_r = (bin_max - bin_min) / nb if bin_max != bin_min else 1
        counts = [0] * nb
        for v in s:
            idx = min(int((v - bin_min) / bin_r), nb - 1)
            counts[idx] += 1
        max_cnt = max(counts) if counts else 1
        half_width = max(1, group_width // 4)

        for bi in range(nb):
            cnt = counts[bi] / max_cnt
            bar_w = max(1, int(cnt * half_width))
            bin_center = bin_min + bi * bin_r + bin_r / 2
            r = yrow(bin_center)
            if 0 <= r < height:
                for c in range(cx - bar_w, cx + bar_w + 1):
                    if 0 <= c < width + 6:
                        display[r][c] = color_code + '█' + reset_code

    # Draw y-axis
    for r in range(height):
        y_val = min_val + (height - 1 - r) * (val_range / max(height - 1, 1))
        if r % (height // 5 if height >= 5 else 1) == 0 or r == 0 or r == height - 1:
            label = f"{y_val:.1f}"
            for i, ch in enumerate(label):
                if i < 6:
                    display[r][i] = ch

    output.append('+' + '-' * (width + 6) + '+')
    for row in display:
        output.append('|' + ''.join(row) + '|')
    output.append('+' + '-' * (width + 6) + '+')

    label_line = " " * 6
    for lbl in labels:
        label_line += lbl.center(group_width)[:group_width]
    output.append(label_line)

    if xlabel:
        output.append(f"\n{xlabel.center(width + 6)}")
    output.append("")

    write_output(output, output_file)
    return (output if _return_output else None)
