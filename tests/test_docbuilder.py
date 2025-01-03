import pytest
from docbuilderpy import DocBuilder


def test_docbuilder():
    with pytest.raises(TypeError):
        docbuilder = DocBuilder()
