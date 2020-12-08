def is_already_visited(index, visited):
    if index in visited:
        return True
    visited.add(index)
    return False

def acc_op(acc, prg_cnt, x):
    acc += x
    return acc, prg_cnt+1

def jmp_op(acc, prg_cnt, x):
    prg_cnt += x
    return acc, prg_cnt

def nop_op(acc, prg_cnt, x):
    return acc, prg_cnt+1

ops = {
    'acc': acc_op,
    'jmp': jmp_op,
    'nop': nop_op,
}

def parse_op(s):
    op_and_value = s.strip().split()
    return (op_and_value[0], int(op_and_value[1]))

program = list(map(parse_op, filter(None, open('day_08/input.txt').read().split('\n'))))

def execute(prg):
    acc, prg_cnt = 0, 0
    visited = set()
    while not is_already_visited(prg_cnt, visited):
        if prg_cnt >= len(prg):
            break
        op, value = prg[prg_cnt]
        acc, prg_cnt = ops[op](acc, prg_cnt, value)
    return acc, prg_cnt

final_acc, _ = execute(program)
print(str(final_acc))


def find_bug(prg):
    for mod in range(0,len(prg)):
        mod_program = prg.copy()
        if mod_program[mod][0] == 'acc':
            continue
        mod_op, mod_value = prg[mod]
        mod_program[mod] = ('nop', mod_value) if mod_op == 'jmp' else ('jmp', mod_value)
        acc, prg_cnt = execute(mod_program)
        if prg_cnt >= len(mod_program):
            return acc
    return 0

final_acc = find_bug(program)
print(str(final_acc))
