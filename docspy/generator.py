import abc
from typing import List
from docspy.definitions import Definition


class Generator(abc.ABC):
    @abc.abstractmethod
    def generate(self, definitions: List[Definition]) -> str:
        pass
