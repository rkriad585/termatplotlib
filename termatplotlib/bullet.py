from typing import List, Optional

from termatplotlib.utils import COLORS, write_output, get_terminal_width, get_default


def bullet(
    labels: List[str],
    actuals: List[float],
    targets: List[float],
    ranges: Optional[List[dict]] = None,
    width: Optional[int] = None,
    title: Optional[str] = None,
    color_actual: Optional[str] = None,
    color_target: Optional[str] = None,
    output_file: Optional[str] = None,
    _return_output: bool = False,
) -> Optional[List[str]]:
    width = get_default('width') or width or get_terminal_width()
    color_actual = get_default('color') or color_actual or 'cyan'
    color_target = get_default('color_secondary') or color_target or 'red'

    output: List[str] = []
    if title:
        output.append(f"\n{title.center(width)}\n")

    if not labels or not actuals or not targets or len(labels) != len(actuals) or len(labels) != len(targets):
        output.append("Error: Invalid input.")
        write_output(output, output_file)
        return (output if _return_output else None)

    for i in range(len(labels)):
        mx = max(actuals[i], targets[i]) * 1.2
        if mx <= 0:
            mx = 1
        rng_data = ranges[i] if ranges and i < len(ranges) else {}
        bad = rng_data.get('bad', mx * 0.6)
        satisfactory = rng_data.get('satisfactory', mx * 0.3)

        chart_w = width - 30
        if chart_w < 10:
            chart_w = 10

        clr_act = COLORS.get(color_actual, '')
        clr_tgt = COLORS.get(color_target, '')
        rc = COLORS['reset'] if (clr_act or clr_tgt) else ''
        label = str(labels[i]).ljust(20)
        line = f"  {label} "

        bad_len = int(bad / mx * chart_w)
        sat_len = int((satisfactory - bad) / mx * chart_w)
        good_len = chart_w - bad_len - sat_len

        bad_char = clr_act + '░' + rc if clr_act else '░'
        sat_char = clr_act + '▒' + rc if clr_act else '▒'
        good_char = ' '

        line += bad_char * max(0, bad_len)
        line += sat_char * max(0, sat_len)
        line += good_char * max(0, good_len)

        actual_len = int(actuals[i] / mx * chart_w)
        line += f" {'│' * max(0, actual_len)}"
        line += f" {actuals[i]:.0f}"

        target_pos = int(targets[i] / mx * chart_w)
        tgt_marker_line = " " * (22 + chart_w + 1)
        tgt_marker_line = tgt_marker_line[:22 + target_pos] + (clr_tgt + '▼' + rc if clr_tgt else '▼') + tgt_marker_line[22 + target_pos + 1:]
        output.append(line)
        output.append(tgt_marker_line + f" target: {targets[i]:.0f}")
        output.append("")

    output.append("")
    write_output(output, output_file)
    return (output if _return_output else None)
