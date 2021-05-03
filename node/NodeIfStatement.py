from . import Node


class NodeIfStatement(Node.Node):
    def __init__(self, if_block=None, elif_block=None, else_block=None):
        super().__init__()
        self.if_block = if_block
        self.elif_block = elif_block
        self.else_block = else_block
