import watch
from . basic import BaseASTNode


class Drop(BaseASTNode):
    pass


class Add(BaseASTNode):
    shift = watch.builtins.InstanceOf(int)

    def __init__(self, shift):
        self.shift = shift

