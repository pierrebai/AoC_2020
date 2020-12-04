def clean_lines(file_name):
    return filter(None, map(lambda l2: l2.strip(), open(file_name)))

values = set(map(lambda x: int(x), clean_lines('day_01/input.txt')))

def match_target(target):
    for v in values:
        complement = target - v
        if complement in values:
            return v * complement
    return None

def match_2020():
    print(str(match_target(2020)))

def match_3_2020():
    for v in values:
        matches = match_target(2020 - v)
        if matches:
            print(str(v * matches))
            break

match_2020()
match_3_2020()
