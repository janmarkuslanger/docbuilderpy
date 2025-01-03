import ast
from typing import NamedTuple, List


class AnalyzedResult(NamedTuple):
    path: str
    items: List[ast.stmt]
