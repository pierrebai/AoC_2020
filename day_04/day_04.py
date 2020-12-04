def clean_lines(file_name):
    return map(lambda l: l.strip(), open(file_name))

def read_passports():
    passports = []
    passport = {}
    for line in clean_lines('day_04/input.txt'):
        if not line and passport:
            passports.append(passport)
            passport = {}
            continue
        fields = line.split()
        for field in fields:
            key, value = field.split(':')
            passport[key] = value
    if passport:    
        passports.append(passport)
    return passports

def passport_has_fields(passport, required_fields, validate):
    for f, v in required_fields:
        if f not in passport:
            return False
        if validate and not v(passport[f]):
            return False
    return True

def is_height_valid(hgt):
    if len(hgt) == 4 and 'in' == hgt[2:4]:
        return 59 <= int(hgt[0:2]) <= 76
    if len(hgt) == 5 and 'cm' == hgt[3:5]:
        return 150 <= int(hgt[0:3]) <= 193
    return False

def is_hair_valid(hcr):
    return len(hcr) == 7 and hcr[0] == '#' and sum(map(lambda x: x in '0123456789abcdef', hcr[1:7])) == 6

def is_eye_valid(eye):
    return eye in {
        'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth',
    }

def is_pid_valid(pid):
    return len(pid) == 9 and sum(map(lambda x: x in '0123456789', pid)) == 9

required_fields = [
    ('byr', lambda x: len(x) == 4 and 1920 <= int(x) <= 2002 ),  # (Birth Year)
    ('iyr', lambda x: len(x) == 4 and 2010 <= int(x) <= 2020 ),  # (Issue Year)
    ('eyr', lambda x: len(x) == 4 and 2020 <= int(x) <= 2030 ),  # (Expiration Year)
    ('hgt', is_height_valid ),  # (Height)
    ('hcl', is_hair_valid ),  # (Hair Color)
    ('ecl', is_eye_valid ),  # (Eye Color)
    ('pid', is_pid_valid ),  # (Passport ID)
    # ('cid', None ),  # (Country ID)    
]

def is_passport_valid(passport):
    return passport_has_fields(passport, required_fields, False)

def is_passport_really_valid(passport):
    return passport_has_fields(passport, required_fields, True)

passports = read_passports()
valids = list(map(is_passport_valid, passports))
count = sum(valids)
print(str(count))

valids = list(map(is_passport_really_valid, passports))
count = sum(valids)
print(str(count))
