from . import Node


class NodeElseBlock(Node.Node):
    def __init__(self, line: int = 0, column: int = 0):
        super().__init__()
        self.line = line
        self.column = column
