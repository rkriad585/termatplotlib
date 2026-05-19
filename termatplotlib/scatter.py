import math
from typing import Callable, List, Optional, Tuple

from termatplotlib.utils import COLORS, write_output, validate_data, format_plot_lines, get_default


def _transform_log(vals: List[float], label: str) -> List[float]:
    out = []
    for v in vals:
        if v <= 0:
            raise ValueError(f"{label} contains non-positive value {v} — log scale requires positive values")
        out.append(math.log10(v))
    return out


def scatter(
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
    x_range = max_x - min_x
    y_range = max_y - min_y

    grid_chart = [[' ' for _ in range(width)] for _ in range(height)]

    for series in data:
        sx = series['x']
        sy = series['y']
        series_color = series.get('color') or color or 'white'
        marker = series.get('marker', '*')
        error_y = series.get('error_y')

        color_code = COLORS.get(series_color, '')
        reset_code = COLORS['reset'] if color_code else ''

        for i in range(len(sx)):
            x_scaled = int(((sx[i] - min_x) / x_range) * (width - 1)) if x_range != 0 else 0
            y_scaled = int(((sy[i] - min_y) / y_range) * (height - 1)) if y_range != 0 else 0
            grid_chart[height - 1 - y_scaled][x_scaled] = color_code + marker + reset_code

            if error_y is not None:
                err = error_y[i] if isinstance(error_y, list) else error_y
                if log_y and err > 0:
                    low = sy[i] - math.log10(10 ** sy[i] - err) if (10 ** sy[i] - err) > 0 else -999
                    high = math.log10(10 ** sy[i] + err) - sy[i] if (10 ** sy[i] + err) > 0 else 999
                    err_low = low
                    err_high = high
                else:
                    err_low = err_high = err
                y_low = int(((sy[i] - err_low - min_y) / y_range) * (height - 1)) if y_range != 0 else 0
                y_high = int(((sy[i] + err_high - min_y) / y_range) * (height - 1)) if y_range != 0 else 0
                for yb in range(min(y_low, y_high), max(y_low, y_high) + 1):
                    if 0 <= (height - 1 - yb) < height and 0 <= x_scaled < width:
                        grid_chart[height - 1 - yb][x_scaled] = color_code + '|' + reset_code

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
