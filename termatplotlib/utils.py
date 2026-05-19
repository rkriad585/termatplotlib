import math
import re
import shutil
from typing import Any, Dict, List, Optional, Tuple

ANSI_RE = re.compile(r'\033\[[0-9;]*m')

COLORS = {
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'reset': '\033[0m'
}

COLOR_NAMES: List[str] = list(COLORS.keys())[:-1]

_DEFAULTS: Dict[str, Any] = {}


def set_default(**kwargs: Any) -> None:
    _DEFAULTS.update(kwargs)


def get_default(key: str) -> Any:
    return _DEFAULTS.get(key)


def reset_defaults() -> None:
    _DEFAULTS.clear()


def strip_ansi(text: str) -> str:
    return ANSI_RE.sub('', text)


def write_output(output_lines: List[str], output_file: Optional[str] = None) -> None:
    text = "\n".join(output_lines) + "\n"
    if output_file:
        with open(output_file, 'w') as f:
            f.write(strip_ansi(text))
    else:
        print(text)


def get_terminal_width(default: int = 80) -> int:
    try:
        return shutil.get_terminal_size().columns
    except Exception:
        return default


def validate_data(data: List[dict]) -> Tuple[List[float], List[float]]:
    if not data:
        raise ValueError("Data list cannot be empty.")
    all_x: List[float] = []
    all_y: List[float] = []
    for i, series in enumerate(data):
        if 'x' not in series or 'y' not in series:
            raise ValueError(f"Series {i} is missing 'x' or 'y' keys.")
        if len(series['x']) != len(series['y']):
            raise ValueError(
                f"Series {i} has mismatched x ({len(series['x'])}) "
                f"and y ({len(series['y'])}) lengths."
            )
        all_x.extend(series['x'])
        all_y.extend(series['y'])
    if not all_x:
        raise ValueError("All series have empty data.")
    return all_x, all_y


def _format_tick_label(val: float, log_scale: bool) -> str:
    if log_scale:
        if val <= 0:
            return "0"
        actual = 10 ** val
        if actual >= 1e6 or actual <= 1e-4:
            return f"{actual:.1e}"
        elif actual == int(actual):
            return str(int(actual))
        else:
            return f"{actual:.2f}"
    return f"{val:.1f}"


def format_plot_lines(
    grid: List[List[str]],
    width: int,
    height: int,
    min_x: float,
    max_x: float,
    min_y: float,
    max_y: float,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    grid_lines: bool = False,
    log_x: bool = False,
    log_y: bool = False,
) -> List[str]:
    output: List[str] = []
    x_range = max_x - min_x
    y_range = max_y - min_y

    if grid_lines:
        y_tick_step = height // 5 if height >= 5 else 1
        x_tick_step = width // 5 if width >= 5 else 1
        for r in range(height):
            is_hline = (r % y_tick_step == 0 or r == 0 or r == height - 1)
            for c in range(width):
                is_vline = (c % x_tick_step == 0 or c == 0 or c == width - 1)
                if grid[r][c] == ' ' and (is_hline or is_vline):
                    if is_hline and is_vline:
                        grid[r][c] = '+'
                    elif is_hline:
                        grid[r][c] = '-'
                    elif is_vline:
                        grid[r][c] = '|'

    sample_label = _format_tick_label(max_y if not log_y else max_y, log_y)
    y_label_width = len(sample_label) + 2

    display_grid = [[' ' for _ in range(width + y_label_width)] for _ in range(height)]

    for r in range(height):
        y_val = min_y + (height - 1 - r) * (y_range / max(height - 1, 1))
        if r % (height // 5 if height >= 5 else 1) == 0 or r == 0 or r == height - 1:
            label = _format_tick_label(y_val, log_y)
            for i, char in enumerate(label):
                if i < y_label_width:
                    display_grid[r][i] = char
        for c in range(width):
            display_grid[r][c + y_label_width] = grid[r][c]

    output.append('+' + '-' * (width + y_label_width) + '+')
    for row in display_grid:
        output.append('|' + ''.join(row) + '|')
    output.append('+' + '-' * (width + y_label_width) + '+')

    x_tick_interval = x_range / max(width - 1, 1)
    x_labels_line = [" "] * (width + y_label_width)
    for c in range(width):
        x_val = min_x + c * x_tick_interval
        if c % (width // 5 if width >= 5 else 1) == 0 or c == 0 or c == width - 1:
            label = _format_tick_label(x_val, log_x)
            start = c + y_label_width
            if start + len(label) < len(x_labels_line):
                for i, char in enumerate(label):
                    x_labels_line[start + i] = char
    output.append(''.join(x_labels_line))

    if xlabel:
        output.append(f"\n{xlabel.center(width + y_label_width)}")
    output.append("\n")

    return output
