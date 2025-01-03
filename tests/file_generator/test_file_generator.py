import pytest
from docbuilderpy.file_generator import FileGenerator


class CorrectImplementedFileGenerator(FileGenerator):
    def generate(self):
        return []


def test_generator():
    with pytest.raises(TypeError):
        FileGenerator()


def test_correct_implemented_generator():
    generator = CorrectImplementedFileGenerator([], "output_path")
    assert generator is not None
