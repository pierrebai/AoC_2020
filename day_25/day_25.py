#card_public_key = 5764801   # Example
#door_public_key = 17807724  # Example

card_public_key = 10943862
door_public_key = 12721030

def transform(subject_number: int, loop_size: int, modulo: int = 20201227):
    value = 1
    for i in range(0, loop_size):
        value *= subject_number
        value %= modulo
    return value

def find_loop_size_from_public_key(subject_number: int, public_key: int, modulo: int = 20201227):
    value = 1
    for loop_size in range(1, 10000000):
        value *= subject_number
        value %= modulo
        if value == public_key:
            return loop_size
    return -1

card_loop_size = find_loop_size_from_public_key(7, card_public_key)
door_loop_size = find_loop_size_from_public_key(7, door_public_key)

print(card_loop_size)
print(door_loop_size)

card_encryption_key = transform(door_public_key, card_loop_size)
door_encryption_key = transform(card_public_key, door_loop_size)

print(card_encryption_key)
print(door_encryption_key)
