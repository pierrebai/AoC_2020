def password_is_valid(min, max, letter, password):
    count = sum(map(lambda x: 1 if x == letter else 0, password))
    return min <= count <= max

def validate_line(line):
    if not line:
        return False
    times_letter, password = line.split(':')
    password = password.strip()
    times, letter = times_letter.split()
    min, max = map(int, times.split('-'))
    return password_is_valid(min, max, letter, password)

def print_valid_count():
    valid_count = sum(map(validate_line, open('day_02/input.txt')))
    print (str(valid_count))

print_valid_count()

def pos_is_valid(pos, letter, password):
    pos -= 1
    return 0 <= pos <= len(password) and password[pos] == letter

def password_is_valid_2(pos1, pos2, letter, password):
    return 1 == sum((pos_is_valid(pos1, letter, password), pos_is_valid(pos2, letter, password)))

password_is_valid = password_is_valid_2

print_valid_count()
