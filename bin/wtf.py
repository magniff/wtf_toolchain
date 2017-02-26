import sys
from lib import interprete


def main():
    with open(sys.argv[1]) as src_file:
        interprete(src_file.read())

