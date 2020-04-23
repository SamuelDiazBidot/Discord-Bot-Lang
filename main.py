import argparse
from lexerParser import make_parser

argParser = argparse.ArgumentParser()
argParser.add_argument("file_path", help="Path of file to transpile")
args = argParser.parse_args()

inputFile = open(args.file_path, 'r')
parser = make_parser()
parser.parse(inputFile.read())