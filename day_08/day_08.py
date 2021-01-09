def input():
    return Program(compile('day_08/input.txt'))

class Program:
    def __init__(self, ops):
        self.ops = ops
        self.acc, self.cnt = 0, 0

    @staticmethod
    def _is_already_visited(index, visited):
        return False

    def reset(self):
        self.acc, self.cnt = 0, 0

    def execute(self):
        visited = set()
        while True:
            if self.cnt in visited:
                break
            if self.cnt >= len(self.ops):
                break
            visited.add(self.cnt)
            op, value = self.ops[self.cnt]
            op(self, value)
        return self.acc


def acc_op(prg, x):
    prg.acc += x
    prg.cnt += 1

def jmp_op(prg, x):
    prg.cnt += x

def nop_op(prg, x):
    prg.cnt += 1

def compile(filename):
    ops = {
        'acc': acc_op,
        'jmp': jmp_op,
        'nop': nop_op,
    }

    def parse_op(s):
        op_and_value = s.strip().split()
        return (ops[op_and_value[0]], int(op_and_value[1]))

    return list(map(parse_op, filter(None, open(filename).read().split('\n'))))


def part_1(program):
    return program.execute()


def find_bug(prg):
    for mod in range(0,len(prg.ops)):
        mod_program = Program(prg.ops.copy())
        if mod_program.ops[mod][0] == acc_op:
            continue
        mod_op, mod_value = mod_program.ops[mod]
        mod_program.ops[mod] = (nop_op, mod_value) if mod_op == jmp_op else (jmp_op, mod_value)
        acc = mod_program.execute()
        if mod_program.cnt >= len(mod_program.ops):
            return acc
    return 0

def part_2(program):
    return find_bug(program)

if __name__ == '__main__':
    print(part_1(input()))
    print(part_2(input()))
