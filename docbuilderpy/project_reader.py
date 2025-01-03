import os
from typing import List
from docbuilderpy.load_file import load_file
from docbuilderpy.analyzed_result import AnalyzedResult
from docbuilderpy.analyze_ast import analyze_ast


class ProjectReader:
    def __init__(self, path: str) -> None:
        self.path = path

    def skip_file(self, file: str) -> bool:
        if not file.endswith(".py"):
            return True

        if file.endswith("__init__.py"):
            return True

        return False

    def read(self) -> List[AnalyzedResult]:
        file_results = []

        for root, _, files in os.walk(self.path):
            for file in files:
                if self.skip_file(file):
                    continue

                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, self.path)

                file_content = load_file(file_path)
                ast_tree = analyze_ast(file_content)

                file_result = AnalyzedResult(path=relative_path, items=ast_tree)
                file_results.append(file_result)

        return file_results
