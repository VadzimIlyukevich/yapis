from . import Node


class NodeAssigment(Node.Node):
    def __init__(self, var_name: str = '', new_flag: bool = True, line: int = 0, column: int = 0):
        super().__init__()
        self.var_name = var_name
        self.line = line
        self.column = column
        self.new_flag = new_flag
