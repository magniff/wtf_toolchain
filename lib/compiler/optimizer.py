import sys
from lib.ast import Drop, Dec, Inc, LoopNode


optimizers = sys.modules[__name__]


def optimize(node):
    optimizer = getattr(
        optimizers, 'optimize_%s' % type(node).__qualname__,
        lambda node: node
    )
    return optimizer(node)


def optimize_LoopNode(node):
    if len(node.contains) == 1 and isinstance(node.contains[0], (Inc, Dec)):
        return Drop()
    else:
        return LoopNode(
            contains=[optimize(subnode) for subnode in node.contains]
        )


def optimize_ProgramNode(node):
    node.contains = list(map(optimize, node.contains))
    return node
