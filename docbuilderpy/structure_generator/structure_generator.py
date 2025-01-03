import abc
from typing import List
from docbuilderpy.analyzed_result import AnalyzedResult


class StructureGenerator(abc.ABC):
    def __init__(
        self,
        output_path: str,
        analyzed_files: List[AnalyzedResult],
    ) -> None:
        self.output_path = output_path
        self.analyzed_files = analyzed_files

    @abc.abstractmethod
    def generate(self) -> List[AnalyzedResult]:
        pass
