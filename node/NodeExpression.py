from . import Node


class NodeExpression(Node.Node):
    def __init__(self, line: int = 0, column: int = 0):
        super().__init__()
        self.value = None
        self.left_expression = None
        self.right_expression = None
        self.opetor = None
        self.line = line
        self.column = column