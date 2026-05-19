# Contributing

## Development Setup

```bash
git clone https://github.com/rkriad585/termatplotlib
cd termatplotlib
pip install -e .
```

## Running Tests

```bash
pytest
# or with verbose output:
pytest -v
```

All tests are in `tests/test_termatplotlib.py`.

## Code Style

- Follow PEP 8
- Use type hints for all function parameters and return types
- No external dependencies beyond Python stdlib
- Mimic existing code patterns and conventions

## Adding a New Chart Type

1. Create a new module `termatplotlib/newchart.py`
2. Add a public function following the existing pattern:
   - Accept `output_file` and `_return_output` parameters
   - Call `write_output()` at the end
   - Return `(output if _return_output else None)`
3. Import and re-export from `termatplotlib/__init__.py`
4. Add tests in `tests/test_termatplotlib.py`
5. Document in `README.md` and `docs/`

## Commit Guidelines

- Write clear, concise commit messages
- Reference issue numbers if applicable
- Keep commits focused on single changes

## Project Structure

```
termatplotlib/
    __init__.py      Public API re-exports
    bar.py           Bar chart functions
    scatter.py       Scatter plot
    line.py          Line and area charts
    pie.py           Pie chart
    hist.py          Histogram
    boxplot.py       Box plot
    heatmap.py       Heatmap
    figure.py        Figure API
    utils.py         Shared utilities
tests/
    test_termatplotlib.py    All tests
```

## Pull Requests

1. Ensure all tests pass
2. Add tests for new functionality
3. Update documentation
4. Verify no ANSI codes leak into file output
