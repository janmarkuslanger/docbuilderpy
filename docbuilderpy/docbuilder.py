from typing import Type
from docbuilderpy.project_reader import ProjectReader
from docbuilderpy.structure_generator import StructureGenerator
from docbuilderpy.file_generator import FileGenerator

class DocBuilder:
    def __init__(
            self, 
            project_reader: Type[ProjectReader], 
            structure_generator: Type[StructureGenerator], 
            file_generator: Type[FileGenerator]
        ) -> None:
        self.project_reader = project_reader
        self.structure_generator = structure_generator
        self.file_generator = file_generator

    def generate(self) -> None:
        path = 'docbuilderpy'
        output_path = 'output.md'

        project_reader_instance = self.project_reader(path=path)
        analyzed_files = project_reader_instance.read()
        
        structured_analyzed_files = self.structure_generator(
            output_path=output_path, analyzed_files=analyzed_files
        ).generate()

    
        for file_result in structured_analyzed_files:
            file_generator_instance = self.file_generator(
                definitions=file_result.items, output_path=file_result.path
            )
            file_result = file_generator_instance.generate()

            with open(file_result.path, 'w') as file:
                file.write(file_result.content)



    
