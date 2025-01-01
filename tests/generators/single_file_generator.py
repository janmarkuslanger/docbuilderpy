from docbuilderpy.generators.single_file_generator import SingleFileGenerator
from tests.utility import setup_test_environment


class TestGenerator(SingleFileGenerator):
    def generate_file(self, definitions):
        return "my_output"

    def get_file_format(self):
        return "html"


def test_generate(tmp_path):
    setup_test_environment(tmp_path)
    generator = TestGenerator()

    tmp_path_str = str(tmp_path)

    generator.generate(tmp_path_str, tmp_path_str + "/my_output")
    output_file = tmp_path / "my_output.html"
    assert output_file.read_text() == "my_output"
