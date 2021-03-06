def input():
    boarding_passes = filter(None, open('day_05/input.txt').read().split('\n'))
    return list(map(lambda bp: (parse_row(bp), parse_seat(bp)), boarding_passes))

def to_binary_text(s, letter_for_one):
    return map(lambda l: '1' if letter_for_one == l else '0', s)

def to_binary(s, letter_for_one):
    return int(''.join(to_binary_text(s, letter_for_one)), base=2)

def parse_row(bp):
    return to_binary(bp[0:7], 'B')

def parse_seat(bp):
    return to_binary(bp[-3:], 'R')

def part_1(row_seats):
    ids = list(map(lambda rs: rs[0] * 8 + rs[1], row_seats))
    max_id = max(ids)
    return max_id

def part_2(row_seats):
    ids = list(map(lambda rs: rs[0] * 8 + rs[1], row_seats))
    row_seats.sort()
    start_row = 1 + row_seats[0][0]
    end_row = row_seats[-1][0]
    ids = set(ids)
    for id in range(start_row * 8, end_row * 8):
        if id not in ids:
            return id

if __name__ == '__main__':
    print(part_1(input()))
    print(part_2(input()))
