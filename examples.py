import termatplotlib as tpl

# Example 1: Simple bar chart with title, labels, and color
print("--- Example 1: Enhanced Bar Chart ---")
labels1 = ["A", "B", "C", "D"]
values1 = [10, 20, 15, 5]
tpl.bar(labels1, values1, title="My Bar Chart", xlabel="Value", ylabel="Category", color="red")

# Example 2: Scatter plot with title, labels, color, and custom marker
print("\n--- Example 2: Enhanced Scatter Plot ---")
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 5, 7, 6, 8, 9, 10, 8, 9]
data_scatter = [{'x': x, 'y': y, 'color': 'blue', 'marker': 'x'}]
tpl.scatter(data_scatter, title="My Scatter Plot", xlabel="X-Axis", ylabel="Y-Axis")

# Example 3: Line chart with title, labels, color, and custom marker
print("\n--- Example 3: Enhanced Line Chart ---")
x_line = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_line = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
data_line = [{'x': x_line, 'y': y_line, 'color': 'green', 'marker': 'o'}]
tpl.line(data_line, title="My Line Chart", xlabel="X-Axis", ylabel="Y-Axis")

# Example 4: Pie chart
print("\n--- Example 4: Pie Chart ---")
labels4 = ["A", "B", "C", "D"]
values4 = [10, 20, 15, 5]
tpl.pie(labels4, values4, title="My Pie Chart")

# Example 5: Histogram
print("\n--- Example 5: Histogram ---")
data_hist = [1, 1, 2, 3, 3, 3, 4, 5, 5, 6, 7, 7, 7, 7, 8, 9, 10]
tpl.hist(data_hist, bins=5, title="My Histogram", xlabel="Value Range", ylabel="Frequency", color="magenta")

# Example 6: Scatter plot with numerical axis ticks and saving to file
print("\n--- Example 6: Scatter Plot with Numerical Axis Ticks (saved to file) ---")
x_ticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_ticks = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
data_scatter_file = [{'x': x_ticks, 'y': y_ticks, 'color': 'cyan', 'marker': '+'}]
tpl.scatter(data_scatter_file, title="Scatter Plot with Ticks", xlabel="X-Values", ylabel="Y-Values", output_file="scatter_plot.txt")

# Example 7: Line chart with numerical axis ticks and saving to file
print("\n--- Example 7: Line Chart with Numerical Axis Ticks (saved to file) ---")
x_line_file = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_line_file = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
data_line_file = [{'x': x_line_file, 'y': y_line_file, 'color': 'yellow', 'marker': '*'}]
tpl.line(data_line_file, title="Line Chart with Ticks", xlabel="X-Values", ylabel="Y-Values", output_file="line_plot.txt")

# Example 8: Bar chart saved to file
print("\n--- Example 8: Bar Chart (saved to file) ---")
labels8 = ["E", "F", "G"]
values8 = [25, 10, 30]
tpl.bar(labels8, values8, title="Another Bar Chart", color="blue", output_file="bar_chart.txt")

# Example 9: Pie chart saved to file
print("\n--- Example 9: Pie Chart (saved to file) ---")
labels9 = ["X", "Y", "Z"]
values9 = [40, 30, 30]
tpl.pie(labels9, values9, title="Another Pie Chart", output_file="pie_chart.txt")

# Example 10: Histogram saved to file
print("\n--- Example 10: Histogram (saved to file) ---")
data_hist_file = [10, 12, 12, 15, 15, 15, 18, 20, 20, 22, 25]
tpl.hist(data_hist_file, bins=4, title="Another Histogram", color="green", output_file="histogram.txt")

# Example 11: Edge cases - empty data
print("\n--- Example 11: Error Handling (empty data) ---")
tpl.bar([], [], title="Empty Bar")

# Example 12: Multi-series scatter with function-level color fallback
print("\n--- Example 12: Multi-series Scatter ---")
x1 = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
x2 = [1, 2, 3, 4, 5]
y2 = [25, 16, 9, 4, 1]
data_multi = [
    {'x': x1, 'y': y1, 'marker': 'o'},
    {'x': x2, 'y': y2, 'marker': 'x'}
]
tpl.scatter(data_multi, title="Multi-Series Scatter", color="cyan")

# Example 13: Scatter with legend
print("\n--- Example 13: Scatter with Legend ---")
x_a = [1, 2, 3, 4, 5]
y_a = [2, 3, 5, 7, 11]
x_b = [1, 2, 3, 4, 5]
y_b = [11, 7, 5, 3, 2]
data_legend = [
    {'x': x_a, 'y': y_a, 'color': 'green', 'marker': 'o', 'label': 'Primes'},
    {'x': x_b, 'y': y_b, 'color': 'red', 'marker': 'x', 'label': 'Descent'}
]
tpl.scatter(data_legend, title="With Legend", legend=True)

