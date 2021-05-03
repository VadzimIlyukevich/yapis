from . import Node


class NodeForStatement(Node.Node):
    def __init__(self, range_statement=None, line: int = 0, column: int = 0):
        super().__init__()
        self.local_vars = {}
        self.range_statement = range_statement
        self.line = line
        self.column = column
