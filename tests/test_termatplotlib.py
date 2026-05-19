import os
import re
import tempfile
import math

import termatplotlib as tpl

ANSI_RE = re.compile(r'\033\[[0-9;]*m')


def _has_ansi(text):
    return bool(ANSI_RE.search(text))


def _read_file(path):
    with open(path, 'r') as f:
        return f.read()


class TestBar:
    def test_basic_bar(self):
        tpl.bar(["A", "B"], [10, 20], max_width=40)

    def test_bar_with_title(self):
        tpl.bar(["A", "B"], [10, 20], max_width=40, title="Test")

    def test_bar_with_color(self):
        tpl.bar(["A", "B"], [10, 20], max_width=40, color="red")

    def test_bar_with_labels(self):
        tpl.bar(["A", "B"], [10, 20], max_width=40, xlabel="X", ylabel="Y")

    def test_bar_empty(self):
        tpl.bar([], [], max_width=40)

    def test_bar_mismatched(self):
        tpl.bar(["A"], [10, 20], max_width=40)

    def test_bar_output_file_no_ansi(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            path = f.name
        try:
            tpl.bar(["A", "B"], [10, 20], max_width=40, color="red", output_file=path)
            content = _read_file(path)
            assert not _has_ansi(content), "Output file contains ANSI codes"
        finally:
            os.unlink(path)

    def test_bar_single_item(self):
        tpl.bar(["A"], [5], max_width=40)

    def test_bar_negative_values(self):
        tpl.bar(["A", "B"], [-5, 10], max_width=40)


class TestScatter:
    def test_basic_scatter(self):
        data = [{'x': [1, 2, 3], 'y': [4, 5, 6]}]
        tpl.scatter(data, width=20, height=10)

    def test_scatter_with_title(self):
        data = [{'x': [1, 2, 3], 'y': [4, 5, 6]}]
        tpl.scatter(data, width=20, height=10, title="Test")

    def test_scatter_multi_series(self):
        data = [
            {'x': [1, 2], 'y': [3, 4], 'color': 'red', 'marker': 'o'},
            {'x': [1, 2], 'y': [5, 6], 'color': 'blue', 'marker': 'x'},
        ]
        tpl.scatter(data, width=20, height=10)

    def test_scatter_with_legend(self):
        data = [
            {'x': [1, 2], 'y': [3, 4], 'label': 'First'},
            {'x': [1, 2], 'y': [5, 6], 'label': 'Second'},
        ]
        tpl.scatter(data, width=20, height=10, legend=True)

    def test_scatter_empty_data(self):
        tpl.scatter([], width=20, height=10)

    def test_scatter_single_point(self):
        data = [{'x': [5], 'y': [5]}]
        tpl.scatter(data, width=20, height=10)

    def test_scatter_mismatched_lengths(self):
        data = [{'x': [1, 2], 'y': [3]}]
        tpl.scatter(data, width=20, height=10)

    def test_scatter_color_fallback(self):
        data = [{'x': [1, 2], 'y': [3, 4], 'marker': 'o'}]
        tpl.scatter(data, width=20, height=10, color="green")

    def test_scatter_output_file_no_ansi(self):
        data = [{'x': [1, 2, 3], 'y': [4, 5, 6], 'color': 'cyan'}]
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            path = f.name
        try:
            tpl.scatter(data, width=20, height=10, output_file=path)
            content = _read_file(path)
            assert not _has_ansi(content), "Output file contains ANSI codes"
        finally:
            os.unlink(path)

    def test_scatter_custom_marker(self):
        data = [{'x': [1, 2], 'y': [3, 4], 'marker': '+'}]
        tpl.scatter(data, width=20, height=10)


class TestLine:
    def test_basic_line(self):
        data = [{'x': [0, 1, 2], 'y': [0, 1, 4]}]
        tpl.line(data, width=20, height=10)

    def test_line_multi_series(self):
        data = [
            {'x': [0, 1, 2], 'y': [0, 1, 4], 'color': 'green'},
            {'x': [0, 1, 2], 'y': [4, 1, 0], 'color': 'red'},
        ]
        tpl.line(data, width=20, height=10)

    def test_line_legend(self):
        data = [
            {'x': [0, 1, 2], 'y': [0, 1, 4], 'label': 'Up'},
            {'x': [0, 1, 2], 'y': [4, 1, 0], 'label': 'Down'},
        ]
        tpl.line(data, width=20, height=10, legend=True)

    def test_line_single_point(self):
        data = [{'x': [5], 'y': [5]}]
        tpl.line(data, width=20, height=10)

    def test_line_output_file_no_ansi(self):
        data = [{'x': [0, 1, 2], 'y': [0, 1, 4], 'color': 'yellow'}]
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            path = f.name
        try:
            tpl.line(data, width=20, height=10, output_file=path)
            content = _read_file(path)
            assert not _has_ansi(content), "Output file contains ANSI codes"
        finally:
            os.unlink(path)


class TestPie:
    def test_basic_pie(self):
        tpl.pie(["A", "B", "C"], [10, 20, 15])

    def test_pie_with_title(self):
        tpl.pie(["A", "B"], [10, 20], title="Test")

    def test_pie_no_legend(self):
        tpl.pie(["A", "B"], [10, 20], legend=False)

    def test_pie_empty(self):
        tpl.pie([], [])

    def test_pie_single_slice(self):
        tpl.pie(["Only"], [100])

    def test_pie_output_file_no_ansi(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            path = f.name
        try:
            tpl.pie(["A", "B"], [30, 70], output_file=path)
            content = _read_file(path)
            assert not _has_ansi(content), "Output file contains ANSI codes"
        finally:
            os.unlink(path)


class TestHist:
    def test_basic_hist(self):
        tpl.hist([1, 2, 2, 3, 3, 3, 4, 5], bins=5, width=40)

    def test_hist_with_title(self):
        tpl.hist([1, 2, 3, 4, 5], bins=3, width=40, title="Test")

    def test_hist_empty(self):
        tpl.hist([], bins=5, width=40)

    def test_hist_all_same(self):
        tpl.hist([5, 5, 5, 5], bins=5, width=40)

    def test_hist_with_color(self):
        tpl.hist([1, 2, 3, 4, 5], bins=3, width=40, color="magenta")

    def test_hist_with_labels(self):
        tpl.hist([1, 2, 3, 4, 5], bins=3, width=40, xlabel="X", ylabel="Y")

    def test_hist_output_file_no_ansi(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            path = f.name
        try:
            tpl.hist([1, 2, 2, 3, 3, 3, 4, 5], bins=4, width=40, color="green", output_file=path)
            content = _read_file(path)
            assert not _has_ansi(content), "Output file contains ANSI codes"
        finally:
            os.unlink(path)


class TestGroupedBar:
    def test_basic_grouped_bar(self):
        tpl.grouped_bar(["A", "B"], [[10, 20], [15, 25]], max_width=40)

    def test_grouped_bar_with_colors(self):
        tpl.grouped_bar(["A", "B"], [[10, 20], [15, 25]], max_width=40, colors=["red", "blue"])

    def test_grouped_bar_output_file(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            path = f.name
        try:
            tpl.grouped_bar(["A", "B"], [[10, 20], [15, 25]], max_width=40, output_file=path)
            content = _read_file(path)
            assert not _has_ansi(content)
        finally:
            os.unlink(path)


class TestStackedBar:
    def test_basic_stacked_bar(self):
        tpl.stacked_bar(["A", "B"], [[10, 20], [5, 10]], max_width=40)

    def test_stacked_bar_three_series(self):
        tpl.stacked_bar(["A", "B"], [[10, 20], [5, 10], [3, 5]], max_width=40)

    def test_stacked_bar_output_file(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            path = f.name
        try:
            tpl.stacked_bar(["A", "B"], [[10, 20], [5, 10]], max_width=40, output_file=path)
            content = _read_file(path)
            assert not _has_ansi(content)
        finally:
            os.unlink(path)


class TestArea:
    def test_basic_area(self):
        data = [{'x': [0, 1, 2], 'y': [0, 1, 0]}]
        tpl.area(data, width=20, height=10)

    def test_stacked_area(self):
        data = [
            {'x': [0, 1, 2], 'y': [1, 2, 1]},
            {'x': [0, 1, 2], 'y': [1, 2, 1]},
        ]
        tpl.area(data, width=20, height=10, stacked=True)

    def test_area_legend(self):
        data = [{'x': [0, 1, 2], 'y': [0, 1, 0], 'label': 'Curve'}]
        tpl.area(data, width=20, height=10, legend=True)

    def test_area_output_file(self):
        data = [{'x': [0, 1, 2], 'y': [0, 1, 0]}]
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            path = f.name
        try:
            tpl.area(data, width=20, height=10, output_file=path)
            content = _read_file(path)
            assert not _has_ansi(content)
        finally:
            os.unlink(path)


class TestBoxPlot:
    def test_basic_boxplot(self):
        data = [
            [1, 2, 3, 4, 5],
            [2, 3, 4, 5, 6],
        ]
        tpl.boxplot(data, width=30, height=10)

    def test_boxplot_with_labels(self):
        data = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
        tpl.boxplot(data, labels=["A", "B"], width=30, height=10)

    def test_boxplot_with_title(self):
        data = [[1, 2, 3, 4, 5]]
        tpl.boxplot(data, width=30, height=10, title="Test Box")

    def test_boxplot_three_groups(self):
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        tpl.boxplot(data, width=30, height=10)

    def test_boxplot_output_file(self):
        data = [[1, 2, 3, 4, 5]]
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            path = f.name
        try:
            tpl.boxplot(data, width=30, height=10, output_file=path)
            content = _read_file(path)
            assert not _has_ansi(content)
        finally:
            os.unlink(path)


class TestUtils:
    def test_strip_ansi(self):
        assert tpl.strip_ansi("\033[31mHello\033[0m") == "Hello"

    def test_strip_ansi_no_ansi(self):
        assert tpl.strip_ansi("Hello") == "Hello"

    def test_get_terminal_width(self):
        w = tpl.get_terminal_width()
        assert w >= 20

    def test_colors_present(self):
        assert 'red' in tpl.COLORS
        assert 'green' in tpl.COLORS
        assert 'blue' in tpl.COLORS


class TestGrid:
    def test_scatter_grid(self):
        tpl.scatter([{'x': [1, 2, 3], 'y': [4, 5, 6]}], width=20, height=10, grid=True)

    def test_line_grid(self):
        tpl.line([{'x': [0, 1, 2], 'y': [0, 1, 4]}], width=20, height=10, grid=True)

    def test_area_grid(self):
        tpl.area([{'x': [0, 1, 2], 'y': [0, 1, 0]}], width=20, height=10, grid=True)


class TestAxisLimits:
    def test_scatter_xlim(self):
        tpl.scatter([{'x': [1, 2, 3], 'y': [4, 5, 6]}], width=20, height=10, xlim=(0, 10))

    def test_scatter_ylim(self):
        tpl.scatter([{'x': [1, 2, 3], 'y': [4, 5, 6]}], width=20, height=10, ylim=(0, 20))

    def test_scatter_both_limits(self):
        tpl.scatter([{'x': [1, 2, 3], 'y': [4, 5, 6]}], width=20, height=10, xlim=(0, 10), ylim=(0, 20))

    def test_line_xlim(self):
        tpl.line([{'x': [0, 1, 2], 'y': [0, 1, 4]}], width=20, height=10, xlim=(-1, 5))

    def test_line_ylim(self):
        tpl.line([{'x': [0, 1, 2], 'y': [0, 1, 4]}], width=20, height=10, ylim=(-1, 10))


class TestNegativeValues:
    def test_bar_negative(self):
        tpl.bar(["A", "B"], [-5, 10], max_width=40)

    def test_bar_all_negative(self):
        tpl.bar(["A", "B"], [-10, -5], max_width=40)

    def test_grouped_bar_negative(self):
        tpl.grouped_bar(["A", "B"], [[-10, 20], [15, -5]], max_width=40)

    def test_stacked_bar_negative(self):
        tpl.stacked_bar(["A", "B"], [[10, 20], [5, -5]], max_width=40)


class TestConfig:
    def test_set_and_get_default(self):
        tpl.set_default(color='red', width=100)
        assert tpl.get_default('color') == 'red'
        assert tpl.get_default('width') == 100
        tpl.reset_defaults()
        assert tpl.get_default('color') is None

    def test_reset_defaults(self):
        tpl.set_default(color='blue')
        tpl.reset_defaults()
        assert tpl.get_default('color') is None

    def test_config_affects_scatter(self):
        tpl.set_default(width=20, height=10)
        tpl.scatter([{'x': [1, 2], 'y': [3, 4]}])
        tpl.reset_defaults()

    def test_config_affects_bar(self):
        tpl.set_default(color='green')
        tpl.bar(["A"], [5], max_width=40)
        tpl.reset_defaults()


class TestLogScale:
    def test_scatter_log_x(self):
        tpl.scatter([{'x': [1, 10, 100], 'y': [1, 2, 3]}], width=20, height=10, log_x=True)

    def test_scatter_log_y(self):
        tpl.scatter([{'x': [1, 2, 3], 'y': [1, 10, 100]}], width=20, height=10, log_y=True)

    def test_scatter_log_both(self):
        tpl.scatter([{'x': [1, 10, 100], 'y': [1, 10, 100]}], width=20, height=10, log_x=True, log_y=True)

    def test_line_log_x(self):
        tpl.line([{'x': [1, 10, 100], 'y': [0, 1, 2]}], width=20, height=10, log_x=True)

    def test_line_log_y(self):
        tpl.line([{'x': [0, 1, 2], 'y': [1, 10, 100]}], width=20, height=10, log_y=True)

    def test_area_log_y(self):
        tpl.area([{'x': [0, 1, 2], 'y': [1, 10, 100]}], width=20, height=10, log_y=True)

    def test_log_scale_with_xlim(self):
        tpl.scatter([{'x': [1, 10, 100], 'y': [1, 2, 3]}], width=20, height=10, log_x=True, xlim=(1, 200))

    def test_log_scale_non_positive_error(self):
        tpl.scatter([{'x': [0, 1, 2], 'y': [1, 2, 3]}], width=20, height=10, log_x=True)

    def test_log_output_file_no_ansi(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            path = f.name
        try:
            tpl.scatter([{'x': [1, 10, 100], 'y': [1, 2, 3]}], width=20, height=10, log_x=True, output_file=path)
            content = _read_file(path)
            assert not _has_ansi(content)
        finally:
            os.unlink(path)

    def test_line_log_scale_with_grid(self):
        tpl.line([{'x': [1, 10, 100], 'y': [1, 10, 100]}], width=20, height=10, log_x=True, log_y=True, grid=True)


class TestErrorBars:
    def test_bar_error_y_single(self):
        tpl.bar(["A", "B"], [10, 20], max_width=40, error_y=2)

    def test_bar_error_y_list(self):
        tpl.bar(["A", "B"], [10, 20], max_width=40, error_y=[1, 3])

    def test_bar_error_y_file_output(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            path = f.name
        try:
            tpl.bar(["A", "B"], [10, 20], max_width=40, error_y=1.5, output_file=path)
            content = _read_file(path)
            assert not _has_ansi(content)
        finally:
            os.unlink(path)

    def test_scatter_error_y(self):
        tpl.scatter([{'x': [1, 2, 3], 'y': [4, 5, 6], 'error_y': 1}], width=20, height=10)

    def test_scatter_error_y_list(self):
        tpl.scatter([{'x': [1, 2, 3], 'y': [4, 5, 6], 'error_y': [0.5, 1, 1.5]}], width=20, height=10)

    def test_line_error_y(self):
        tpl.line([{'x': [0, 1, 2], 'y': [0, 1, 4], 'error_y': 0.5}], width=20, height=10)


class TestHeatmap:
    def test_basic_heatmap(self):
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        tpl.heatmap(data)

    def test_heatmap_with_labels(self):
        data = [[1, 2], [3, 4]]
        tpl.heatmap(data, row_labels=["A", "B"], col_labels=["X", "Y"])

    def test_heatmap_with_title(self):
        tpl.heatmap([[1, 2], [3, 4]], title="Test Heatmap")

    def test_heatmap_with_color(self):
        tpl.heatmap([[1, 2], [3, 4]], color="red")

    def test_heatmap_empty(self):
        tpl.heatmap([], width=40)

    def test_heatmap_uneven_rows(self):
        tpl.heatmap([[1, 2], [3]], width=40)

    def test_heatmap_output_file(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            path = f.name
        try:
            tpl.heatmap([[1, 2], [3, 4]], output_file=path)
            content = _read_file(path)
            assert not _has_ansi(content)
        finally:
            os.unlink(path)

    def test_heatmap_single_value(self):
        tpl.heatmap([[5]], width=40)

    def test_heatmap_constant_values(self):
        tpl.heatmap([[1, 1], [1, 1]], width=40)

    def test_heatmap_with_palette(self):
        tpl.heatmap([[1, 2, 3], [4, 5, 6]], palette=["red", "blue"])


class TestFigure:
    def test_figure_basic(self):
        fig = tpl.Figure(title="Multi-Chart")
        fig.add_chart(tpl.bar, ["A", "B"], [10, 20], max_width=40)
        fig.add_chart(tpl.pie, ["X", "Y"], [30, 70])
        fig.render()

    def test_figure_savefig(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            path = f.name
        try:
            fig = tpl.Figure()
            fig.add_chart(tpl.bar, ["A"], [5], max_width=40)
            fig.savefig(path)
            content = _read_file(path)
            assert not _has_ansi(content)
        finally:
            os.unlink(path)

    def test_figure_chaining(self):
        fig = tpl.Figure().add_chart(tpl.bar, ["A"], [5], max_width=40)
        fig.render()

    def test_figure_multiple_charts(self):
        fig = tpl.Figure(title="Three Charts")
        fig.add_chart(tpl.bar, ["A", "B"], [5, 10], max_width=40, color="red")
        fig.add_chart(tpl.scatter, [{'x': [1, 2], 'y': [3, 4]}], width=20, height=10)
        fig.add_chart(tpl.pie, ["A", "B"], [30, 70])
        fig.render()


class TestThemes:
    def test_apply_theme_default(self):
        tpl.apply_theme('default')
        assert tpl.get_default('color') is not None
        tpl.reset_defaults()

    def test_apply_theme_dark(self):
        tpl.apply_theme('dark')
        assert tpl.get_default('color') == 'blue'
        tpl.reset_defaults()

    def test_apply_theme_invalid(self):
        try:
            tpl.apply_theme('nonexistent')
        except ValueError:
            pass

    def test_themes_present(self):
        assert 'default' in tpl.THEMES
        assert 'monokai' in tpl.THEMES
        assert 'ocean' in tpl.THEMES


class TestVerticalBar:
    def test_basic_vertical_bar(self):
        tpl.vertical_bar(["A", "B", "C"], [10, 20, 15], height=10, width=30)

    def test_vertical_bar_with_title(self):
        tpl.vertical_bar(["A", "B"], [10, 20], height=10, width=30, title="Test")

    def test_vertical_bar_empty(self):
        tpl.vertical_bar([], [], height=10, width=30)

    def test_vertical_bar_output_file(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            path = f.name
        try:
            tpl.vertical_bar(["A"], [5], height=10, width=30, output_file=path)
            content = _read_file(path)
            assert not _has_ansi(content)
        finally:
            os.unlink(path)


class TestDivergingBar:
    def test_basic_diverging(self):
        tpl.diverging_bar(["A", "B", "C"], [10, -5, 3], max_width=40)

    def test_diverging_with_baseline(self):
        tpl.diverging_bar(["A", "B"], [15, 5], baseline=10, max_width=40)

    def test_diverging_with_colors(self):
        tpl.diverging_bar(["A", "B"], [10, -5], max_width=40, colors=["blue", "red"])

    def test_diverging_output_file(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            path = f.name
        try:
            tpl.diverging_bar(["A"], [10], max_width=40, output_file=path)
            content = _read_file(path)
            assert not _has_ansi(content)
        finally:
            os.unlink(path)


class TestSparkline:
    def test_basic_sparkline(self):
        tpl.sparkline([1, 5, 22, 13, 5])

    def test_sparkline_with_title(self):
        tpl.sparkline([1, 2, 3, 4, 5], title="Trend")

    def test_sparkline_with_color(self):
        tpl.sparkline([1, 2, 3], color="green")

    def test_sparkline_empty(self):
        tpl.sparkline([])

    def test_sparkline_custom_range(self):
        tpl.sparkline([1, 2, 3], min_val=0, max_val=10)

    def test_sparkline_output_file(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            path = f.name
        try:
            tpl.sparkline([1, 2, 3], output_file=path)
            content = _read_file(path)
            assert not _has_ansi(content)
        finally:
            os.unlink(path)

    def test_sparkline_width_sampling(self):
        tpl.sparkline(list(range(100)), width=10)


class TestCandlestick:
    def test_basic_candlestick(self):
        data = [
            {'open': 100, 'high': 110, 'low': 95, 'close': 105},
            {'open': 105, 'high': 115, 'low': 100, 'close': 102},
        ]
        tpl.candlestick(data, width=30, height=10)

    def test_candlestick_with_title(self):
        data = [{'open': 50, 'high': 55, 'low': 48, 'close': 53}]
        tpl.candlestick(data, width=30, height=10, title="AAPL")

    def test_candlestick_colors(self):
        data = [{'open': 50, 'high': 55, 'low': 48, 'close': 53}]
        tpl.candlestick(data, width=30, height=10, color_up="green", color_down="red")

    def test_candlestick_empty(self):
        tpl.candlestick([], width=30, height=10)

    def test_candlestick_output_file(self):
        data = [{'open': 100, 'high': 110, 'low': 95, 'close': 105}]
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            path = f.name
        try:
            tpl.candlestick(data, width=30, height=10, output_file=path)
            content = _read_file(path)
            assert not _has_ansi(content)
        finally:
            os.unlink(path)


class TestViolin:
    def test_basic_violin(self):
        tpl.violinplot([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]], width=30, height=10)

    def test_violin_with_labels(self):
        tpl.violinplot([[1, 2, 3], [4, 5, 6]], labels=["A", "B"], width=30, height=10)

    def test_violin_with_title(self):
        tpl.violinplot([[1, 2, 3]], width=30, height=10, title="Distribution")

    def test_violin_empty(self):
        tpl.violinplot([[]], width=30, height=10)

    def test_violin_output_file(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            path = f.name
        try:
            tpl.violinplot([[1, 2, 3]], width=30, height=10, output_file=path)
            content = _read_file(path)
            assert not _has_ansi(content)
        finally:
            os.unlink(path)


class TestCalendarHeatmap:
    def test_basic_calendar(self):
        tpl.calendar_heatmap({"2026-01-01": 5, "2026-06-15": 10})

    def test_calendar_with_title(self):
        tpl.calendar_heatmap({"2026-01-01": 1}, title="Contributions")

    def test_calendar_empty(self):
        tpl.calendar_heatmap({})

    def test_calendar_output_file(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            path = f.name
        try:
            tpl.calendar_heatmap({"2026-01-01": 1}, output_file=path)
            content = _read_file(path)
            assert not _has_ansi(content)
        finally:
            os.unlink(path)

    def test_calendar_with_palette(self):
        tpl.calendar_heatmap({"2026-01-01": 1, "2026-06-01": 10}, palette=["blue", "red"])


class TestThresholds:
    def test_scatter_threshold_y(self):
        tpl.scatter([{'x': [1, 2, 3], 'y': [4, 5, 6]}], width=20, height=10,
                    thresholds=[{'axis': 'y', 'value': 5, 'color': 'red'}])

    def test_scatter_threshold_x(self):
        tpl.scatter([{'x': [1, 2, 3], 'y': [4, 5, 6]}], width=20, height=10,
                    thresholds=[{'axis': 'x', 'value': 2, 'color': 'blue'}])

    def test_line_threshold(self):
        tpl.line([{'x': [0, 1, 2], 'y': [0, 1, 4]}], width=20, height=10,
                 thresholds=[{'axis': 'y', 'value': 2, 'color': 'red', 'char': '='}])


class TestCustomTicks:
    def test_scatter_custom_xticks(self):
        tpl.scatter([{'x': [1, 2, 3], 'y': [4, 5, 6]}], width=20, height=10,
                    custom_xticks=[1, 2, 3])

    def test_scatter_custom_yticks(self):
        tpl.scatter([{'x': [1, 2, 3], 'y': [4, 5, 6]}], width=20, height=10,
                    custom_yticks=[4, 5, 6])

    def test_line_custom_ticks(self):
        tpl.line([{'x': [0, 1, 2], 'y': [0, 1, 4]}], width=20, height=10,
                 custom_xticks=[0, 1, 2], custom_yticks=[0, 2, 4])


class TestTickFormatter:
    def test_scatter_formatter(self):
        tpl.scatter([{'x': [1, 2, 3], 'y': [4, 5, 6]}], width=20, height=10,
                    tick_formatter=lambda v: f"${v:.0f}")

    def test_line_formatter(self):
        tpl.line([{'x': [0, 1, 2], 'y': [0, 1, 4]}], width=20, height=10,
                 tick_formatter=lambda v: f"{v:.2f}")


class TestRadar:
    def test_basic_radar(self):
        tpl.radar(["A", "B", "C", "D"], [5, 8, 3, 6], width=30)

    def test_radar_with_title(self):
        tpl.radar(["A", "B", "C"], [5, 8, 3], width=30, title="Radar")

    def test_radar_with_color(self):
        tpl.radar(["A", "B", "C"], [5, 8, 3], width=30, color="red")

    def test_radar_with_fill(self):
        tpl.radar(["A", "B", "C"], [5, 8, 3], width=30, fill=True, color="cyan")

    def test_radar_few_categories(self):
        tpl.radar(["A", "B"], [5, 8], width=30)

    def test_radar_empty(self):
        tpl.radar([], [], width=30)

    def test_radar_output_file(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            path = f.name
        try:
            tpl.radar(["A", "B", "C"], [5, 8, 3], width=30, color="green", output_file=path)
            content = _read_file(path)
            assert not _has_ansi(content)
        finally:
            os.unlink(path)


class TestWaterfall:
    def test_basic_waterfall(self):
        tpl.waterfall(["Start", "+Rev", "-Cost", "End"], [100, 50, -30, 120], width=60)

    def test_waterfall_with_title(self):
        tpl.waterfall(["A", "B", "C"], [10, 20, -5], width=60, title="Waterfall")

    def test_waterfall_empty(self):
        tpl.waterfall([], [], width=60)

    def test_waterfall_output_file(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            path = f.name
        try:
            tpl.waterfall(["A", "B", "C"], [10, -5, 15], width=60, output_file=path)
            content = _read_file(path)
            assert not _has_ansi(content)
        finally:
            os.unlink(path)


class TestGantt:
    def test_basic_gantt(self):
        tasks = [
            {'label': 'Research', 'start': 0, 'end': 5},
            {'label': 'Design', 'start': 3, 'end': 8},
            {'label': 'Implement', 'start': 6, 'end': 12},
        ]
        tpl.gantt(tasks, width=60)

    def test_gantt_with_title(self):
        tasks = [
            {'label': 'Task A', 'start': 0, 'end': 5},
            {'label': 'Task B', 'start': 2, 'end': 8},
        ]
        tpl.gantt(tasks, width=60, title="Project")

    def test_gantt_empty(self):
        tpl.gantt([], width=60)

    def test_gantt_output_file(self):
        tasks = [
            {'label': 'A', 'start': 0, 'end': 5},
            {'label': 'B', 'start': 3, 'end': 10},
        ]
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            path = f.name
        try:
            tpl.gantt(tasks, width=60, output_file=path)
            content = _read_file(path)
            assert not _has_ansi(content)
        finally:
            os.unlink(path)


class TestStep:
    def test_basic_step(self):
        tpl.step([{'x': [0, 1, 2, 3], 'y': [0, 1, 1, 4]}], width=30, height=10)

    def test_step_with_title(self):
        tpl.step([{'x': [0, 1, 2], 'y': [0, 3, 1]}], width=30, height=10, title="Step")

    def test_step_multi_series(self):
        tpl.step([
            {'x': [0, 1, 2], 'y': [0, 2, 4], 'color': 'red', 'label': 'Fast'},
            {'x': [0, 1, 2], 'y': [0, 1, 2], 'color': 'blue', 'label': 'Slow'},
        ], width=30, height=10, legend=True)

    def test_step_empty(self):
        tpl.step([], width=30, height=10)

    def test_step_output_file(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            path = f.name
        try:
            tpl.step([{'x': [0, 1, 2], 'y': [0, 2, 4]}], width=30, height=10, output_file=path)
            content = _read_file(path)
            assert not _has_ansi(content)
        finally:
            os.unlink(path)


class TestBubble:
    def test_basic_bubble(self):
        tpl.bubble([{'x': [1, 2, 3], 'y': [4, 5, 6], 'size': [2, 5, 8]}], width=30, height=12)

    def test_bubble_with_title(self):
        tpl.bubble([{'x': [1, 2, 3], 'y': [4, 5, 6], 'size': [2, 5, 8]}],
                   width=30, height=12, title="Bubble")

    def test_bubble_multi_series(self):
        tpl.bubble([
            {'x': [1, 2], 'y': [3, 4], 'size': [2, 6], 'color': 'red', 'label': 'A'},
            {'x': [3, 4], 'y': [5, 6], 'size': [4, 8], 'color': 'blue', 'label': 'B'},
        ], width=30, height=12, legend=True)

    def test_bubble_empty(self):
        tpl.bubble([], width=30, height=12)

    def test_bubble_output_file(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            path = f.name
        try:
            tpl.bubble([{'x': [1, 2], 'y': [4, 5], 'size': [3, 7]}],
                       width=30, height=12, output_file=path)
            content = _read_file(path)
            assert not _has_ansi(content)
        finally:
            os.unlink(path)


class TestStrip:
    def test_basic_strip(self):
        tpl.strip([1, 2, 2, 3, 3, 3, 4, 5, 5, 6], width=30)

    def test_strip_with_title(self):
        tpl.strip([1, 2, 3, 4, 5], width=30, title="Distribution")

    def test_strip_with_color(self):
        tpl.strip([1, 2, 3], width=30, color="red")

    def test_strip_empty(self):
        tpl.strip([], width=30)

    def test_strip_output_file(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            path = f.name
        try:
            tpl.strip([1, 2, 3, 4, 5], width=30, color="blue", output_file=path)
            content = _read_file(path)
            assert not _has_ansi(content)
        finally:
            os.unlink(path)


class TestEdgeCases:
    def test_all_charts_render(self):
        """Smoke test - all chart types render without crashing"""
        tpl.bar(["A"], [1], max_width=20)
        tpl.scatter([{'x': [1], 'y': [1]}], width=10, height=5)
        tpl.line([{'x': [0, 1], 'y': [0, 1]}], width=10, height=5)
        tpl.pie(["A"], [100])
        tpl.hist([1, 2, 3], width=20)
        tpl.grouped_bar(["A"], [[1], [2]], max_width=20)
        tpl.stacked_bar(["A"], [[1], [2]], max_width=20)
        tpl.area([{'x': [0, 1], 'y': [0, 1]}], width=10, height=5)
        tpl.boxplot([[1, 2, 3]], width=20, height=10)
        tpl.heatmap([[1]], width=20)
        tpl.vertical_bar(["A"], [5], height=10, width=20)
        tpl.diverging_bar(["A"], [5], max_width=20)
        tpl.sparkline([1, 2, 3])
        tpl.violinplot([[1, 2, 3]], width=20, height=10)
        tpl.calendar_heatmap({"2026-01-01": 1})
        tpl.radar(["A", "B", "C"], [5, 8, 3], width=20)
        tpl.waterfall(["A", "B", "C"], [10, 20, -5], width=40)
        tpl.gantt([{'label': 'A', 'start': 0, 'end': 5}], width=40)
        tpl.step([{'x': [0, 1, 2], 'y': [0, 1, 4]}], width=20, height=8)
        tpl.bubble([{'x': [1, 2], 'y': [3, 4], 'size': [2, 6]}], width=20, height=8)
        tpl.strip([1, 2, 3, 4, 5], width=20)

    def test_boxplot_identical_values(self):
        tpl.boxplot([[5, 5, 5, 5], [3, 3, 3]], width=20, height=10)

    def test_hist_single_value(self):
        tpl.hist([1, 1, 1, 1], bins=3, width=40)
