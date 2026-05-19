from typing import Dict, List, Optional, Tuple

from termatplotlib.utils import COLORS, write_output, get_terminal_width, get_default


def sankey(
    nodes: List[str],
    links: List[dict],
    width: Optional[int] = None,
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

    if not nodes or not links:
        output.append("Error: Need at least 1 node and 1 link.")
        write_output(output, output_file)
        return (output if _return_output else None)

    links_out: Dict[str, List[dict]] = {n: [] for n in nodes}
    links_in: Dict[str, List[dict]] = {n: [] for n in nodes}
    for link in links:
        if 'source' not in link or 'target' not in link or 'value' not in link:
            continue
        s, t, v = link['source'], link['target'], link['value']
        links_out.setdefault(s, []).append(link)
        links_in.setdefault(t, []).append(link)

    node_colors = {}
    for i, n in enumerate(nodes):
        node_colors[n] = colors[i % len(colors)]

    col_a = []
    col_b = []
    for link in links:
        s = link['source']
        t = link['target']
        if s not in col_a:
            col_a.append(s)
        if t not in col_b:
            col_b.append(t)

    max_label = max(len(str(n)) for n in nodes) + 2
    col_w = (width - max_label * 2 - 6) // 3
    if col_w < 5:
        col_w = 5

    total_vals = {}
    for n in nodes:
        out_v = sum(l['value'] for l in links_out.get(n, []))
        in_v = sum(l['value'] for l in links_in.get(n, []))
        total_vals[n] = max(out_v, in_v) if (out_v or in_v) else 1

    max_total = max(total_vals.values()) if total_vals else 1
    chart_h = 20
    scale = (chart_h - 2) / max_total

    grid = [[' ' for _ in range(width)] for _ in range(chart_h)]

    col_a_x = max_label + 2
    col_b_x = col_a_x + col_w + 2
    col_b_label_x = col_b_x + col_w + 1

    def node_y(n):
        all_n = col_a if n in col_a else col_b
        idx = all_n.index(n) if n in all_n else 0
        total_idx = len(all_n) if all_n else 1
        return 2 + idx * (chart_h - 4) // max(total_idx, 1)

    for n in nodes:
        if n not in col_a and n not in col_b:
            continue
        in_col_a = n in col_a
        nx = col_a_x if in_col_a else col_b_x
        ny = node_y(n)
        clr = COLORS.get(node_colors[n], '')
        rc = COLORS['reset'] if clr else ''
        label = f" {n} "
        styled_label = clr + label + rc if clr else label
        if 0 <= ny < chart_h and nx < width:
            for i, ch in enumerate(styled_label):
                if nx + i < width:
                    grid[ny][nx + i] = ch

    for link in links:
        s, t, v = link['source'], link['target'], link['value']
        if s not in col_a or t not in col_b:
            continue
        sy = node_y(s)
        ty = node_y(t)
        vh = max(1, int(v * scale))
        clr = COLORS.get(node_colors.get(s, 'cyan'), '')
        rc = COLORS['reset'] if clr else ''

        mid_x = col_a_x + col_w + 1
        for r in range(sy - vh // 2, sy + vh // 2 + 1):
            for c in range(col_a_x, col_b_x + col_w):
                if 0 <= r < chart_h and 0 <= c < width:
                    frac = (c - col_a_x) / (col_b_x + col_w - col_a_x) if (col_b_x + col_w - col_a_x) else 1
                    row_frac = (r - sy) / vh if vh else 0
                    tgt_frac = (r - ty) / vh if vh else 0
                    row_at = sy + row_frac * (1 - frac) + tgt_frac * frac
                    if abs(r - row_at) < 0.8:
                        if grid[r][c] == ' ':
                            grid[r][c] = clr + '▒' + rc if clr else '▒'

    for r, row in enumerate(grid):
        output.append(''.join(row))

    for i, n in enumerate(nodes):
        clr = COLORS.get(node_colors[n], '')
        rc = COLORS['reset'] if clr else ''
        out_v = sum(l['value'] for l in links_out.get(n, []))
        in_v = sum(l['value'] for l in links_in.get(n, []))
        output.append(f"  {clr}■{rc} {n}: out={out_v}  in={in_v}")

    output.append("")
    write_output(output, output_file)
    return (output if _return_output else None)
