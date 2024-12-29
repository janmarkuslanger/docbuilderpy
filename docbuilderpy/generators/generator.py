import abc
from typing import List
from docbuilderpy.definitions import Definition


class Generator(abc.ABC):
    @abc.abstractmethod
    def generate_file(self) -> str:
        pass

    @abc.abstractmethod
    def generate_file(self, definitions: List[Definition]):
        pass

    def get_file_format(self) -> str:
        pass
