from . import Node


class NodeGetArrayElement(Node.Node):
    def __init__(self, var_name: str = '', index: int = 0, line: int = 0, column: int = 0):
        super().__init__()
        self.var_name = var_name
        self.index = index
        self.line = line
        self.column = column
