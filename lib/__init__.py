from .compiler import p_program, build_token_generator
from .ast import Inc, Dec, Left, Right, Output, LoopNode


def interprete_worker(node, pc, dp, memory):
    if isinstance(node, Left):
        dp -= node.repeat
    elif isinstance(node, Right):
        dp += node.repeat
    elif isinstance(node, Output):
        for _ in range(node.repeat):
            print(chr(memory[dp]), end='')
    elif isinstance(node, LoopNode):
        while True:
            if memory[dp] == 0:
                return pc, dp
            for inner_node in node.contains:
                pc, dp = interprete_worker(inner_node, pc, dp, memory)
            if memory[dp] == 0:
                return pc, dp
    elif isinstance(node, Inc):
        memory[dp] += node.repeat
    elif isinstance(node, Dec):
        memory[dp] -= node.repeat

    return pc, dp


def interprete(code):
    program_counter = 0
    data_pointer = 0
    memory = [0] * 30000
    for node in p_program.parse(tuple(build_token_generator(code))).contains:
        program_counter, data_pointer = interprete_worker(
            node=node, pc=program_counter, dp=data_pointer, memory=memory
        )

