import math
from typing import Callable, List, Optional, Tuple

from termatplotlib.utils import COLORS, write_output, validate_data, format_plot_lines, get_default


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


def _transform_log(vals: List[float], label: str) -> List[float]:
    out = []
    for v in vals:
        if v <= 0:
            raise ValueError(f"{label} contains non-positive value {v} — log scale requires positive values")
        out.append(math.log10(v))
    return out


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
    log_x: bool = False,
    log_y: bool = False,
    custom_xticks: Optional[List[float]] = None,
    custom_yticks: Optional[List[float]] = None,
    tick_formatter: Optional[Callable[[float], str]] = None,
    thresholds: Optional[List[dict]] = None,
    _return_output: bool = False,
) -> Optional[List[str]]:
    width = get_default('width') or width
    height = get_default('height') or height
    color = get_default('color') or color
    legend = get_default('legend') or legend
    grid = get_default('grid') or grid

    output: List[str] = []
    if title:
        output.append(f"\n{title.center(width)}\n")

    try:
        all_x, all_y = validate_data(data)
    except ValueError as e:
        output.append(f"Error: {e}")
        write_output(output, output_file)
        return (output if _return_output else None)

    if log_x:
        try:
            all_x = _transform_log(all_x, "x data")
            for series in data:
                series['x'] = _transform_log(series['x'], "x data")
        except ValueError as e:
            output.append(f"Error: {e}")
            write_output(output, output_file)
            return (output if _return_output else None)
    if log_y:
        try:
            all_y = _transform_log(all_y, "y data")
            for series in data:
                series['y'] = _transform_log(series['y'], "y data")
        except ValueError as e:
            output.append(f"Error: {e}")
            write_output(output, output_file)
            return (output if _return_output else None)

    if xlim:
        min_x, max_x = (math.log10(xlim[0]), math.log10(xlim[1])) if log_x else xlim
    else:
        min_x, max_x = min(all_x), max(all_x)
    if ylim:
        min_y, max_y = (math.log10(ylim[0]), math.log10(ylim[1])) if log_y else ylim
    else:
        min_y, max_y = min(all_y), max(all_y)

    grid_chart = [[' ' for _ in range(width)] for _ in range(height)]

    for series in data:
        sx = series['x']
        sy = series['y']
        series_color = series.get('color') or color or 'white'
        marker = series.get('marker', '*')
        error_y = series.get('error_y')

        color_code = COLORS.get(series_color, '')
        reset_code = COLORS['reset'] if color_code else ''

        scaled = [_scale_point(sx[i], sy[i], min_x, max_x, min_y, max_y, width, height)
                  for i in range(len(sx))]

        for i in range(len(scaled) - 1):
            _plot_line_segment(grid_chart, width, height,
                               scaled[i][0], scaled[i][1],
                               scaled[i + 1][0], scaled[i + 1][1],
                               color_code, marker, reset_code)

        if error_y is not None:
            for i in range(len(sx)):
                err = error_y[i] if isinstance(error_y, list) else error_y
                if log_y and err > 0:
                    low = sy[i] - math.log10(10 ** sy[i] - err) if (10 ** sy[i] - err) > 0 else -999
                    high = math.log10(10 ** sy[i] + err) - sy[i] if (10 ** sy[i] + err) > 0 else 999
                    err_low = low
                    err_high = high
                else:
                    err_low = err_high = err
                xs, ys = scaled[i]
                y_low = int(((sy[i] - err_low - min_y) / max(max_y - min_y, 1)) * (height - 1)) if max_y != min_y else 0
                y_high = int(((sy[i] + err_high - min_y) / max(max_y - min_y, 1)) * (height - 1)) if max_y != min_y else 0
                for yb in range(min(y_low, y_high), max(y_low, y_high) + 1):
                    row = height - 1 - yb
                    if 0 <= row < height and 0 <= xs < width:
                        grid_chart[row][xs] = color_code + '|' + reset_code

    plot_lines = format_plot_lines(
        grid_chart, width, height, min_x, max_x, min_y, max_y,
        xlabel, ylabel, grid_lines=grid, log_x=log_x, log_y=log_y,
        custom_xticks=custom_xticks, custom_yticks=custom_yticks,
        tick_formatter=tick_formatter, thresholds=thresholds,
    )
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
    return (output if _return_output else None)


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
    log_x: bool = False,
    log_y: bool = False,
    custom_xticks: Optional[List[float]] = None,
    custom_yticks: Optional[List[float]] = None,
    tick_formatter: Optional[Callable[[float], str]] = None,
    thresholds: Optional[List[dict]] = None,
    _return_output: bool = False,
) -> Optional[List[str]]:
    width = get_default('width') or width
    height = get_default('height') or height
    color = get_default('color') or color
    legend = get_default('legend') or legend
    grid = get_default('grid') or grid

    output: List[str] = []
    if title:
        output.append(f"\n{title.center(width)}\n")

    try:
        all_x, all_y = validate_data(data)
    except ValueError as e:
        output.append(f"Error: {e}")
        write_output(output, output_file)
        return (output if _return_output else None)

    if log_x:
        try:
            all_x = _transform_log(all_x, "x data")
            for series in data:
                series['x'] = _transform_log(series['x'], "x data")
        except ValueError as e:
            output.append(f"Error: {e}")
            write_output(output, output_file)
            return (output if _return_output else None)
    if log_y:
        try:
            all_y = _transform_log(all_y, "y data")
            for series in data:
                series['y'] = _transform_log(series['y'], "y data")
        except ValueError as e:
            output.append(f"Error: {e}")
            write_output(output, output_file)
            return (output if _return_output else None)

    if stacked:
        n = len(data[0]['x'])
        base = [0.0] * n
        for series in data:
            for i in range(len(series['y'])):
                series['y'][i] += base[i]
                base[i] = series['y'][i]
        _, all_y = validate_data(data)

    if xlim:
        min_x, max_x = (math.log10(xlim[0]), math.log10(xlim[1])) if log_x else xlim
    else:
        min_x, max_x = min(all_x), max(all_x)
    if ylim:
        min_y, max_y = (math.log10(ylim[0]), math.log10(ylim[1])) if log_y else ylim
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

    plot_lines = format_plot_lines(
        grid_chart, width, height, min_x, max_x, min_y, max_y,
        xlabel, ylabel, grid_lines=grid, log_x=log_x, log_y=log_y,
        custom_xticks=custom_xticks, custom_yticks=custom_yticks,
        tick_formatter=tick_formatter, thresholds=thresholds,
    )
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
    return (output if _return_output else None)


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
