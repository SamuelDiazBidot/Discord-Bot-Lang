from lexerParser import make_parser

inputFile = open('input.bot', 'r')
parser = make_parser()

parser.parse(inputFile.read())