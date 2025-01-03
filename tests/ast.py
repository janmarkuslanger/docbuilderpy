import ast
from docbuilderpy.analyzed_result import AnalyzedResult

# Class: MyClass
class_def = ast.ClassDef(
    name="MyClass",
    bases=[],
    keywords=[],
    body=[
        ast.FunctionDef(
            name="greet",
            args=ast.arguments(
                posonlyargs=[],
                args=[ast.arg(arg="self")],
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[],
            ),
            body=[ast.Return(value=ast.Constant(value="Hello from MyClass!"))],
            decorator_list=[],
            returns=ast.Name(id="str", ctx=ast.Load()),
        )
    ],
    decorator_list=[],
)

# Function: my_function
function_def = ast.FunctionDef(
    name="my_function",
    args=ast.arguments(
        posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]
    ),
    body=[
        ast.Expr(
            value=ast.Call(
                func=ast.Name(id="print", ctx=ast.Load()),
                args=[ast.Constant(value="Hello from my_function!")],
                keywords=[],
            )
        )
    ],
    decorator_list=[],
    returns=None,
)

# Assignment: x = 42
assignment = ast.Assign(
    targets=[ast.Name(id="x", ctx=ast.Store())], value=ast.Constant(value=42)
)

# Expression: print("Just a statement")
expression = ast.Expr(
    value=ast.Call(
        func=ast.Name(id="print", ctx=ast.Load()),
        args=[ast.Constant(value="Just a statement")],
        keywords=[],
    )
)

stmt_list_filtered = [
    AnalyzedResult(path="much.py", items=[class_def, function_def]),
    AnalyzedResult(path="wow.py", items=[class_def, function_def]),
]

stmt_list = stmt_list_filtered + [
    AnalyzedResult(path="wow.py", items=[assignment, expression])
]
