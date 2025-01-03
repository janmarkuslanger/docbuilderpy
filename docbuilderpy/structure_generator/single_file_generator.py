from typing import List
from docbuilderpy.structure_generator import StructureGenerator
from docbuilderpy.analyzed_result import AnalyzedResult


class SingleFileGenerator(StructureGenerator):
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
