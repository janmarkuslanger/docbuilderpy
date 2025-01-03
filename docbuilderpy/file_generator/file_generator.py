import abc
import ast
from typing import List
from docbuilderpy.file_result import FileResult


class FileGenerator(abc.ABC):
    def __init__(
        self,
        definitions: List[ast.stmt] | None = None,
        output_path: None | str = None,
        format: None | str = None,
    ) -> None:
        self.definitions = definitions
        self.output_path = output_path
        self.format = format

    @abc.abstractmethod
    def generate(self) -> FileResult:
        pass
