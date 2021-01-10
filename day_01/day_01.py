def input():
    return set(map(lambda x: int(x), clean_lines('day_01/input.txt')))

def clean_lines(file_name):
    return filter(None, map(lambda l2: l2.strip(), open(file_name)))

def match_target(values, target):
    for v in values:
        complement = target - v
        if complement in values:
            return v * complement
    return None

def part_1(values):
    return match_target(values, 2020)

def part_2(values):
    for v in values:
        matches = match_target(values, 2020 - v)
        if matches:
            return v * matches

if __name__ == '__main__':
    print(part_1(input()))
    print(part_2(input()))
