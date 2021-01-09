def input():
    #card_public_key = 5764801   # Example
    #door_public_key = 17807724  # Example
    card_public_key = 10943862
    door_public_key = 12721030
    return (card_public_key, door_public_key)

def transform(subject_number: int, loop_size: int, modulo: int = 20201227):
    value = 1
    for i in range(0, loop_size):
        value *= subject_number
        value %= modulo
    return value

def find_loop_size_from_public_key(subject_number: int, public_key: int, modulo: int = 20201227):
    value = 1
    for loop_size in range(1, max(public_key, modulo)):
        value *= subject_number
        value %= modulo
        if value == public_key:
            return loop_size
    raise Exception("Loop size not found.")

def part_1(input_data):
    card_public_key, door_public_key = input_data
    card_loop_size = find_loop_size_from_public_key(7, card_public_key)
    door_loop_size = find_loop_size_from_public_key(7, door_public_key)

    card_encryption_key = transform(door_public_key, card_loop_size)
    door_encryption_key = transform(card_public_key, door_loop_size)

    return door_encryption_key

def part_2(input_data):
    return None

if __name__ == '__main__':
    print(part_1(input()))
    print(part_2(input()))
