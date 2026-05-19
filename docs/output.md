# Output & Formatting

## Terminal Output

By default, all chart functions print directly to the terminal with ANSI color codes. The output is rendered immediately when the function is called.

```python
tpl.bar(["A", "B"], [10, 20], color="green")
# Prints colored bar chart to stdout
```

## File Output

Pass `output_file="path.txt"` to save the chart to a file. ANSI color codes are automatically stripped from the file content.

```python
tpl.bar(["A", "B"], [10, 20], color="green", output_file="chart.txt")
# Saves clean text without ANSI codes to chart.txt
```

This works on all chart types.

## Figure Output

Use the `Figure` class to compose multiple charts into one output:

```python
fig = tpl.Figure(title="Report")
fig.add_chart(tpl.bar, ["A", "B"], [10, 20], max_width=40)
fig.add_chart(tpl.pie, ["X", "Y"], [30, 70])
fig.render()                          # print to terminal
fig.savefig("report.txt")             # save to file (ANSI stripped)
```

## ANSI Strip Behavior

- File output: all ANSI escape codes (`\033[...m`) are removed
- Terminal output: ANSI codes are preserved for colored display
- The `strip_ansi()` utility is available for custom use

```python
clean = tpl.strip_ansi("\033[31mHello\033[0m")  # "Hello"
```

## Output Files Generated

The project's `.gitignore` excludes common generated output files (`*.txt` in the root) to prevent accidental commits.
