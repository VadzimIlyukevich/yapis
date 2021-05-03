from . import Node


class NodeFuncCall(Node.Node):
    def __init__(self, func_name: str = '', line: int = 0, column: int = 0):
        super().__init__()
        self.var_name = func_name
        self.line = line
        self.column = column