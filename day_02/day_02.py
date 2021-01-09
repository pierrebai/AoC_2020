def input():
    return open('day_02/input.txt')

def password_is_valid_part_1(min, max, letter, password):
    count = sum(map(lambda x: 1 if x == letter else 0, password))
    return min <= count <= max

password_is_valid = password_is_valid_part_1

def validate_line(line):
    if not line:
        return False
    times_letter, password = line.split(':')
    password = password.strip()
    times, letter = times_letter.split()
    min, max = map(int, times.split('-'))
    return password_is_valid(min, max, letter, password)

def pos_is_valid(pos, letter, password):
    pos -= 1
    return 0 <= pos <= len(password) and password[pos] == letter

def password_is_valid_part_2(pos1, pos2, letter, password):
    return 1 == sum((pos_is_valid(pos1, letter, password), pos_is_valid(pos2, letter, password)))

def part_1(input_data):
    global password_is_valid
    password_is_valid = password_is_valid_part_1
    return sum(map(validate_line, input_data))

def part_2(input_data):
    global password_is_valid
    password_is_valid = password_is_valid_part_2
    return sum(map(validate_line, input_data))

if __name__ == '__main__':
    print(part_1(input()))
    print(part_2(input()))
