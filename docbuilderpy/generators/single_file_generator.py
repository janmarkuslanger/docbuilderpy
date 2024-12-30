import abc
import os
from typing import List, Union, override
from docbuilderpy.generators.generator import Generator
from docbuilderpy.load_file import load_file
from docbuilderpy.analyze_definitions import analyze_definitions
from docbuilderpy.definitions import FunctionDefinition, ClassDefinition


class SingleFileGenerator(Generator, abc.ABC):
    @override
    def generate(self, source_path: str, output_path: str) -> None:
        definitions = []
        for root, _, files in os.walk(source_path):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    code = load_file(file_path)
                    definitions.extend(analyze_definitions(code, file_path))

        content = self.generate_file(definitions)
        output_file_path = output_path + "." + self.get_file_format()
        with open(output_file_path, "w") as output_file:
            output_file.write(content)

    @override
    @abc.abstractmethod
    def generate_file(
        self, definitions: List[Union[FunctionDefinition, ClassDefinition]]
    ) -> str:
        pass

    @override
    @abc.abstractmethod
    def get_file_format(self) -> str:
        pass
