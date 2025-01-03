# 🔧 docbuilderpy

`docbuilderpy` is a Python library designed to simplify the generation and management of documentation for Python projects. It analyzes project structures, parses source code, and generates customizable documentation files in various formats, including Markdown.

---

## ✨ Features

- 🧩 **AST Analysis**: Extract meaningful information from Python code using Abstract Syntax Tree (AST) parsing.
- 🕁️ **Documentation Generation**:
- 🏢 **Modular Design**: Create your own implementation

---

## 🔄 Installation

Install `docbuilderpy` using pip:

```bash
pip install docbuilderpy
```

Or, clone the repository and install locally:

```bash
git clone https://github.com/janmarkuslanger/docbuilderpy.git
cd docbuilderpy
pip install .
```

---

## 🔧 Usage

### Example: Generate Documentation for a Project

```python
from docbuilderpy import DocBuilder, ProjectReader, SingleFileGenerator
from docbuilderpy.file_generator import MarkdownGenerator

docs = DocBuilder(
    'docbuilderpy', # Path to the project 
    'output.md', # Output path can also be a dir if you want to create multiple files
    ProjectReader, # Class with a method reading the file 
    SingleFileGenerator, # Class which generates the project structure
    MarkdownGenerator # Class which generates the file 
)
docs.generate()
```

This will generate a Markdown file named `output.md` for the specified project directory.

---

## 📖 Docs

### StructureGenerator

If you want to create your own structure, you need to create a class that inherits from the `StructureGenerator`.
The class must implement the `generate` method. It can access `self.analyzed_files`, which is a list of `AnalyzedResult`
from the project reader class. `AnalyzedResult` is a NamedTuple of path and a list of AST nodes.
The method must also return a list of `AnalyzedResult`. For every item in the list, there should also be a file. The path will be the output. The AST nodes will also be passed.

For example, the SingleFileGenerator: 
In this case, every definition will be in one file. So we iterate through the files and put it into one list.

```python
class SingleFileGenerator(StructureGenerator):
    def generate(self) -> List[AnalyzedResult]:
        return [
            AnalyzedResult(
                path=self.output_path,
                items=[
                    item
                    for file_result in self.analyzed_files
                    for item in file_result.items
                ],
            )
        ]
```

### FileGenerator

If you want to create your own file, you need to create a class that inherits from the `FileGenerator`.
The class must implement the `generate` method. It can access `self.definitions`, which is a list of AST nodes `List[ast.stmt]`.
It must return a NamedTuple `FileResult`. It holds the final path and the content as a string.

```python
...

class MarkdownGenerator(FileGenerator):
    ...

    def generate(self) -> FileResult:
        content = "# Documentation\n\n"

        if self.definitions:
            content += "## Definitions\n\n"

            for node in self.definitions:
                content += f"### Function: `{node.name}`\n\n"
                

        return FileResult(path=self.output_path, content=content)
```

---

## 📚 Development

### Setting up the Development Environment

1. Clone the repository:
   ```bash
   git clone https://github.com/janmarkuslanger/docbuilderpy.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run tests to verify the setup:
   ```bash
   pytest
   ```

### Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch for your feature/bugfix.
3. Submit a pull request with a clear description of your changes.

---

## ⚖️ License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🌟 Acknowledgments

Thanks to all contributors who have supported this project. Your feedback and input are invaluable!

---

## 📢 Contact

For questions or support, reach out via [GitHub Issues](https://github.com/janmarkuslanger/docbuilderpy/issues).
