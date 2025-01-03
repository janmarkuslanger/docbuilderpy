from docbuilderpy import ProjectReader
from tests.utility import setup_test_environment


def test_projectreader():
    project_reader = ProjectReader("my_path")
    assert project_reader is not None
    assert project_reader.path == "my_path"


def test_projectreader_read_empty(tmp_path):
    project_reader = ProjectReader(tmp_path)
    assert project_reader.read() == []


def test_projectreader_read(tmp_path):
    setup_test_environment(tmp_path)
    project_reader = ProjectReader(tmp_path)

    files = project_reader.read()

    assert len(files) == 2
