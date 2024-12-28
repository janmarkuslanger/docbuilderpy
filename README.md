
# Docspy

**Docspy** is a tool for easily generating documentation for Python projects. It provides default functionality for generating documentation in Markdown format and allows users to include custom generators.

## 🚀 Installation

To install **Docspy**, run the following command:

```bash
pip install docspy
```

## 📖 Usage

Once installed, you can use the `docspy` command in the terminal. The basic syntax is:

```bash
docspy PATH [OPTIONS]
```

### Options

- **`path`** *(required)*: The path to the Python project or directory to analyze.
- **`--output`, `-o`** *(optional)*: The path where the generated documentation will be saved. Default: `docs`.
- **`--format`, `-f`** *(optional)*: The output format of the documentation. Currently supported: `markdown` (default).
- **`--custom_generator`, `-cg`** *(optional)*: Path to a Python file containing a custom generator class.

### Examples

#### Generate standard documentation

Create documentation in Markdown format and save it to the default output path `docs`:

```bash
docspy ./my_project
```

#### Save documentation to a custom path

Create documentation and save it to a custom directory:

```bash
docspy ./my_project --output ./custom_docs
```

#### Use a custom generator

Use a custom generator class from the file `custom_generator.py`:

```bash
docspy ./my_project --custom_generator ./custom_generator.py
```

## 🔧 Creating Custom Generators

If you want to extend the default functionality, you can create your own generator classes. The custom class must inherit from the abstract class `Generator` and implement the `generate()` method.

### Example: Custom Generator Class

Create a file `custom_generator.py` with the following content:

```python
from docspy.generate import Generator
from typing import List
from docspy.definitions import Definition

class CustomGenerator(Generator):
    def generate(self, definitions: List[Definition]) -> str:
        return "This is a custom generator!"
```

Then, use this class with the `--custom_generator` option:

```bash
docspy ./my_project --custom_generator ./custom_generator.py
```

## 🤝 Contributing

Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

Enjoy using **Docspy**! If you have questions or issues, feel free to open an issue on GitHub.
