from docbuilderpy.generators.generator import Generator


def generate(source_path: str, output_path: str, generator: Generator) -> None:
    generator.generate(source_path, output_path)