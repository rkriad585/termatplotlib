from typing import List, Optional, Tuple

from termatplotlib.utils import COLORS, write_output, validate_data, format_plot_lines


def _plot_line_segment(
    grid: List[List[str]],
    width: int,
    height: int,
    x0: int,
    y0: int,
    x1: int,
    y1: int,
    color_code: str,
    marker: str,
    reset_code: str,
) -> None:
    dx = abs(x1 - x0)
    dy = -abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx + dy

    while True:
        if 0 <= y0 < height and 0 <= x0 < width:
            grid[y0][x0] = color_code + marker + reset_code
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy


def _scale_point(
    x: float,
    y: float,
    min_x: float,
    max_x: float,
    min_y: float,
    max_y: float,
    width: int,
    height: int,
) -> Tuple[int, int]:
    x_range = max_x - min_x
    y_range = max_y - min_y
    xs = int(((x - min_x) / x_range) * (width - 1)) if x_range != 0 else 0
    ys = int(((y - min_y) / y_range) * (height - 1)) if y_range != 0 else 0
    return xs, height - 1 - ys


def line(
    data: List[dict],
    width: int = 50,
    height: int = 20,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    output_file: Optional[str] = None,
    color: Optional[str] = None,
    legend: bool = False,
    grid: bool = False,
    xlim: Optional[Tuple[float, float]] = None,
    ylim: Optional[Tuple[float, float]] = None,
) -> None:
    output: List[str] = []
    if title:
        output.append(f"\n{title.center(width)}\n")

    try:
        all_x, all_y = validate_data(data)
    except ValueError as e:
        output.append(f"Error: {e}")
        write_output(output, output_file)
        return

    if xlim:
        min_x, max_x = xlim
    else:
        min_x, max_x = min(all_x), max(all_x)
    if ylim:
        min_y, max_y = ylim
    else:
        min_y, max_y = min(all_y), max(all_y)

    grid_chart = [[' ' for _ in range(width)] for _ in range(height)]

    for series in data:
        sx = series['x']
        sy = series['y']
        series_color = series.get('color') or color or 'white'
        marker = series.get('marker', '*')

        color_code = COLORS.get(series_color, '')
        reset_code = COLORS['reset'] if color_code else ''

        scaled = [_scale_point(sx[i], sy[i], min_x, max_x, min_y, max_y, width, height)
                  for i in range(len(sx))]

        for i in range(len(scaled) - 1):
            _plot_line_segment(grid_chart, width, height,
                               scaled[i][0], scaled[i][1],
                               scaled[i + 1][0], scaled[i + 1][1],
                               color_code, marker, reset_code)

    plot_lines = format_plot_lines(grid_chart, width, height, min_x, max_x, min_y, max_y, xlabel, ylabel, grid_lines=grid)
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


def area(
    data: List[dict],
    width: int = 50,
    height: int = 20,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    output_file: Optional[str] = None,
    color: Optional[str] = None,
    stacked: bool = False,
    legend: bool = False,
    grid: bool = False,
    xlim: Optional[Tuple[float, float]] = None,
    ylim: Optional[Tuple[float, float]] = None,
) -> None:
    output: List[str] = []
    if title:
        output.append(f"\n{title.center(width)}\n")

    try:
        all_x, all_y = validate_data(data)
    except ValueError as e:
        output.append(f"Error: {e}")
        write_output(output, output_file)
        return

    if stacked:
        n = len(data[0]['x'])
        base = [0.0] * n
        for series in data:
            for i in range(len(series['y'])):
                series['y'][i] += base[i]
                base[i] = series['y'][i]
        _, all_y = validate_data(data)

    if xlim:
        min_x, max_x = xlim
    else:
        min_x, max_x = min(all_x), max(all_x)
    if ylim:
        min_y, max_y = ylim
    else:
        min_y, max_y = min(all_y), max(all_y)

    grid_chart = [[' ' for _ in range(width)] for _ in range(height)]

    for series in data:
        sx = series['x']
        sy = series['y']
        series_color = series.get('color') or color or 'white'
        marker = series.get('marker', '*')

        color_code = COLORS.get(series_color, '')
        reset_code = COLORS['reset'] if color_code else ''

        scaled = [_scale_point(sx[i], sy[i], min_x, max_x, min_y, max_y, width, height)
                  for i in range(len(sx))]

        for i in range(len(scaled) - 1):
            _plot_line_segment(grid_chart, width, height,
                               scaled[i][0], scaled[i][1],
                               scaled[i + 1][0], scaled[i + 1][1],
                               color_code, marker, reset_code)

        fill_char = marker if marker != '*' else '░'
        _fill_under_segments(grid_chart, width, height, scaled, color_code, fill_char, reset_code)

    plot_lines = format_plot_lines(grid_chart, width, height, min_x, max_x, min_y, max_y, xlabel, ylabel, grid_lines=grid)
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


def _fill_under_segments(
    grid: List[List[str]],
    width: int,
    height: int,
    scaled: List[Tuple[int, int]],
    color_code: str,
    fill_char: str,
    reset_code: str,
) -> None:
    for i in range(len(scaled) - 1):
        x0, y0 = scaled[i]
        x1, y1 = scaled[i + 1]

        x_start = min(x0, x1)
        x_end = max(x0, x1)

        for x in range(x_start, x_end + 1):
            if x1 != x0:
                t = (x - x0) / (x1 - x0)
                y_line = y0 + t * (y1 - y0)
            else:
                y_line = min(y0, y1)

            y_line = int(round(y_line))

            for y in range(y_line, height):
                if 0 <= y < height and 0 <= x < width:
                    if grid[y][x] == ' ':
                        grid[y][x] = color_code + fill_char + reset_code
