from rpython.rlib.jit import JitDriver
import os


SETUP_LOOP = 0
END_LOOP = 1
INC = 2
DEC = 3
RSHIFT = 4
LSHIFT = 5
WRITE = 6
READ = 7
DROP = 8
ADD = 9

TERMINATE = 255


jitdriver = JitDriver(
    greens=['program_counter', 'input_bytes'],
    reds=['data_pointer', 'memory']
)


def jitpolicy(driver):
    from rpython.jit.codewriter.policy import JitPolicy
    return JitPolicy()


SHORT_OPCODE = 1
LONG_OPCODE = 3


def interprete(input_bytes):
    program_counter = 0
    data_pointer = 0
    memory = [0] * 30000

    while 1:
        jitdriver.jit_merge_point(
            program_counter=program_counter, input_bytes=input_bytes,
            data_pointer=data_pointer, memory=memory
        )
        opcode = input_bytes[program_counter]
        argument = (
            input_bytes[program_counter+1] * 256 +
            input_bytes[program_counter+2]
        )

        if opcode == LSHIFT:
            data_pointer -= argument
            program_counter += LONG_OPCODE

        elif opcode == RSHIFT:
            data_pointer += argument
            program_counter += LONG_OPCODE

        elif opcode == READ:
            memory[data_pointer] = ord(os.read(0, 1)[0])
            program_counter += SHORT_OPCODE

        elif opcode == WRITE:
            os.write(1, str(chr(memory[data_pointer])))
            program_counter += SHORT_OPCODE

        elif opcode == SETUP_LOOP:
            if memory[data_pointer] == 0:
                program_counter += LONG_OPCODE + argument + LONG_OPCODE
            else:
                program_counter += LONG_OPCODE

        elif opcode == END_LOOP:
            if memory[data_pointer] == 0:
                program_counter += LONG_OPCODE
            else:
                program_counter -= LONG_OPCODE + argument
                jitdriver.can_enter_jit(
                    program_counter=program_counter, input_bytes=input_bytes,
                    data_pointer=data_pointer, memory=memory
                 )

        elif opcode == INC:
            memory[data_pointer] += argument
            program_counter += LONG_OPCODE

        elif opcode == DEC:
            memory[data_pointer] -= argument
            program_counter += LONG_OPCODE

        elif opcode == DROP:
            memory[data_pointer] = 0
            program_counter += SHORT_OPCODE

        elif opcode == ADD:
            if input_bytes[program_counter+1] == 0:
                shift = input_bytes[program_counter+2]
            else:
                shift = -input_bytes[program_counter+2]
            memory[data_pointer+shift] += memory[data_pointer]
            memory[data_pointer] = 0
            program_counter += LONG_OPCODE

        elif opcode == TERMINATE:
            break

    return 0


def main(argv):
    if len(argv) != 2:
        print("This tool takes exactly one arguments - filename.")
        return 1
    if not os.path.exists(argv[1]):
        print("File %s not found." % argv[1])
        return 1
    with open(argv[1], 'rb') as data:
        code = data.read()
    return interprete(bytearray(code))


def target(*args):
    return main, None

