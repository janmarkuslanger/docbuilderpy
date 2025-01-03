import pytest
from docbuilderpy.structure_generator import StructureGenerator


class CorrectImplementedStructureGenerator(StructureGenerator):
    def generate(self):
        return []


def test_structure_generator():
    with pytest.raises(TypeError):
        structure_generator = StructureGenerator()


def test_correct_implemented_structure_generator():
    structure_generator = CorrectImplementedStructureGenerator()
    assert structure_generator is not None
