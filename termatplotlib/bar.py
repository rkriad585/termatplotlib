from termatplotlib.utils import COLORS, COLOR_NAMES, write_output, get_terminal_width


def bar(labels, values, max_width=None, title=None, xlabel=None, ylabel=None, color=None, output_file=None):
    if max_width is None:
        max_width = get_terminal_width()

    output = []
    if title:
        output.append(f"\n{title.center(max_width)}\n")

    if not labels or not values or len(labels) != len(values):
        output.append("Error: Invalid input. Labels and values must be non-empty and of the same length.")
        write_output(output, output_file)
        return

    max_label_len = max(len(str(label)) for label in labels)
    abs_values = [abs(v) for v in values]
    max_abs = max(abs_values) if abs_values else 1
    available_width = max_width - max_label_len - 5
    if available_width < 10:
        available_width = 10
    scale = available_width / max_abs

    color_code = COLORS.get(color, '')
    reset_code = COLORS['reset'] if color_code else ''

    if ylabel:
        output.append(f"{ylabel.rjust(max_label_len)}")

    for label, value in zip(labels, values):
        bar_len = int(abs(value) * scale)
        bar_str = '█' * bar_len
        if value < 0:
            bar_str = color_code + bar_str + reset_code + ' <'
        else:
            bar_str = color_code + bar_str + reset_code
        output.append(f"{str(label):<{max_label_len}} | {bar_str} {value}")

    if xlabel:
        output.append(f"\n{xlabel.center(max_width)}")

    write_output(output, output_file)


def grouped_bar(labels, values, max_width=None, title=None, xlabel=None, ylabel=None, colors=None, output_file=None):
    if max_width is None:
        max_width = get_terminal_width()

    output = []
    if title:
        output.append(f"\n{title.center(max_width)}\n")

    if not labels or not values:
        output.append("Error: Invalid input.")
        write_output(output, output_file)
        return

    if not colors:
        colors = COLOR_NAMES[:len(values)]

    n_series = len(values)
    for s_vals in values:
        if len(s_vals) != len(labels):
            output.append("Error: Each series must have the same number of values as labels.")
            write_output(output, output_file)
            return

    max_label_len = max(len(str(label)) for label in labels)
    all_abs = [abs(v) for series in values for v in series]
    max_abs = max(all_abs) if all_abs else 1
    available_width = max_width - max_label_len - 5 - n_series
    if available_width < 10:
        available_width = 10
    bar_width = max(available_width // max_abs, 0)

    if ylabel:
        output.append(f"{ylabel.rjust(max_label_len)}")

    for i, label in enumerate(labels):
        line = f"{str(label):<{max_label_len}} | "
        for j in range(n_series):
            c = COLORS.get(colors[j % len(colors)], '')
            r = COLORS['reset'] if c else ''
            val = abs(values[j][i])
            bar_len = int(val * bar_width)
            line += c + '█' * max(bar_len, 0) + r
            if j < n_series - 1:
                line += ' '
        line += f" {sum(values[j][i] for j in range(n_series))}"
        output.append(line)

    if xlabel:
        output.append(f"\n{xlabel.center(max_width)}")

    if colors:
        output.append("")
        for j in range(n_series):
            c = COLORS.get(colors[j % len(colors)], '')
            label = f"Series {j+1}"
            output.append(f"  {c}█{COLORS['reset']} {label}")

    write_output(output, output_file)


def stacked_bar(labels, values, max_width=None, title=None, xlabel=None, ylabel=None, colors=None, output_file=None):
    if max_width is None:
        max_width = get_terminal_width()

    output = []
    if title:
        output.append(f"\n{title.center(max_width)}\n")

    if not labels or not values:
        output.append("Error: Invalid input.")
        write_output(output, output_file)
        return

    if not colors:
        colors = COLOR_NAMES[:len(values)]

    n_series = len(values)
    for s_vals in values:
        if len(s_vals) != len(labels):
            output.append("Error: Each series must have the same number of values as labels.")
            write_output(output, output_file)
            return

    max_label_len = max(len(str(label)) for label in labels)
    totals = [sum(values[j][i] for j in range(n_series)) for i in range(len(labels))]
    max_total = max(totals) if totals else 1
    available_width = max_width - max_label_len - 5
    if available_width < 10:
        available_width = 10
    scale = available_width / max_total

    if ylabel:
        output.append(f"{ylabel.rjust(max_label_len)}")

    for i, label in enumerate(labels):
        line = f"{str(label):<{max_label_len}} | "
        for j in range(n_series):
            c = COLORS.get(colors[j % len(colors)], '')
            r = COLORS['reset'] if c else ''
            val = abs(values[j][i])
            bar_len = int(val * scale)
            line += c + '█' * max(bar_len, 0) + r
        line += f" {totals[i]}"
        output.append(line)

    if xlabel:
        output.append(f"\n{xlabel.center(max_width)}")

    if colors:
        output.append("")
        for j in range(n_series):
            c = COLORS.get(colors[j % len(colors)], '')
            label = f"Series {j+1}"
            output.append(f"  {c}█{COLORS['reset']} {label}")

    write_output(output, output_file)