# Example 14: Line chart with legend
print("\n--- Example 14: Line Chart with Legend ---")
x_sin = [i * 0.5 for i in range(13)]
y_sin = [__import__('math').sin(x) for x in x_sin]
x_cos = [i * 0.5 for i in range(13)]
y_cos = [__import__('math').cos(x) for x in x_cos]
data_wave = [
    {'x': x_sin, 'y': y_sin, 'color': 'blue', 'marker': '.', 'label': 'sin(x)'},
    {'x': x_cos, 'y': y_cos, 'color': 'red', 'marker': '.', 'label': 'cos(x)'},
]
tpl.line(data_wave, title="Waves", legend=True)

# Example 15: More bar
print("\n--- Example 15: Bar Chart ---")
tpl.bar(["Q1", "Q2", "Q3"], [300, 150, 200], title="Quarterly Sales", xlabel="Revenue", color="green")

# Example 16: Grouped bar chart
print("\n--- Example 16: Grouped Bar Chart ---")
tpl.grouped_bar(
    ["Apples", "Bananas", "Oranges"],
    [[30, 20, 25], [20, 35, 15]],
    title="Fruit Sales by Region",
    xlabel="Quantity",
    colors=["red", "blue"]
)

# Example 17: Stacked bar chart
print("\n--- Example 17: Stacked Bar Chart ---")
tpl.stacked_bar(
    ["Q1", "Q2", "Q3", "Q4"],
    [[100, 120, 110, 130], [80, 90, 95, 100], [60, 70, 65, 80]],
    title="Quarterly Revenue by Product",
    xlabel="Revenue",
    colors=["cyan", "magenta", "yellow"]
)

# Example 18: Area chart
print("\n--- Example 18: Area Chart ---")
x_area = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_area = [0, 2, 3, 5, 7, 10, 8, 6, 4, 2, 1]
tpl.area([{'x': x_area, 'y': y_area, 'color': 'green', 'marker': 'o'}],
         title="Area Under Curve", legend=True)

# Example 19: Stacked area chart
print("\n--- Example 19: Stacked Area Chart ---")
x_sa = [0, 1, 2, 3, 4, 5]
y1_sa = [1, 2, 3, 4, 5, 6]
y2_sa = [1, 2, 1, 2, 1, 2]
tpl.area([
    {'x': x_sa, 'y': y1_sa, 'color': 'blue', 'marker': 'o', 'label': 'Series A'},
    {'x': x_sa, 'y': y2_sa, 'color': 'red', 'marker': 'x', 'label': 'Series B'},
], title="Stacked Area", stacked=True, legend=True)

# Example 20: Box plot
print("\n--- Example 20: Box Plot ---")
import random
random.seed(42)
data_box = [
    [random.gauss(50, 10) for _ in range(50)],
    [random.gauss(60, 15) for _ in range(50)],
    [random.gauss(45, 8) for _ in range(50)],
]
tpl.boxplot(data_box, labels=["Group A", "Group B", "Group C"],
            title="Distribution Comparison", color="cyan")

# Example 21: Scatter with grid lines
print("\n--- Example 21: Scatter with Grid Lines ---")
x_grid = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_grid = [3, 6, 2, 8, 5, 9, 4, 7, 1, 10]
tpl.scatter([{'x': x_grid, 'y': y_grid, 'color': 'magenta', 'marker': 'o'}],
            title="With Grid Lines", grid=True)

# Example 22: Line with axis limits
print("\n--- Example 22: Line with Custom Axis Limits ---")
x_lim = [1, 2, 3, 4, 5]
y_lim = [10, 20, 15, 30, 25]
tpl.line([{'x': x_lim, 'y': y_lim, 'color': 'red', 'marker': '*'}],
         title="Zoomed View", xlim=(0, 6), ylim=(0, 40))

# Example 23: Line with grid and limits
print("\n--- Example 23: Line with Grid + Limits ---")
x_sin = [i * 0.25 for i in range(25)]
y_sin = [__import__('math').sin(x) for x in x_sin]
tpl.line([{'x': x_sin, 'y': y_sin, 'color': 'blue', 'marker': '.'}],
         title="Sine Wave", xlim=(0, 6), ylim=(-1.5, 1.5), grid=True)

# Example 24: Bar with negative values
print("\n--- Example 24: Bar with Negative Values ---")
tpl.bar(["Profit", "Loss", "Tax", "Revenue"],
        [100, -30, -20, 150], title="Financials", color="cyan")

# Example 25: Bar with error bars
print("\n--- Example 25: Bar with Error Bars ---")
tpl.bar(["A", "B", "C"], [10, 20, 15], max_width=40, color="green", error_y=[1, 2, 1.5])

