from . import Node


class NodeGet(Node.Node):
    def __init__(self, attribute_name: str = '', var_name: str = '', line: int = 0, column: int = 0):
        super().__init__()
        self.var_name = var_name
        self.attribute_name = attribute_name
        self.line = line
        self.column = column
