from typing import Dict, List, Optional

from termatplotlib.utils import COLORS, write_output, get_terminal_width, get_default

CAL_CHARS = [' ', '░', '▒', '▓', '█']


def calendar_heatmap(
    data: Dict[str, float],
    year: Optional[int] = None,
    title: Optional[str] = None,
    color: Optional[str] = None,
    palette: Optional[List[str]] = None,
    output_file: Optional[str] = None,
    _return_output: bool = False,
) -> Optional[List[str]]:
    color = get_default('color') or color

    output: List[str] = []
    if title:
        output.append(f"\n{title.center(60)}\n")

    if not data:
        output.append("(no data)")
        write_output(output, output_file)
        return (output if _return_output else None)

    values = list(data.values())
    vmin = min(values)
    vmax = max(values)
    vrange = vmax - vmin if vmax != vmin else 1

    if palette is None:
        palette = [color] if color else ['green', 'yellow', 'red']

    import datetime
    today = datetime.date.today()
    y = year or today.year

    days_in_month = [31, 29 if (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)) else 28,
                     31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    header = f"{'Mon':>3} "
    for mn in month_names:
        header += f"{mn:>4}"
    output.append(header)

    # grid: day of week (0=Mon) x ~52 weeks
    grid: Dict[int, Dict[int, str]] = {}
    for month, ndays in enumerate(days_in_month):
        for day in range(1, ndays + 1):
            try:
                dt = datetime.date(y, month + 1, day)
            except ValueError:
                continue
            key = dt.isoformat()
            val = data.get(key, 0)
            norm = (val - vmin) / vrange
            intensity = min(int(norm * 4), 4)
            p = palette[int(norm * (len(palette) - 1))] if len(palette) > 1 else palette[0]
            c = COLORS.get(p, '')
            r = COLORS['reset'] if c else ''
            char = c + CAL_CHARS[intensity] + r if c else CAL_CHARS[intensity]
            w = dt.isocalendar()[1]
            dw = (dt.weekday() + 1) % 7
            if dw not in grid:
                grid[dw] = {}
            grid[dw][w] = char

    day_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for dw in range(7):
        line = f"{day_names[dw]:>3} "
        for w in range(1, 54):
            char = grid.get(dw, {}).get(w, ' ')
            line += char * 3 + " "
        output.append(line)

    output.append("")
    write_output(output, output_file)
    return (output if _return_output else None)