# Example 26: Scatter with log scale
print("\n--- Example 26: Scatter with Log-Y Scale ---")
tpl.scatter([{'x': [1, 2, 3, 4, 5], 'y': [1, 10, 100, 1000, 10000], 'marker': 'o'}],
            width=40, height=15, title="Log Scale", log_y=True)

# Example 27: Scatter with error bars
print("\n--- Example 27: Scatter with Error Bars ---")
tpl.scatter([{'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10], 'error_y': 0.5, 'marker': 'o'}],
            width=30, height=15, title="With Error Bars")

# Example 28: Line with log scale and grid
print("\n--- Example 28: Line with Log-Log and Grid ---")
import math
x_log = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_log = [x**2 for x in x_log]
tpl.line([{'x': x_log, 'y': y_log, 'color': 'blue', 'marker': '.'}],
         title="Quadratic (Log-Log)", log_x=True, log_y=True, grid=True, width=40, height=15)

# Example 29: Heatmap
print("\n--- Example 29: Heatmap ---")
data_heat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
tpl.heatmap(data_heat, row_labels=["Row1", "Row2", "Row3"],
            col_labels=["Col1", "Col2", "Col3", "Col4"],
            title="Basic Heatmap", color="cyan")

# Example 30: Heatmap with custom palette
print("\n--- Example 30: Heatmap with Palette ---")
tpl.heatmap([[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]],
            title="Heatmap with Palette", palette=["red", "yellow", "green"])

# Example 31: Figure with multiple charts
print("\n--- Example 31: Multi-Figure Dashboard ---")
fig = tpl.Figure(title="Dashboard")
fig.add_chart(tpl.bar, ["Q1", "Q2", "Q3", "Q4"], [150, 200, 175, 250],
              max_width=40, color="blue")
fig.add_chart(tpl.pie, ["Sales", "Marketing", "R&D", "Support"], [40, 25, 20, 15],
              radius=8)
fig.render()

# Example 32: Figure saved to file
print("\n--- Example 32: Figure saved to file ---")
fig2 = tpl.Figure(title="Report")
fig2.add_chart(tpl.bar, ["A", "B"], [10, 20], max_width=40)
fig2.add_chart(tpl.hist, [1, 2, 2, 3, 3, 3, 4, 5], bins=4, width=40)
fig2.savefig("report.txt")
print("Saved to report.txt")

# Example 33: Vertical bar chart
print("\n--- Example 33: Vertical Bar Chart ---")
tpl.vertical_bar(["Q1", "Q2", "Q3", "Q4"], [15, 25, 20, 30],
                 height=12, width=30, title="Quarterly", color="blue")

# Example 34: Diverging bar chart
print("\n--- Example 34: Diverging Bar Chart ---")
tpl.diverging_bar(["Revenue", "Cost", "Profit", "Loss"],
                  [200, -80, 120, -50], max_width=50, title="P&L",
                  colors=["green", "red"])

# Example 35: Sparkline
print("\n--- Example 35: Sparkline ---")
tpl.sparkline([1, 5, 22, 13, 5, 8, 3, 10, 15, 7, 2, 6],
              title="Sparkline Trend", color="green")

# Example 36: Candlestick chart
print("\n--- Example 36: Candlestick Chart ---")
candle_data = [
    {'open': 100, 'high': 110, 'low': 95, 'close': 105},
    {'open': 105, 'high': 115, 'low': 100, 'close': 102},
    {'open': 102, 'high': 108, 'low': 98, 'close': 107},
    {'open': 107, 'high': 112, 'low': 103, 'close': 104},
    {'open': 104, 'high': 118, 'low': 101, 'close': 115},
]
tpl.candlestick(candle_data, width=40, height=15, title="Stock Price")

# Example 37: Violin plot
print("\n--- Example 37: Violin Plot ---")
import random
random.seed(42)
v_data = [
    [random.gauss(50, 10) for _ in range(80)],
    [random.gauss(60, 15) for _ in range(80)],
    [random.gauss(45, 8) for _ in range(80)],
]
tpl.violinplot(v_data, labels=["Group A", "Group B", "Group C"],
               width=50, height=15, title="Distribution Comparison", color="cyan")

# Example 38: Calendar heatmap
print("\n--- Example 38: Calendar Heatmap ---")
cal_data = {}
for d in range(1, 366):
    import datetime
    dt = datetime.date(2026, 1, 1) + datetime.timedelta(days=d - 1)
    cal_data[dt.isoformat()] = int(random.random() * 15)
tpl.calendar_heatmap(cal_data, title="Year of Activity", color="green")

# Example 39: Threshold lines on scatter
print("\n--- Example 39: Scatter with Threshold Lines ---")
tpl.scatter([{'x': [1, 2, 3, 4, 5], 'y': [3, 6, 2, 8, 4], 'marker': 'o'}],
            width=30, height=15, title="With Thresholds",
            thresholds=[
                {'axis': 'y', 'value': 5, 'color': 'red', 'char': '-'},
                {'axis': 'y', 'value': 3, 'color': 'green', 'char': '-'},
            ])

# Example 40: Custom ticks and formatter
print("\n--- Example 40: Custom Ticks with Currency Formatter ---")
tpl.scatter([{'x': [1, 2, 3, 4, 5], 'y': [10, 20, 15, 30, 25]}],
            width=30, height=15, title="Revenue",
            custom_yticks=[10, 15, 20, 25, 30],
            tick_formatter=lambda v: f"${v:.0f}")

# Example 41: Theme system
print("\n--- Example 41: Theme System ---")
tpl.apply_theme('monokai')
tpl.bar(["A", "B", "C"], [10, 20, 15], max_width=40, title="Monokai Theme")
tpl.reset_defaults()

# Example 42: Radar chart
print("\n--- Example 42: Radar Chart ---")
tpl.radar(["Speed", "Power", "Agility", "Stamina", "Intelligence"],
          [8, 6, 9, 5, 7], width=30, title="Player Attributes", fill=True, color="red")

# Example 43: Waterfall chart
print("\n--- Example 43: Waterfall Chart ---")
tpl.waterfall(["Revenue", "COGS", "R&D", "Marketing", "Net Profit"],
              [1000, -400, -200, -100, 300], width=60, title="P&L Bridge",
              color_up="green", color_down="red", color_total="blue")

# Example 44: Gantt chart
print("\n--- Example 44: Gantt Chart ---")
tpl.gantt([
    {'label': 'Research',  'start': 0,  'end': 5},
    {'label': 'Design',    'start': 3,  'end': 8},
    {'label': 'Frontend',  'start': 6,  'end': 12},
    {'label': 'Backend',   'start': 7,  'end': 13},
    {'label': 'Testing',   'start': 11, 'end': 15},
    {'label': 'Launch',    'start': 14, 'end': 16},
], width=60, title="Project Timeline")

# Example 45: Step chart
print("\n--- Example 45: Step Chart ---")
tpl.step([
    {'x': [0, 1, 2, 3, 4, 5], 'y': [0, 0, 3, 3, 7, 7], 'label': 'Stairs', 'color': 'cyan'},
    {'x': [0, 1, 2, 3, 4, 5], 'y': [0, 2, 2, 5, 5, 8], 'label': 'Ramp', 'color': 'magenta'},
], width=40, height=14, title="Step Comparison", legend=True, grid=True)

# Example 46: Bubble chart
print("\n--- Example 46: Bubble Chart ---")
tpl.bubble([{'x': [1, 2, 3, 4, 5], 'y': [10, 25, 15, 30, 20],
             'size': [2, 10, 5, 15, 8], 'label': 'Products', 'color': 'green'}],
           width=40, height=15, title="Product Portfolio", legend=True)

# Example 47: Strip plot
print("\n--- Example 47: Strip Plot ---")
data = []
for _ in range(50):
    import random
    data.append(random.gauss(5, 1.5))
tpl.strip(data, width=40, title="Distribution", color="cyan")

# Example 48: Sankey diagram
print("\n--- Example 48: Sankey Diagram ---")
tpl.sankey(
    ["Revenue", "Costs", "Tax", "Profit"],
    [
        {"source": "Revenue", "target": "Costs", "value": 400},
        {"source": "Revenue", "target": "Tax", "value": 200},
        {"source": "Revenue", "target": "Profit", "value": 400},
    ],
    width=60, title="Cash Flow"
)

# Example 49: Funnel chart
print("\n--- Example 49: Funnel Chart ---")
tpl.funnel(["Awareness", "Interest", "Desire", "Action"],
           [1000, 500, 200, 50], width=50, title="Sales Pipeline", color="cyan")

# Example 50: Bullet chart
print("\n--- Example 50: Bullet Chart ---")
tpl.bullet(["Revenue", "Users", "Satisfaction"],
           [85, 70, 90], [100, 80, 95], width=60, title="KPI Dashboard")

# Example 51: Donut chart
print("\n--- Example 51: Donut Chart ---")
tpl.donut(["Product", "Service", "Subscription", "Other"],
          [40, 30, 20, 10], title="Revenue Mix", legend=True)

# Example 52: Pareto chart
print("\n--- Example 52: Pareto Chart ---")
tpl.pareto(["Issue A", "Issue B", "Issue C", "Issue D"],
           [50, 30, 15, 5], width=60, title="Bug Priority")

# Example 53: Word cloud
print("\n--- Example 53: Word Cloud ---")
tpl.wordcloud({
    "python": 10, "data": 8, "chart": 5, "terminal": 4,
    "ascii": 3, "visualization": 3, "library": 2, "open": 2,
    "source": 2, "code": 1, "tool": 1, "plot": 1,
}, width=50, title="Tag Cloud")
