import argparse
import sys
from typing import List

from termatplotlib import bar, scatter, line, pie, hist, sparkline, step, bubble, strip, waterfall, gantt, radar, sankey, funnel, bullet, donut, pareto, wordcloud


def main() -> None:
    parser = argparse.ArgumentParser(description="termatplotlib — ASCII plots in your terminal")
    parser.add_argument("--type", "-t", default="bar",
                        choices=["bar", "scatter", "line", "pie", "hist", "sparkline",
                                 "step", "bubble", "strip", "waterfall", "gantt", "radar",
                                 "sankey", "funnel", "bullet", "donut", "pareto", "wordcloud"],
                        help="Chart type")
    parser.add_argument("--title", help="Chart title")
    parser.add_argument("--color", help="Chart color")
    parser.add_argument("--width", type=int, help="Chart width")
    parser.add_argument("--height", type=int, help="Chart height")
    parser.add_argument("--output", "-o", help="Output file")
    parser.add_argument("--labels", nargs="*", help="Labels for bar/pie charts")
    parser.add_argument("--bins", type=int, default=10, help="Histogram bins")
    parser.add_argument("--delim", default=None, help="Input delimiter")
    parser.add_argument("--legend", action="store_true", help="Show legend")
    parser.add_argument("--grid", action="store_true", help="Show grid")
    parser.add_argument("--log-x", action="store_true", help="Log X axis")
    parser.add_argument("--log-y", action="store_true", help="Log Y axis")

    args = parser.parse_args()

    # Read data from stdin or file args
    if not sys.stdin.isatty():
        data_lines = sys.stdin.read().strip().splitlines()
        values: List[float] = []
        for line in data_lines:
            parts = line.strip().split(args.delim or ",")
            for p in parts:
                p = p.strip()
                try:
                    values.append(float(p))
                except ValueError:
                    pass
    else:
        values = []

    chart_kwargs = {}
    if args.title:
        chart_kwargs['title'] = args.title
    if args.color:
        chart_kwargs['color'] = args.color
    if args.output:
        chart_kwargs['output_file'] = args.output
    if args.width:
        chart_kwargs['width'] = args.width
    if args.height:
        chart_kwargs['height'] = args.height
    if args.legend:
        chart_kwargs['legend'] = True
    if args.grid:
        chart_kwargs['grid'] = True
    if args.log_x:
        chart_kwargs['log_x'] = True
    if args.log_y:
        chart_kwargs['log_y'] = True

    if args.type == "bar":
        labels = args.labels or [str(i) for i in range(len(values))]
        bar(labels, values, max_width=args.width, **chart_kwargs)
    elif args.type == "scatter":
        x_vals = list(range(len(values)))
        data = [{'x': x_vals, 'y': values}]
        scatter(data, **chart_kwargs)
    elif args.type == "line":
        x_vals = list(range(len(values)))
        data = [{'x': x_vals, 'y': values}]
        line(data, **chart_kwargs)
    elif args.type == "pie":
        labels = args.labels or [str(i) for i in range(len(values))]
        pie(labels, values, **chart_kwargs)
    elif args.type == "hist":
        hist(values, bins=args.bins, **chart_kwargs)
    elif args.type == "sparkline":
        sparkline(values, **chart_kwargs)
    elif args.type == "step":
        x_vals = list(range(len(values)))
        data = [{'x': x_vals, 'y': values}]
        step(data, **chart_kwargs)
    elif args.type == "bubble":
        x_vals = list(range(len(values)))
        data = [{'x': x_vals, 'y': values, 'size': [5] * len(values)}]
        bubble(data, **chart_kwargs)
    elif args.type == "strip":
        strip(values, **chart_kwargs)
    elif args.type == "waterfall":
        labels = args.labels or [str(i) for i in range(len(values))]
        waterfall(labels, values, **chart_kwargs)
    elif args.type == "gantt":
        tasks = [{'label': f"Task {i}", 'start': i, 'end': i + v} for i, v in enumerate(values)] if values else []
        gantt(tasks, **chart_kwargs)
    elif args.type == "radar":
        labels = args.labels or [str(i) for i in range(len(values))]
        radar(labels, values, **chart_kwargs)
    elif args.type == "sankey":
        n = len(values)
        nodes = args.labels or [f"N{i}" for i in range(n)]
        links = [{'source': nodes[i], 'target': nodes[(i + 1) % n], 'value': v} for i, v in enumerate(values) if i + 1 < n]
        sankey(nodes, links, **chart_kwargs)
    elif args.type == "funnel":
        labels = args.labels or [str(i) for i in range(len(values))]
        funnel(labels, values, **chart_kwargs)
    elif args.type == "donut":
        labels = args.labels or [str(i) for i in range(len(values))]
        donut(labels, values, **chart_kwargs)
    elif args.type == "bullet":
        labels = args.labels or [str(i) for i in range(len(values[:len(values)//2]))]
        n = len(labels)
        actuals = values[:n]
        targets = values[n:2*n] if len(values) >= 2*n else [max(v * 1.2, 1) for v in actuals]
        bullet(labels, actuals, targets, **chart_kwargs)
    elif args.type == "pareto":
        labels = args.labels or [str(i) for i in range(len(values))]
        pareto(labels, values, **chart_kwargs)
    elif args.type == "wordcloud":
        labels = args.labels or [f"word{i}" for i in range(len(values))]
        wc = {labels[i]: values[i] for i in range(len(values))}
        wordcloud(wc, **chart_kwargs)


if __name__ == "__main__":
    main()
