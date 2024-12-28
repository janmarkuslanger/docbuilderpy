import abc
from typing import List
from docpy.definitions import Definition


class Generator(abc.ABC):
    @abc.abstractmethod
    def generate(self, definitions: List[Definition]) -> str:
        pass
