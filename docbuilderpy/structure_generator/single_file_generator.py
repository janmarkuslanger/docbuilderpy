from typing import List
from docbuilderpy.structure_generator import StructureGenerator
from docbuilderpy.analyzed_result import AnalyzedResult


class SingleFileGenerator(StructureGenerator):
    def __init__(
        self,
        output_path: None | str = None,
        analyzed_files: List[AnalyzedResult] = None,
    ) -> None:
        super().__init__(output_path, analyzed_files)

    def generate(self) -> List[AnalyzedResult]:
        return [
            AnalyzedResult(
                path=self.output_path,
                items=[
                    item
                    for file_result in self.analyzed_files
                    for item in file_result.items
                ],
            )
        ]
