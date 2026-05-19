from typing import Any, Callable, List, Optional

from termatplotlib.utils import write_output


class Figure:
    def __init__(self, title: Optional[str] = None):
        self.title = title
        self._charts: List[tuple] = []

    def add_chart(self, func: Callable, *args: Any, **kwargs: Any) -> 'Figure':
        self._charts.append((func, args, kwargs))
        return self

    def render(self, output_file: Optional[str] = None) -> None:
        all_lines: List[str] = []
        if self.title:
            all_lines.append(f"\n{'=' * 60}")
            all_lines.append(f"{self.title.center(60)}")
            all_lines.append(f"{'=' * 60}\n")
        for func, args, kwargs in self._charts:
            kwargs.pop('output_file', None)
            kwargs['_return_output'] = True
            lines = func(*args, **kwargs, output_file=None)
            if isinstance(lines, str):
                lines = lines.rstrip('\n').split('\n')
            elif isinstance(lines, list):
                lines = list(lines)
            else:
                lines = []
            all_lines.extend(lines)
        write_output(all_lines, output_file)

    def savefig(self, path: str) -> None:
        self.render(output_file=path)
