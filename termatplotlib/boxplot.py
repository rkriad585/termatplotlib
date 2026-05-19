import math

from termatplotlib.utils import COLORS, write_output, get_terminal_width


def _quartiles(data):
    s = sorted(data)
    n = len(s)
    q2 = s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2
    lower = s[:n // 2] if n % 2 else s[:n // 2]
    upper = s[(n + 1) // 2:] if n % 2 else s[n // 2:]
    q1 = lower[len(lower) // 2] if len(lower) % 2 else (lower[len(lower) // 2 - 1] + lower[len(lower) // 2]) / 2
    q3 = upper[len(upper) // 2] if len(upper) % 2 else (upper[len(upper) // 2 - 1] + upper[len(upper) // 2]) / 2
    return q1, q2, q3


def boxplot(data, labels=None, width=50, height=20, title=None, xlabel=None, ylabel=None, output_file=None, color=None):
    output = []
    if title:
        output.append(f"\n{title.center(width)}\n")

    if not data:
        output.append("Error: Input data cannot be empty.")
        write_output(output, output_file)
        return

    if labels is None:
        labels = [f"Set {i+1}" for i in range(len(data))]

    stats = []
    all_vals = []
    for d in data:
        if not d:
            output.append("Error: Empty dataset found.")
            write_output(output, output_file)
            return
        mn, mx = min(d), max(d)
        q1, med, q3 = _quartiles(d)
        iqr = q3 - q1
        lower_whisker = max(mn, q1 - 1.5 * iqr)
        upper_whisker = min(mx, q3 + 1.5 * iqr)
        stats.append((lower_whisker, q1, med, q3, upper_whisker, mn, mx))
        all_vals.extend([lower_whisker, q1, med, q3, upper_whisker])

    min_val = min(all_vals)
    max_val = max(all_vals)
    val_range = max_val - min_val if max_val != min_val else 1

    n_groups = len(data)
    group_width = width // n_groups if n_groups > 0 else width
    box_width = max(3, group_width - 4)

    color_code = COLORS.get(color, '')
    reset_code = COLORS['reset'] if color_code else ''

    y_label_width = len(f"{max_val:.1f}") + 2

    display = [[' ' for _ in range(width + y_label_width)] for _ in range(height)]

    for r in range(height):
        y_val = min_val + (height - 1 - r) * (val_range / max(height - 1, 1))
        if r % (height // 5 if height >= 5 else 1) == 0 or r == 0 or r == height - 1:
            label = f"{y_val:.1f}"
            for i, ch in enumerate(label):
                if i < y_label_width:
                    display[r][i] = ch

    for g_idx, (lower_whisker, q1, med, q3, upper_whisker, mn, mx) in enumerate(stats):
        cx = y_label_width + g_idx * group_width + group_width // 2
        left = cx - box_width // 2
        right = cx + box_width // 2

        def y_to_row(val):
            return int((max_val - val) / val_range * (height - 1))

        q1_row = y_to_row(q1)
        q3_row = y_to_row(q3)
        med_row = y_to_row(med)
        lower_row = y_to_row(lower_whisker)
        upper_row = y_to_row(upper_whisker)
        mn_row = y_to_row(mn)
        mx_row = y_to_row(mx)

        for r in range(min(q1_row, q3_row), max(q1_row, q3_row) + 1):
            for c in range(left, right + 1):
                if 0 <= r < height and 0 <= c < width + y_label_width:
                    if r == q1_row or r == q3_row or c == left or c == right:
                        display[r][c] = color_code + '█' + reset_code
                    else:
                        display[r][c] = color_code + '░' + reset_code

        if 0 <= med_row < height:
            for c in range(left, right + 1):
                if 0 <= c < width + y_label_width:
                    display[med_row][c] = color_code + '━' + reset_code

        if 0 <= cx < width + y_label_width:
            for r in range(min(lower_row, upper_row), max(lower_row, upper_row) + 1):
                if 0 <= r < height:
                    if r < min(q1_row, q3_row) or r > max(q1_row, q3_row):
                        display[r][cx] = color_code + '│' + reset_code

            if 0 <= lower_row < height:
                for c in range(left, right + 1):
                    if 0 <= c < width + y_label_width:
                        display[lower_row][c] = color_code + '╶' + reset_code

            if 0 <= upper_row < height:
                for c in range(left, right + 1):
                    if 0 <= c < width + y_label_width:
                        display[upper_row][c] = color_code + '╶' + reset_code

    output.append('+' + '-' * (width + y_label_width) + '+')
    for row in display:
        output.append('|' + ''.join(row) + '|')
    output.append('+' + '-' * (width + y_label_width) + '+')

    label_line = " " * y_label_width
    for i, lbl in enumerate(labels):
        cx_pos = y_label_width + i * group_width + group_width // 2
        label_line += lbl.center(group_width)[:group_width]
    output.append(label_line)

    if xlabel:
        output.append(f"\n{xlabel.center(width + y_label_width)}")

    output.append("\nLegend:")
    output.append(f"  {color_code}█{reset_code} Box (Q1–Q3)")
    output.append(f"  {color_code}━{reset_code} Median")
    output.append(f"  {color_code}│{reset_code} Whiskers")
    output.append("")

    write_output(output, output_file)
