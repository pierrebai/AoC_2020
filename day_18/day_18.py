def input():
    return list(filter(None, open('day_18/input.txt').read().split('\n')))

import re
number_re = re.compile('''[0-9]+''')

def apply_op(v1: int, v2: int, op: str, to_mult, mult_is_low: bool):
    if mult_is_low and op == '*':
        if v1:
            to_mult.append(v1)
        return v2
    else:
        if op == '+':
            return v1 + v2
        if op == '*':
            return v1 * v2
        return v2

def parse_until_closed(line: str, index: int, mult_is_low: bool):
    value = 0
    op = ''
    to_mult = []
    while index < len(line):
        number_match = number_re.match(line, index)
        if number_match:
            number = int(number_match.group(0))
            value = apply_op(value, number, op, to_mult, mult_is_low)
            index = number_match.end(0) - 1
        elif line[index] == '+' or line[index] == '*':
            op = line[index]
        elif line[index] == '(':
            number, index = parse_until_closed(line, index+1, mult_is_low)
            value = apply_op(value, number, op, to_mult, mult_is_low)
        elif line[index] == ')':
            break
        index += 1
    for v in to_mult:
        value *= v
    return value, index

def part_1(input_data):
    values = list(map(lambda l: parse_until_closed(l, 0, False)[0], input_data))
    return sum(values)

def part_2(input_data):
    values = list(map(lambda l: parse_until_closed(l, 0, True)[0], input_data))
    return sum(values)

if __name__ == '__main__':
    print(part_1(input()))
    print(part_2(input()))
