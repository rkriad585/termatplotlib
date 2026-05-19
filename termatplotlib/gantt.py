from typing import List, Optional, Tuple

from termatplotlib.utils import COLORS, write_output, get_terminal_width, get_default


def gantt(
    tasks: List[dict],
    width: Optional[int] = None,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    bar_char: str = '█',
    colors: Optional[List[str]] = None,
    output_file: Optional[str] = None,
    _return_output: bool = False,
) -> Optional[List[str]]:
    width = get_default('width') or width or get_terminal_width()
    if colors is None:
        colors = ['cyan', 'green', 'yellow', 'blue', 'magenta', 'red',
                  'white', 'green', 'cyan', 'yellow']

    output: List[str] = []
    if title:
        output.append(f"\n{title.center(width)}\n")

    if not tasks:
        output.append("Error: No tasks provided.")
        write_output(output, output_file)
        return (output if _return_output else None)

    all_starts = [t['start'] for t in tasks]
    all_ends = [t['end'] for t in tasks]
    if not all_starts or not all_ends:
        output.append("Error: Tasks must have 'start' and 'end'.")
        write_output(output, output_file)
        return (output if _return_output else None)

    t_min = min(all_starts)
    t_max = max(all_ends)
    t_range = t_max - t_min if t_max != t_min else 1

    task_label_width = max(len(str(t.get('label', f"Task {i}"))) for i, t in enumerate(tasks))
    task_label_width = min(task_label_width, 20)
    chart_w = width - task_label_width - 4
    if chart_w < 10:
        chart_w = 10

    for t in tasks:
        t.setdefault('label', f"Task {tasks.index(t) + 1}")
        t.setdefault('color', colors[tasks.index(t) % len(colors)])

    for i, t in enumerate(tasks):
        label = str(t['label']).ljust(task_label_width)
        left = int((t['start'] - t_min) / t_range * (chart_w - 1))
        right = int((t['end'] - t_min) / t_range * (chart_w - 1))
        if right >= chart_w:
            right = chart_w - 1
        if left < 0:
            left = 0
        clr = COLORS.get(t['color'], '')
        rc = COLORS['reset'] if clr else ''
        styled = clr + bar_char + rc if clr else bar_char
        bar = "  " + label + " |"
        for c in range(chart_w):
            if left <= c <= right:
                bar += styled
            else:
                bar += "·"
        bar += "|"
        output.append(bar)

    if xlabel:
        output.append(f"\n{xlabel.center(width)}")
    output.append("")
    output.append(f"  Scale: {t_min:.0f} to {t_max:.0f} across {chart_w} columns")
    output.append("")

    write_output(output, output_file)
    return (output if _return_output else None)
