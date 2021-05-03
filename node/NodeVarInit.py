from . import Node


class NodeVarInit(Node.Node):
    def __init__(self, var_name: str = '', var_type: str = '', new_flag: bool = True, line: int = 0, column: int = 0):
        super().__init__()
        self.var_name = var_name
        self.var_type = var_type
        self.new_flag = new_flag
        self.line = line
        self.column = column

