from termatplotlib.utils import COLORS, write_output, get_terminal_width, validate_data, format_plot_lines


def scatter(data, width=50, height=20, title=None, xlabel=None, ylabel=None, output_file=None, color=None, legend=False):
    output = []
    if title:
        output.append(f"\n{title.center(width)}\n")

    try:
        all_x, all_y = validate_data(data)
    except ValueError as e:
        output.append(f"Error: {e}")
        write_output(output, output_file)
        return

    min_x, max_x = min(all_x), max(all_x)
    min_y, max_y = min(all_y), max(all_y)
    x_range = max_x - min_x
    y_range = max_y - min_y

    grid = [[' ' for _ in range(width)] for _ in range(height)]

    for series in data:
        sx = series['x']
        sy = series['y']
        series_color = series.get('color') or color or 'white'
        marker = series.get('marker', '*')

        color_code = COLORS.get(series_color, '')
        reset_code = COLORS['reset'] if color_code else ''

        for i in range(len(sx)):
            x_scaled = int(((sx[i] - min_x) / x_range) * (width - 1)) if x_range != 0 else 0
            y_scaled = int(((sy[i] - min_y) / y_range) * (height - 1)) if y_range != 0 else 0
            grid[height - 1 - y_scaled][x_scaled] = color_code + marker + reset_code

    plot_lines = format_plot_lines(grid, width, height, min_x, max_x, min_y, max_y, xlabel, ylabel)
    output.extend(plot_lines)

    if legend:
        output.append("Legend:")
        for i, series in enumerate(data):
            label = series.get('label', f'Series {i+1}')
            series_color = series.get('color') or color or 'white'
            c = COLORS.get(series_color, '')
            marker = series.get('marker', '*')
            output.append(f"  {c}{marker}{COLORS['reset']} {label}")
        output.append("")

    write_output(output, output_file)
