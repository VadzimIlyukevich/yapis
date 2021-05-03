from . import Node


class NodeCondition(Node.Node):
    def __init__(self, is_not: bool = False, and_or: str = '', line: int = 0, column: int = 0):
        super().__init__()
        self.is_not = is_not
        self.and_or = and_or
        self.column = column
        self.line = line