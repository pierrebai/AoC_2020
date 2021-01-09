def input():
    return list(map(parse_map, map(lambda l: l.strip(), open('day_03/input.txt'))))
    
def parse_map(line: str):
    return list(map(lambda x: 1 if x == '#' else 0, line))

def count_trees(lines, right: int, down: int):
    count = 0
    x = 0
    y = 0
    for map_line in lines:
        print_line = list(map(lambda x: '.' if x == 0 else '#', map_line))
        if y % down == 0:
            if map_line[x]:
                count += 1
                print_line[x] = 'X'
            else:
                print_line[x] = 'O'
            x += right
            x %= len(map_line)
        #print(''.join(print_line))
        y += 1
    return count

def part_1(input_data):
    return count_trees(input_data, 3, 1)

def part_2(input_data):
    slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    counts = 1
    for right, down in slopes:
        counts *= count_trees(input_data, right, down)
    return counts

if __name__ == '__main__':
    print(part_1(input()))
    print(part_2(input()))
