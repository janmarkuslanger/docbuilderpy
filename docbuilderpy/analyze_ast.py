import ast
from typing import List


def analyze_ast(code: str) -> List[ast.stmt]:
    ast_nodes = []

    tree = ast.parse(code)

    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            ast_nodes.append(node)

        if isinstance(node, ast.ClassDef):
            ast_nodes.append(node)

    return ast_nodes
