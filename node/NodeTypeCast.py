from . import Node


class NodeTypeCast(Node.Node):
    def __init__(self, var_name: str = '',cast_type: str = '', line: int = 0, column: int = 0):
        self.var_name = var_name
        self.cast_type = cast_type
        self.line = line
        self.column = column
