input_data = list(filter(None, open('day_17/input.txt').read().split('\n')))
cubes = {}
for y, line in enumerate(input_data):
    for x, c in enumerate(line):
        if c == '#':
            cubes[(x, y, 0, 0)] = 1

def count_neighbours(cubes, x: int, y: int, z: int, w: int):
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in range(-1, 2):
                    if dx != 0 or dy != 0 or dz != 0 or dw != 0:
                        if (x+dx, y+dy, z+dz, w+dw) in cubes:
                            count += 1
    return count

def execute_cycle(cubes):
    new_cubes = {}
    done = set()
    for x, y, z, w in cubes.keys():
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                for dz in range(-1, 2):
                    for dw in range(-1, 2):
                        coord = (x+dx, y+dy, z+dz, w+dw)
                        if coord not in done:
                            done.add(coord)
                            active = coord in cubes
                            count = count_neighbours(cubes, *coord)
                            if count == 3 or (count == 2 and active):
                                new_cubes[coord] = 1
    return new_cubes

for i in range(0,6):
    cubes = execute_cycle(cubes)

print(str(len(cubes)))
