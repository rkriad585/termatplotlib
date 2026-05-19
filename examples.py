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
