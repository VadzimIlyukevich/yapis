from antlr4 import *
from generated import EasyXMLVisitor, EasyXMLLexer, EasyXMLParser
from node.Node import Node
from visitor.visitor import MyVisitor


def main(xml_program: str) -> None:
    input_stream = FileStream('xml_program.el')
    lexer = EasyXMLLexer.EasyXMLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = EasyXMLParser.EasyXMLParser(stream)
    tree = parser.xml()
    if parser.getNumberOfSyntaxErrors():
        exit(1)
    visitor = MyVisitor()
    visitor.visit(tree)
    print(1)


if __name__ == '__main__':
    # if len(sys.argv) > 1:
    #     main(sys.argv[1])
    main('')
