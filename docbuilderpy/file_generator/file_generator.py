import abc
import ast
from typing import List
from docbuilderpy.file_result import FileResult


class FileGenerator(abc.ABC):
    def __init__(
        self,
        output_path: str,
        definitions: List[ast.stmt],
    ) -> None:
        self.output_path = output_path
        self.definitions = definitions
        self.format = format

    @abc.abstractmethod
    def generate(self) -> FileResult:
        pass
