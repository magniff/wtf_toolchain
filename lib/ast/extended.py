from watch.builtins import InstanceOf
from . basic import BaseASTNode


class Drop(BaseASTNode):
    pass


class Add(BaseASTNode):
    shift = InstanceOf(int)

    def __init__(self, shift):
        self.shift = shift

