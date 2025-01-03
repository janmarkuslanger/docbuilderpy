from docbuilderpy.structure_generator import SingleFileGenerator
from tests.utility import setup_test_environment
from tests.ast import stmt_list_filtered


def test_single_file_generator(tmp_path):
    setup_test_environment(tmp_path)
    single_file_generator = SingleFileGenerator(
        output_path=tmp_path / "output", analyzed_files=stmt_list_filtered
    )

    assert single_file_generator is not None

    file_results = single_file_generator.generate()

    assert len(file_results) == 1
    assert file_results[0].path == tmp_path / "output"

    print("WOW", file_results[0].items)

    assert len(file_results[0].items) == 4
