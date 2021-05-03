from . import Node


class NodeWhileStatement(Node.Node):
    def __init__(self, condition=None, line: int = 0, column: int = 0):
        super().__init__()
        self.local_vars = {}
        self.condition = condition
        self.line = line
        self.column = column
