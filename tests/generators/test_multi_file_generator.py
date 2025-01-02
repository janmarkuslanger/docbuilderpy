from docbuilderpy.generators.multi_file_generator import MultiFileGenerator
from tests.utility import setup_test_environment


class TestGenerator(MultiFileGenerator):
    def generate_file(self):
        return "my_output"

    def get_file_format(self):
        return "html"


def test_generate(tmp_path):
    setup_test_environment(tmp_path)
    tmp_path_str = str(tmp_path)

    generator = TestGenerator()
    generator.source_path = str(tmp_path)
    generator.file_format = "html"

    generator.output_path = tmp_path_str + "/my_output"
    generator.generate()

    base_path = tmp_path / "my_output" / "my_lib"

    assert (base_path / "test_class.html").exists()
    assert (base_path / "utility/is_test.html").exists()
