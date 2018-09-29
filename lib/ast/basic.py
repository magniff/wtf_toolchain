import watch
from watch.builtins import InstanceOf, Container


class BaseASTNode(watch.WatchMe):
    def to_bf_code(self):
        raise NotImplementedError()


class SimpleInstruction(BaseASTNode):
    repeat = InstanceOf(int)

    def __eq__(self, other):
        return type(self) == type(other) and self.repeat == other.repeat

    def to_bf_code(self):
        return self.bf_instruction * self.repeat

    def __init__(self, repeat):
        self.repeat = repeat


class Inc(SimpleInstruction):
    bf_instruction = '+'


class Dec(SimpleInstruction):
    bf_instruction = '-'


class Right(SimpleInstruction):
    bf_instruction = '>'


class Left(SimpleInstruction):
    bf_instruction = '<'


class Input(SimpleInstruction):
    bf_instruction = ','


class Output(SimpleInstruction):
    bf_instruction = '.'


class Loop(BaseASTNode):
    contains = Container(InstanceOf(BaseASTNode))

    def __eq__(self, other):
        return type(self) == type(other) and self.contains == other.contains

    def to_bf_code(self):
        return '[%s]' % ''.join(node.to_bf_code() for node in self.contains)

    def __init__(self, contains):
        self.contains = contains


class Program(Loop):
    def to_bf_code(self):
        return ''.join(node.to_bf_code() for node in self.contains)

