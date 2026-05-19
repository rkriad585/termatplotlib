import math
import random
from typing import Dict, List, Optional

from termatplotlib.utils import COLORS, write_output, get_terminal_width, get_default


def wordcloud(
    word_weights: Dict[str, float],
    width: Optional[int] = None,
    height: int = 10,
    title: Optional[str] = None,
    colors: Optional[List[str]] = None,
    output_file: Optional[str] = None,
    _return_output: bool = False,
) -> Optional[List[str]]:
    width = get_default('width') or width or get_terminal_width()
    if colors is None:
        colors = ['cyan', 'green', 'yellow', 'blue', 'magenta', 'red', 'white']

    output: List[str] = []
    if title:
        output.append(f"\n{title.center(width)}\n")

    if not word_weights:
        output.append("Error: Empty word data.")
        write_output(output, output_file)
        return (output if _return_output else None)

    max_weight = max(word_weights.values()) if word_weights else 1
    min_weight = min(word_weights.values()) if word_weights else 0
    w_range = max_weight - min_weight if max_weight != min_weight else 1

    grid = [[' ' for _ in range(width)] for _ in range(height)]

    words = sorted(word_weights.items(), key=lambda x: -x[1])

    SIZES = [
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 1),
        (5, 1),
    ]

    placements = []

    for word, weight in words:
        strength = (weight - min_weight) / w_range if w_range else 1
        size_idx = min(int(strength * 4), 4)
        char_w = size_idx + 1
        char_h = 1
        word_display = word[:char_w].ljust(char_w)

        clr = COLORS.get(colors[len(placements) % len(colors)], '')
        rc = COLORS['reset'] if clr else ''

        placed = False
        for _ in range(50):
            rx = random.randint(0, max(0, width - char_w - 1))
            ry = random.randint(0, max(0, height - char_h - 1))
            collision = False
            for pw, px, py, pw_w, pw_h in placements:
                if not (rx + char_w <= px or rx >= px + pw_w or ry + char_h <= py or ry >= py + pw_h):
                    collision = True
                    break
            if not collision:
                for i, ch in enumerate(word_display):
                    if ry < height and rx + i < width:
                        grid[ry][rx + i] = clr + ch + rc if clr else ch
                placements.append((word, rx, ry, char_w, char_h))
                placed = True
                break

    for row in grid:
        line = ''.join(row)
        if line.strip():
            output.append('  ' + line)

    output.append("")
    for i, (word, weight) in enumerate(words[:10]):
        clr = COLORS.get(colors[i % len(colors)], '')
        rc = COLORS['reset'] if clr else ''
        bar_len = int(weight / max_weight * 10) if max_weight else 1
        bar = '█' * bar_len
        output.append(f"  {clr}{bar}{rc} {word}: {weight}")

    if len(words) > 10:
        output.append(f"  ... and {len(words) - 10} more")

    output.append("")
    write_output(output, output_file)
    return (output if _return_output else None)
