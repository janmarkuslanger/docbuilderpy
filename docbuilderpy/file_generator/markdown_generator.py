import ast
from typing import List
from docbuilderpy.file_generator import FileGenerator
from docbuilderpy.file_result import FileResult


class MarkdownGenerator(FileGenerator):
    def __init__(
        self,
        definitions: List[ast.stmt] | None = None,
        output_path: None | str = None,
        format: None | str = None,
    ) -> None:
        super().__init__(definitions, output_path, format)

    def generate(self) -> FileResult:
        content = "# Documentation\n\n"

        if self.definitions:
            content += "## Definitions\n\n"

            for node in self.definitions:
                if isinstance(node, ast.FunctionDef):
                    content += f"### Function: `{node.name}`\n\n"
                    docstring = ast.get_docstring(node) or "No documentation provided."
                    content += f"{docstring}\n\n"
                elif isinstance(node, ast.ClassDef):
                    content += f"### Class: `{node.name}`\n\n"
                    docstring = ast.get_docstring(node) or "No documentation provided."
                    content += f"{docstring}\n\n"

                    methods = [n for n in node.body if isinstance(n, ast.FunctionDef)]
                    if methods:
                        content += "#### Methods:\n\n"
                        for method in methods:
                            content += f"- `{method.name}`: {ast.get_docstring(method) or 'No documentation provided.'}\n"
                        content += "\n"

        else:
            content += "No definitions provided.\n"

        return FileResult(path=self.output_path, content=content)
