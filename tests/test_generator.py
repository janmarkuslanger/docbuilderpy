from typing import List
from docspy.generator import Generator
from docspy.definitions import Definition


class TestGenerator(Generator):
    def generate(self, definitions: List[Definition]) -> str:
        return "test"


def test_generator():
    generator = TestGenerator()
    definitions = []
    result = generator.generate(definitions)
    assert result == "test"
