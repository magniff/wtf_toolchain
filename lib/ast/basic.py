import watch


class BaseASTNode(watch.WatchMe):
    def to_bf_code(self):
        raise NotImplementedError()


class SimpleInstructionNode(BaseASTNode):
    repeat = watch.builtins.InstanceOf(int)

    def to_bf_code(self):
        return self.bf_instruction * self.repeat

    def __init__(self, repeat):
        self.repeat = repeat


class Inc(SimpleInstructionNode):
    bf_instruction = '+'


class Dec(SimpleInstructionNode):
    bf_instruction = '-'


class Right(SimpleInstructionNode):
    bf_instruction = '>'


class Left(SimpleInstructionNode):
    bf_instruction = '<'


class Input(SimpleInstructionNode):
    bf_instruction = ','


class Output(SimpleInstructionNode):
    bf_instruction = '.'


class LoopNode(BaseASTNode):
    contains = watch.ArrayOf(watch.builtins.InstanceOf(BaseASTNode))

    def to_bf_code(self):
        return '[%s]' % ''.join(node.to_bf_code() for node in self.contains)

    def __init__(self, contains):
        self.contains = contains


class ProgramNode(LoopNode):
    def to_bf_code(self):
        return ''.join(node.to_bf_code() for node in self.contains)

