import math

from termatplotlib.utils import COLORS, COLOR_NAMES, write_output


def pie(labels, values, radius=10, title=None, legend=True, output_file=None):
    output = []
    if title:
        output.append(f"\n{title.center(radius * 2)}\n")

    if not labels or not values or len(labels) != len(values):
        output.append("Error: Invalid input. Labels and values must be non-empty and of the same length.")
        write_output(output, output_file)
        return

    total = sum(values)
    proportions = [v / total for v in values]

    grid = [[' ' for _ in range(radius * 2)] for _ in range(radius * 2)]
    center_x, center_y = radius, radius

    start_angle = 0
    for i, prop in enumerate(proportions):
        end_angle = start_angle + prop * 2 * math.pi
        color_code = COLORS[COLOR_NAMES[i % len(COLOR_NAMES)]]

        for y in range(radius * 2):
            for x in range(radius * 2):
                dx, dy = x - center_x, y - center_y
                if dx ** 2 + dy ** 2 <= radius ** 2:
                    angle = math.atan2(dy, dx)
                    if angle < 0:
                        angle += 2 * math.pi
                    if start_angle <= angle < end_angle:
                        grid[y][x] = color_code + '█' + COLORS['reset']

        start_angle = end_angle

    for row in grid:
        output.append(''.join(row))

    if legend:
        output.append("\nLegend:")
        for i, label in enumerate(labels):
            c = COLORS[COLOR_NAMES[i % len(COLOR_NAMES)]]
            output.append(f"{c}█{COLORS['reset']} {label}: {values[i]} ({proportions[i]:.1%})")
    output.append("\n")

    write_output(output, output_file)
