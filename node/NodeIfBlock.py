from . import Node


class NodeIfBlock(Node.Node):
    def __init__(self, condition = None, line: int = 0, column: int = 0):
        super().__init__()
        self.condition = condition
        self.line = line
        self.column = column