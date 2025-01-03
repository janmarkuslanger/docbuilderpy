import ast
from typing import List
from docbuilderpy.file_generator import FileGenerator
from docbuilderpy.file_result import FileResult


class MarkdownGenerator(FileGenerator):
    def __init__(self, definitions: List[ast.stmt] | None = None,
            output_path: None | str = None,
            format: None | str = None) -> None:
        super().__init__(definitions, output_path, format)

    def generate(self) -> FileResult:
        return FileResult(
            path=self.output_path,
            content="# Documentation\n\n"
        )