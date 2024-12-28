import os
from docpy.analyze_definitions import analyze_definitions
from docpy.load_file import load_file
from docpy.generator import Generator


def generate(path: str, output: str, generator: Generator):
    definitions = []
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                code = load_file(file_path)
                definitions.extend(analyze_definitions(code, file_path))

    content = generator.generate(definitions)
    with open(output, "w") as file:
        file.write(content)
