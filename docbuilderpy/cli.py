from docbuilderpy import DocBuilder, ProjectReader, SingleFileGenerator
from docbuilderpy.file_generator import MarkdownGenerator


def main():
    t = DocBuilder(ProjectReader, SingleFileGenerator, MarkdownGenerator)
    t.generate()

if __name__ == "__main__":
    main()