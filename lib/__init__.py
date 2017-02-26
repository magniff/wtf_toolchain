from collections import namedtuple


BF_INSTRUCTIONS = "+-[].,<>"


def parse(source):
    stack = list()
    jumps = dict()
    code = ''.join(filter(lambda value: value in BF_INSTRUCTIONS, source))

    for counter, instruction in enumerate(code):
        if instruction == '[':
            stack.append(counter)
        elif instruction == ']':
            loopback_address = stack.pop()
            jumps[counter] = loopback_address
            jumps[loopback_address] = counter + 1

    for counter, instruction in enumerate(code):
        yield (instruction, jumps.get(counter))


def interprete(code):
    memory = [0] * 30000
    current_cell = 0
    current_instruction = 0
    clean_code = tuple(parse(code))
    program_len = len(clean_code)
    while True:
        if current_instruction > program_len - 1:
            break
        instruction, link = clean_code[current_instruction]
        if instruction == '<':
            current_cell -= 1
        elif instruction == '>':
            current_cell += 1
        elif instruction == '.':
            print(chr(memory[current_cell]), end='')
        elif instruction == '[':
            if memory[current_cell] == 0:
                current_instruction = link
                continue
        elif instruction == ']':
            if memory[current_cell] != 0:
                current_instruction = link
                continue
        elif instruction == '+':
            memory[current_cell] += 1
        elif instruction == '-':
            memory[current_cell] -= 1

        current_instruction += 1

