import sys
from collections.abc import Iterable
from itertools import chain
import struct

from lib.ast import LoopNode
from . import opcodes

visitors = sys.modules[__name__]


SETUP_LOOP = 0
END_LOOP = 1
INC = 2
DEC = 3
RSHIFT = 4
LSHIFT = 5
WRITE = 6
READ = 7
DROP = 8
TERMINATE = 255


def visit(node):
    yield from bytes(
        getattr(visitors, "visit_%s" % type(node).__qualname__)(node)
    )


def visit_Drop(node):
    yield opcodes.DROP


def visit_Inc(node):
    yield opcodes.INC
    yield from struct.pack('>h', node.repeat)


def visit_Dec(node):
    yield opcodes.DEC
    yield from struct.pack('>h', node.repeat)


def visit_Left(node):
    yield opcodes.LSHIFT
    yield from struct.pack('>h', node.repeat)


def visit_Input(node):
    yield opcodes.READ


def visit_Output(node):
    yield opcodes.WRITE


def visit_Right(node):
    yield opcodes.RSHIFT
    yield from struct.pack('>h', node.repeat)


def visit_LoopNode(node):
    all_insides = tuple(chain(*(visit(subnode) for subnode in node.contains)))
    yield opcodes.SETUP_LOOP
    yield from struct.pack('>h', len(all_insides))
    yield from all_insides
    yield opcodes.END_LOOP
    yield from struct.pack('>h', len(all_insides))


def visit_ProgramNode(node):
    for subnode in node.contains:
        yield from visit(subnode)
    yield opcodes.TERMINATE

