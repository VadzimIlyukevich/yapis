from . import Node


class NodeFuncInit(Node.Node):
    def __init__(self, var_type: str = '', var_name: str = '', params=None, line: int = 0, column: int = 0):
        super().__init__()
        self.local_vars = {}
        self.var_type = var_type
        self.var_name = var_name
        self.params = params
        self.return_statement = None
        self.line = line
        self.column = column
