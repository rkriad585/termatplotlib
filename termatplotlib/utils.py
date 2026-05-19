import re
import shutil

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

COLOR_NAMES = list(COLORS.keys())[:-1]


def strip_ansi(text):
    return ANSI_RE.sub('', text)


def write_output(output_lines, output_file=None):
    text = "\n".join(output_lines) + "\n"
    if output_file:
        with open(output_file, 'w') as f:
            f.write(strip_ansi(text))
    else:
        print(text)


def get_terminal_width(default=80):
    try:
        return shutil.get_terminal_size().columns
    except Exception:
        return default


def validate_data(data):
    if not data:
        raise ValueError("Data list cannot be empty.")
    all_x = []
    all_y = []
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


def format_plot_lines(grid, width, height, min_x, max_x, min_y, max_y, xlabel=None, ylabel=None):
    output = []
    x_range = max_x - min_x
    y_range = max_y - min_y

    y_label_width = len(f"{max_y:.1f}") + 2

    display_grid = [[' ' for _ in range(width + y_label_width)] for _ in range(height)]

    for r in range(height):
        y_val = min_y + (height - 1 - r) * (y_range / max(height - 1, 1))
        if r % (height // 5 if height >= 5 else 1) == 0 or r == 0 or r == height - 1:
            label = f"{y_val:.1f}"
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
            label = f"{x_val:.1f}"
            start = c + y_label_width
            if start + len(label) < len(x_labels_line):
                for i, char in enumerate(label):
                    x_labels_line[start + i] = char
    output.append(''.join(x_labels_line))

    if xlabel:
        output.append(f"\n{xlabel.center(width + y_label_width)}")
    output.append("\n")

    return output
