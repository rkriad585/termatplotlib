# Configuration System

Global configuration lets you set default parameter values that apply to all subsequent chart calls.

## set_default

```python
tpl.set_default(width=80, height=30, color='blue', legend=True, grid=True)
```

Supported keys:

| Key | Affects | Type |
|-----|---------|------|
| `width` | scatter, line, area, boxplot, heatmap | `int` |
| `height` | scatter, line, area, hist, boxplot | `int` |
| `max_width` | bar, grouped_bar, stacked_bar | `int` |
| `color` | bar, scatter, line, area, hist, boxplot, heatmap | `str` |
| `legend` | scatter, line, area | `bool` |
| `grid` | scatter, line, area | `bool` |

## get_default

```python
current_width = tpl.get_default('width')   # returns value or None
```

## reset_defaults

```python
tpl.reset_defaults()   # clears all stored defaults
```

## Example

```python
import termatplotlib as tpl

tpl.set_default(width=60, height=20, color='cyan', legend=True, grid=True)

# All subsequent charts use these settings:
tpl.scatter([{'x': [1, 2, 3], 'y': [4, 5, 6]}])   # width=60, height=20, color=cyan
tpl.line([{'x': [0, 1], 'y': [0, 1]}])              # same defaults

# Override per-call:
tpl.scatter([{'x': [1, 2], 'y': [3, 4]}], width=30)  # this call uses width=30

tpl.reset_defaults()
```

## Priority

Explicit function parameters take priority over global defaults.
