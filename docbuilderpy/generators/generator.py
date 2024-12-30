import abc
from typing import List, Union
from docbuilderpy.definitions import FunctionDefinition, ClassDefinition


class Generator(abc.ABC):
    @abc.abstractmethod
    def generate(self, source_path: str, output_path: str) -> None:
        pass

    @abc.abstractmethod
    def generate_file(
        self, definitions: List[Union[FunctionDefinition, ClassDefinition]]
    ) -> str:
        pass

    @abc.abstractmethod
    def get_file_format(self) -> str:
        pass
