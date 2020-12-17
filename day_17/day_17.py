from itertools import product

input_data = list(filter(None, open('day_17/input.txt').read().split('\n')))

def prepare_cubes(dims: int):
    cubes = {}
    for y, line in enumerate(input_data):
        for x, c in enumerate(line):
            if c == '#':
                coord = (x, y) + (0,) * (dims - 2)
                cubes[coord] = 1
    return cubes

def count_neighbours(cubes, coord: tuple, dims: int):
    count = 0
    for deltas in product((-1, 0, 1), repeat=dims):
        if any(deltas):
            dc = tuple([c + d for c, d in zip(coord, deltas)])
            if dc in cubes:
                count += 1
    return count

def execute_cycle(cubes, dims: int):
    new_cubes = {}
    done = set()
    for coord in cubes:
        for deltas in product((-1, 0, 1), repeat=dims):
            dc = tuple([c + d for c, d in zip(coord, deltas)])
            if dc not in done:
                done.add(dc)
                active = dc in cubes
                count = count_neighbours(cubes, dc, dims)
                if count == 3 or (count == 2 and active):
                    new_cubes[dc] = 1
    return new_cubes

def execute_n_cycles(cycles: int, dims: int):
    cubes = prepare_cubes(dims)
    for i in range(0, cycles):
        cubes = execute_cycle(cubes, dims)
    return cubes

print(str(len(execute_n_cycles(6, 3))))
print(str(len(execute_n_cycles(6, 4))))
