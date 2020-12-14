input_data = list(filter(None, open('day_14/input.txt').read().split('\n')))
op_and_values = list(map(lambda v: v.split(' = '), input_data))

class Memory:
    def __init__(self):
        self.mem = {}
        self.or_mask = 0
        self.and_mask = 0b11111111111111111111111111111111111111111111111111111

def mask_op(mem: Memory, op: str, raw_mask: str):
    mem.or_mask = int(''.join(map(lambda c: '1' if c == '1' else '0', raw_mask.strip())), 2)
    mem.and_mask = int(''.join(map(lambda c: '1' if c == 'X' else '0', raw_mask.strip())), 2)

import re
mem_addr_re = re.compile('''mem\[([0-9]+)\]''')
def mem_op(mem: Memory, op: str, raw_value: str):
    addr = int(mem_addr_re.match(op).group(1))
    value = int(raw_value)
    value = (value & mem.and_mask) | mem.or_mask
    mem.mem[addr] = value

def execute_ops(mem, ops):
    for op, raw_value in ops:
        if op.strip() == 'mask':
            mask_op(mem, op, raw_value)
        else:
            mem_op(mem, op, raw_value)

mem = Memory()
execute_ops(mem, op_and_values)
total = sum(mem.mem.values())
print(str(total))

class FloatingMemory:
    def __init__(self):
        self.mem = {}
        self.or_mask = 0
        self.float_mask = 0

def mask_op(mem: FloatingMemory, op: str, raw_mask: str):
    mem.or_mask = int(''.join(map(lambda c: '1' if c == '1' else '0', raw_mask.strip())), 2)
    mem.float_mask = int(''.join(map(lambda c: '1' if c == 'X' else '0', raw_mask.strip())), 2)

def float_op(addr, value, mask, bit):
    if bit == 36:
        mem.mem[addr] = value
        return

    or_mask = (1 << bit)
    if mask & or_mask:
        and_mask = 0b1111111111111111111111111111111111111 ^ or_mask
        float_op(addr | or_mask,  value, mask, bit+1)
        float_op(addr & and_mask, value, mask, bit+1)
    else:
        float_op(addr, value, mask, bit+1)

def mem_op(mem: FloatingMemory, op: str, raw_value: str):
    addr = int(mem_addr_re.match(op).group(1))
    addr = addr | mem.or_mask
    value = int(raw_value)
    float_op(addr, value, mem.float_mask, 0)

mem = FloatingMemory()
execute_ops(mem, op_and_values)
total = sum(mem.mem.values())
print(str(total))
