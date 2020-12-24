from collections import defaultdict

def parse_moves(line: str):
    replacements = [ ('ne', '0 '), ('se', '2 '), ('sw', '3 '), ('nw', '5 '), ('e', '1 '), ('w', '4 '), ]
    for dir, val in replacements:
        line = line.replace(dir, val)
    moves = filter(None, line.split())
    return list(map(int, moves))

class hex:
    dir_to_moves = ( (-1,   0), (0, -1), (1, -1), (1,  0), (0,  1), (-1,  1), )
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def move(self, dir):
        deltas = hex.dir_to_moves[dir]
        self.x += deltas[0]
        self.y += deltas[1]

def apply_moves(grid: defaultdict, moves: list):
    pos = hex()
    for m in moves:
        pos.move(m)
    grid[(pos.x, pos.y)] = not grid[(pos.x, pos.y)]
    
def flip_tiles(tile_moves: list):
    grid = defaultdict(bool)
    for moves in tile_moves:
        apply_moves(grid, moves)
    return grid

input_data = list(filter(None, open('day_24/input.txt').read().split('\n')))
tile_moves = list(map(parse_moves, input_data))
grid = flip_tiles(tile_moves)
print(sum(map(int, grid.values())))

def count_around(grid: set, pos: tuple):
    count = 0
    for dir in range(0, 6):
        tile = hex(pos[0], pos[1])
        tile.move(dir)
        if (tile.x, tile.y) in grid:
            count += 1
    return count

def evolve(grid: set):
    new_grid = set()
    for pos in grid:
        count = count_around(grid, pos)
        if count == 1 or count == 2:
            new_grid.add(pos)
        for dir in range(0, 6):
            tile = hex(pos[0], pos[1])
            tile.move(dir)
            new_pos = (tile.x, tile.y)
            if new_pos not in grid:
                count = count_around(grid, new_pos)
                if count == 2:
                    new_grid.add(new_pos)
    return new_grid

cleaned_grid = set()
for k, v in grid.items():
    if v:
        cleaned_grid.add(k)

for i in range(0, 100):
    cleaned_grid = evolve(cleaned_grid)

print(len(cleaned_grid))
