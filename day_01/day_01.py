def clean_lines(file_name):
    return filter(None, map(lambda l2: l2.strip(), open(file_name)))

def input():
    return set(map(lambda x: int(x), clean_lines('day_01/input.txt')))

def match_target(values, target):
    for v in values:
        complement = target - v
        if complement in values:
            return v * complement
    return None

def match_2020(values):
    return match_target(values, 2020)

def match_3_2020(values):
    for v in values:
        matches = match_target(values, 2020 - v)
        if matches:
            return v * matches

def part_1(input_data):
    return match_2020(input_data)

def part_2(input_data):
    return match_3_2020(input_data)

if __name__ == '__main__':
    print(part_1(input()))
    print(part_2(input()))
