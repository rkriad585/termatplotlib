from typing import List, Optional

from termatplotlib.utils import COLORS, write_output, get_default

SPARK_CHARS = [' ', '▁', '▂', '▃', '▄', '▅', '▆', '▇', '█']


def sparkline(
    values: List[float],
    width: Optional[int] = None,
    color: Optional[str] = None,
    title: Optional[str] = None,
    min_val: Optional[float] = None,
    max_val: Optional[float] = None,
    output_file: Optional[str] = None,
    _return_output: bool = False,
) -> Optional[List[str]]:
    color = get_default('color') or color

    output: List[str] = []
    if title:
        output.append(f"  {title}")

    if not values:
        output.append("")
        write_output(output, output_file)
        return (output if _return_output else None)

    mn = min_val if min_val is not None else min(values)
    mx = max_val if max_val is not None else max(values)
    rng = mx - mn if mx != mn else 1

    if width and width < len(values):
        step = len(values) / width
        sampled = []
        for i in range(width):
            idx = int(i * step)
            sampled.append(values[min(idx, len(values) - 1)])
        values = sampled

    c = COLORS.get(color, '')
    rc = COLORS['reset'] if c else ''
    line = ""
    for v in values:
        idx = min(int((v - mn) / rng * 8), 8)
        if idx < 0:
            idx = 0
        line += c + SPARK_CHARS[idx] + rc if c else SPARK_CHARS[idx]
    output.append(f"  {line}")

    output.append("")
    write_output(output, output_file)
    return (output if _return_output else None)
