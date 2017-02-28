import sys
from lib.ast import Drop, Dec, Inc, Loop, Left, Right, Add, Program


optimizers = sys.modules[__name__]


class PlaceHolder(int):
    def __init__(self):
        self.value = None

    def __eq__(self, other):
        self.value = other
        return True


def optimize_add_forward(loop_node):
    ph_0 = PlaceHolder()
    ph_1 = PlaceHolder()
    pattern = [Dec(1), Right(ph_0), Inc(1), Left(ph_1)]
    if pattern == loop_node.contains and ph_0.value == ph_1.value:
        return Add(shift=ph_0.value)


def optimize_add_reverse(loop_node):
    ph_0 = PlaceHolder()
    ph_1 = PlaceHolder()
    pattern = [Dec(1), Left(ph_0), Inc(1), Right(ph_1)]
    if pattern == loop_node.contains and ph_0.value == ph_1.value:
        return Add(shift=-ph_0.value)


def optimize_add(node):
    return optimize_add_forward(node) or optimize_add_reverse(node)


def optimize_drop(loop_node):
    pattern = [Dec(1),]
    if pattern == loop_node.contains:
        return Drop()


OPTIMIZATIONS = [
    optimize_add, optimize_drop,
]


def optimize(node):
    if not isinstance(node, Loop):
        return node
    if isinstance(node, Program):
        return Program(
            contains=[optimize(subnode) for subnode in node.contains]
        )
    else:
        for optimization in OPTIMIZATIONS:
            result = optimization(node)
            if result:
                return result
        return Loop(
            contains=[optimize(subnode) for subnode in node.contains]
        )

