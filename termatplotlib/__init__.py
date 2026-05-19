from termatplotlib.bar import bar, grouped_bar, stacked_bar
from termatplotlib.scatter import scatter
from termatplotlib.line import line, area
from termatplotlib.pie import pie
from termatplotlib.hist import hist
from termatplotlib.boxplot import boxplot
from termatplotlib.heatmap import heatmap
from termatplotlib.figure import Figure
from termatplotlib.utils import (
    COLORS, get_terminal_width, strip_ansi,
    set_default, get_default, reset_defaults,
)

__all__ = [
    'bar', 'grouped_bar', 'stacked_bar',
    'scatter',
    'line', 'area',
    'pie',
    'hist',
    'boxplot',
    'heatmap',
    'Figure',
    'COLORS', 'get_terminal_width', 'strip_ansi',
    'set_default', 'get_default', 'reset_defaults',
]
