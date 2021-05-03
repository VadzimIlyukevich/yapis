from antlr4 import *
from generated import EasyXMLVisitor, EasyXMLLexer, EasyXMLParser
from node.Node import Node


def main(xml_program: str) -> None:
    input_stream = FileStream('xml_program.el')
    lexer = EasyXMLLexer.EasyXMLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = EasyXMLParser.EasyXMLParser(stream)
    tree = parser.xml()
