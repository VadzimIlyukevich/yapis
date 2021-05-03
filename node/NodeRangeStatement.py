from . import Node


class NodeRangeStatement(Node.Node):
    def __init__(self, var_type: str = '', iterator: str = '', collection: str = '', line: int = 0, column: int = 0):
        super().__init__()
        self.var_type = var_type
        self.iterator = iterator
        self.collection = collection
        self.line = line
        self.column = column
