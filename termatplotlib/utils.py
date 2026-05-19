import math
import re
import shutil
from typing import Any, Callable, Dict, List, Optional, Tuple

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

THEMES: Dict[str, Dict[str, str]] = {
    'default': {'primary': 'cyan', 'secondary': 'yellow', 'accent': 'green', 'grid': 'white', 'text': 'white'},
    'dark': {'primary': 'blue', 'secondary': 'magenta', 'accent': 'cyan', 'grid': 'white', 'text': 'white'},
    'light': {'primary': 'red', 'secondary': 'green', 'accent': 'blue', 'grid': 'black', 'text': 'black'},
    'monokai': {'primary': 'red', 'secondary': 'green', 'accent': 'yellow', 'grid': 'white', 'text': 'white'},
    'ocean': {'primary': 'blue', 'secondary': 'cyan', 'accent': 'green', 'grid': 'white', 'text': 'white'},
    'forest': {'primary': 'green', 'secondary': 'yellow', 'accent': 'cyan', 'grid': 'white', 'text': 'white'},
    'sunset': {'primary': 'red', 'secondary': 'magenta', 'accent': 'yellow', 'grid': 'white', 'text': 'white'},
}

_DEFAULTS: Dict[str, Any] = {}


def apply_theme(name: str = 'default') -> None:
    theme = THEMES.get(name)
    if not theme:
        raise ValueError(f"Unknown theme '{name}'. Available: {', '.join(THEMES.keys())}")
    set_default(color=theme['primary'])
    set_default(color_secondary=theme['secondary'])
    set_default(color_accent=theme['accent'])


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


def _render_yticks(
    display_grid: List[List[str]],
    height: int,
    y_label_width: int,
    min_y: float,
    max_y: float,
    log_y: bool,
    custom_yticks: Optional[List[float]] = None,
    formatter: Optional[Callable[[float], str]] = None,
) -> None:
    y_range = max_y - min_y
    if custom_yticks:
        for y_val in custom_yticks:
            if y_val < min_y or y_val > max_y:
                continue
            r = int((max_y - y_val) / y_range * (height - 1)) if y_range else 0
            if 0 <= r < height:
                label = formatter(y_val) if formatter else _format_tick_label(y_val, log_y)
                for i, ch in enumerate(label):
                    if i < y_label_width:
                        display_grid[r][i] = ch
        return
    for r in range(height):
        y_val = min_y + (height - 1 - r) * (y_range / max(height - 1, 1))
        if r % (height // 5 if height >= 5 else 1) == 0 or r == 0 or r == height - 1:
            label = formatter(y_val) if formatter else _format_tick_label(y_val, log_y)
            for i, ch in enumerate(label):
                if i < y_label_width:
                    display_grid[r][i] = ch


def _render_xticks(
    width: int,
    y_label_width: int,
    min_x: float,
    max_x: float,
    log_x: bool,
    custom_xticks: Optional[List[float]] = None,
    formatter: Optional[Callable[[float], str]] = None,
) -> List[str]:
    x_range = max_x - min_x
    x_labels_line = [" "] * (width + y_label_width)
    if custom_xticks:
        for x_val in custom_xticks:
            if x_val < min_x or x_val > max_x:
                continue
            c = int((x_val - min_x) / x_range * (width - 1)) if x_range else 0
            label = formatter(x_val) if formatter else _format_tick_label(x_val, log_x)
            start = c + y_label_width
            if 0 <= c < width and start + len(label) < len(x_labels_line):
                for i, ch in enumerate(label):
                    x_labels_line[start + i] = ch
        return x_labels_line
    for c in range(width):
        x_val = min_x + c * (x_range / max(width - 1, 1))
        if c % (width // 5 if width >= 5 else 1) == 0 or c == 0 or c == width - 1:
            label = formatter(x_val) if formatter else _format_tick_label(x_val, log_x)
            start = c + y_label_width
            if start + len(label) < len(x_labels_line):
                for i, ch in enumerate(label):
                    x_labels_line[start + i] = ch
    return x_labels_line


def _draw_thresholds(
    grid: List[List[str]],
    width: int,
    height: int,
    min_x: float,
    max_x: float,
    min_y: float,
    max_y: float,
    thresholds: Optional[List[dict]] = None,
) -> None:
    if not thresholds:
        return
    x_range = max_x - min_x
    y_range = max_y - min_y
    for th in thresholds:
        axis = th.get('axis', 'y')
        val = th['value']
        char = th.get('char', '-')
        color_code = COLORS.get(th.get('color', ''), '')
        reset_code = COLORS['reset'] if color_code else ''
        styled = color_code + char + reset_code if color_code else char
        if axis == 'y':
            r = int((max_y - val) / y_range * (height - 1)) if y_range else 0
            if 0 <= r < height:
                for c in range(width):
                    grid[r][c] = styled
        elif axis == 'x':
            c = int((val - min_x) / x_range * (width - 1)) if x_range else 0
            if 0 <= c < width:
                for r in range(height):
                    grid[r][c] = styled


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
    custom_xticks: Optional[List[float]] = None,
    custom_yticks: Optional[List[float]] = None,
    tick_formatter: Optional[Callable[[float], str]] = None,
    thresholds: Optional[List[dict]] = None,
) -> List[str]:
    output: List[str] = []
    x_range = max_x - min_x
    y_range = max_y - min_y

    _draw_thresholds(grid, width, height, min_x, max_x, min_y, max_y, thresholds)

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

    sample_label = tick_formatter(max_y) if tick_formatter else _format_tick_label(max_y if not log_y else max_y, log_y)
    y_label_width = len(sample_label) + 2

    display_grid = [[' ' for _ in range(width + y_label_width)] for _ in range(height)]

    _render_yticks(display_grid, height, y_label_width, min_y, max_y, log_y, custom_yticks, tick_formatter)
    for r in range(height):
        for c in range(width):
            display_grid[r][c + y_label_width] = grid[r][c]

    output.append('+' + '-' * (width + y_label_width) + '+')
    for row in display_grid:
        output.append('|' + ''.join(row) + '|')
    output.append('+' + '-' * (width + y_label_width) + '+')

    x_labels_line = _render_xticks(width, y_label_width, min_x, max_x, log_x, custom_xticks, tick_formatter)
    output.append(''.join(x_labels_line))

    if xlabel:
        output.append(f"\n{xlabel.center(width + y_label_width)}")
    output.append("\n")

    return output
