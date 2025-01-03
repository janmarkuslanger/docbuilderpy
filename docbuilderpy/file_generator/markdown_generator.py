import ast
from docbuilderpy.file_generator import FileGenerator
from docbuilderpy.file_result import FileResult


class MarkdownGenerator(FileGenerator):
    def generate(self) -> FileResult:
        content = "# Documentation\n\n"

        no_result = "No documentation provided."

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
                            doctring = ast.get_docstring(method) or "No documentation provided."
                            content += f"- `{method.name}`: {docstring}\n"
                        content += "\n"

        else:
            content += "No definitions provided.\n"

        return FileResult(path=self.output_path, content=content)
