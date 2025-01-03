from typing import Type
from docbuilderpy.project_reader import ProjectReader
from docbuilderpy.structure_generator import StructureGenerator
from docbuilderpy.file_generator import FileGenerator


class DocBuilder:
    def __init__(
        self,
        path: str,
        output_path: str,
        project_reader: Type[ProjectReader],
        structure_generator: Type[StructureGenerator],
        file_generator: Type[FileGenerator],
    ) -> None:
        self.path = path
        self.output_path = output_path
        self.project_reader = project_reader
        self.structure_generator = structure_generator
        self.file_generator = file_generator

    def generate(self) -> None:
        project_reader_instance = self.project_reader(path=self.path)
        analyzed_files = project_reader_instance.read()

        structured_analyzed_files = self.structure_generator(
            output_path=self.output_path, analyzed_files=analyzed_files
        ).generate()

        for file_result in structured_analyzed_files:
            file_generator_instance = self.file_generator(
                output_path=file_result.path, definitions=file_result.items
            )
            final_file = file_generator_instance.generate()

            with open(final_file.path, "w") as file:
                file.write(final_file.content)
