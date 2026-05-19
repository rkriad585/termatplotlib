from typing import List, Optional

from termatplotlib.utils import COLORS, write_output, get_terminal_width


def hist(
    data: List[float],
    bins: int = 10,
    width: Optional[int] = None,
    height: int = 10,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    color: Optional[str] = None,
    char: str = '█',
    output_file: Optional[str] = None,
) -> None:
    if width is None:
        width = get_terminal_width()

    output: List[str] = []
    if title:
        output.append(f"\n{title.center(width)}\n")

    if not data:
        output.append("Error: Input data cannot be empty.")
        write_output(output, output_file)
        return

    min_val, max_val = min(data), max(data)
    if min_val == max_val:
        output.append("Error: All data points are the same, cannot create meaningful bins.")
        write_output(output, output_file)
        return

    bin_range = (max_val - min_val) / bins
    counts = [0] * bins

    for x in data:
        if x == max_val:
            counts[-1] += 1
        else:
            idx = int((x - min_val) / bin_range)
            if idx < 0:
                idx = 0
            elif idx >= bins:
                idx = bins - 1
            counts[idx] += 1

    max_count = max(counts)
    if max_count == 0:
        output.append("No data points fell into any bin.")
        write_output(output, output_file)
        return

    scale = height / max_count
    color_code = COLORS.get(color, '')
    reset_code = COLORS['reset'] if color_code else ''

    y_label_width = len(str(max_count)) + 1

    for h in range(height - 1, -1, -1):
        y_tick = int(max_count * h / max(height - 1, 1))
        show_label = (
            h == height - 1 or h == 0 or
            (height >= 5 and h % (height // 5) == 0)
        )
        if show_label:
            row_str = str(y_tick).rjust(y_label_width)
        else:
            row_str = " " * y_label_width

        for i in range(bins):
            bar_visual_width = width // bins
            if counts[i] * scale > h:
                row_str += color_code + char + reset_code + " " * max(bar_visual_width - 1, 0)
            else:
                row_str += " " * bar_visual_width
        output.append(row_str)

    separator = "-" * (width + y_label_width)
    output.append(separator)

    bin_edges = [min_val + i * bin_range for i in range(bins + 1)]
    label_spacing = width // bins
    label_line = " " * y_label_width
    for i in range(bins):
        lbl = f"{bin_edges[i]:.1f}"
        label_line += lbl.ljust(label_spacing)[:label_spacing]
    output.append(label_line)

    if xlabel:
        output.append(f"\n{xlabel.center(width + y_label_width)}")
    if ylabel:
        output.append(f"{'':>{y_label_width}}{ylabel} (count)")
    output.append("\n")

    write_output(output, output_file)
