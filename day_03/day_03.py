def parse_map(line: str):
    return list(map(lambda x: 1 if x == '#' else 0, line))

def clean_line(line):
    return line.strip()

def count_trees(right: int, down: int):
    count = 0
    x = 0
    y = 0
    for map_line in map(parse_map, map(clean_line, open('day_03/input.txt'))):
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

def right_3_down_1():
    print(str(count_trees(3, 1)))

def multi_slopes():
    slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    counts = 1
    for right, down in slopes:
        counts *= count_trees(right, down)
    print(str(counts))

right_3_down_1()
multi_slopes()