def input():
    input_data = list(filter(None, open('day_24/input.txt').read().split('\n')))
    tile_moves = list(map(parse_moves, input_data))
    return flip_tiles(tile_moves)

def parse_moves(line: str):
    replacements = [ ('ne', '0 '), ('se', '2 '), ('sw', '3 '), ('nw', '5 '), ('e', '1 '), ('w', '4 '), ]
    for dir, val in replacements:
        line = line.replace(dir, val)
    moves = filter(None, line.split())
    return list(map(int, moves))

dir_to_moves = ( (-1, 0), (0, -1), (1, -1), (1, 0), (0, 1), (-1, 1), )
def apply_one_move(pos: tuple, dir: int):
    return (pos[0] + dir_to_moves[dir][0], pos[1] + dir_to_moves[dir][1])

def apply_moves(grid: set, moves: list):
    pos = (0, 0)
    for m in moves:
        pos = apply_one_move(pos, m)
    if pos in grid:
        grid.remove(pos)
    else:
        grid.add(pos)
    
def flip_tiles(tile_moves: list):
    grid = set()
    for moves in tile_moves:
        apply_moves(grid, moves)
    return grid

def part_1(grid):
    return len(grid)

def count_around(grid: set, pos: tuple):
    count = 0
    for dir in range(0, 6):
        if apply_one_move(pos, dir) in grid:
            count += 1
    return count

def evolve(grid: set):
    new_grid = set()
    for pos in grid:
        count = count_around(grid, pos)
        if count == 1 or count == 2:
            new_grid.add(pos)
        for dir in range(0, 6):
            new_pos = apply_one_move(pos, dir)
            if new_pos not in grid:
                count = count_around(grid, new_pos)
                if count == 2:
                    new_grid.add(new_pos)
    return new_grid

def part_2(grid):
    for i in range(0, 100):
        grid = evolve(grid)
    return len(grid)

if __name__ == '__main__':
    print(part_1(input()))
    print(part_2(input()))
