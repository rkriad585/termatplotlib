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

    def test_boxplot_identical_values(self):
        tpl.boxplot([[5, 5, 5, 5], [3, 3, 3]], width=20, height=10)

    def test_hist_single_value(self):
        tpl.hist([1, 1, 1, 1], bins=3, width=40)
