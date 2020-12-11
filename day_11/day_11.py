seats = list(map(lambda row: [c for c in row], filter(None, open('day_11/input.txt').read().split('\n'))))

def count_neighbours(x, y, seats, max_dist):
    count = 0
    mx, my = len(seats[0]), len(seats)
    for dx, dy in ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)):
        for d in range(1, max_dist+1):
            tx, ty = x+dx*d, y+dy*d
            if ty < 0 or ty >= my:
                break
            if tx < 0 or tx >= mx:
                break
            c = seats[ty][tx]
            if c == '.':
                continue
            count += (c == '#')
            break
    return count

def evolve_seats(seats, max_dist, tolerance):
    new_seats = [row.copy() for row in seats]
    changed = 0
    for y in range(0, len(seats)):
        for x in range(0, len(seats[0])):
            if seats[y][x] == '.':
                continue
            elif seats[y][x] == 'L':
                if count_neighbours(x, y, seats, max_dist) == 0:
                    new_seats[y][x] = '#'
                    changed += 1
            elif seats[y][x] == '#':
                if count_neighbours(x, y, seats, max_dist) >= tolerance:
                    new_seats[y][x] = 'L'
                    changed += 1
    return new_seats, changed

def print_seats(seats):
    print('\n'.join(map(lambda row: ''.join(row), seats)) +'\n\n')

def evolve_until_stable(seats, max_dist=1, tolerance=4):
    evolution_generations = 0
    while True:
        evolution_generations += 1
        seats, changed = evolve_seats(seats, max_dist, tolerance)
        #print_seats(seats)
        if not changed:
            return seats, evolution_generations
        
final_seats, gens = evolve_until_stable(seats)
print(gens)
occupied_count = sum(map(lambda row: sum(map(lambda c: 1 if c == '#' else 0, row)), final_seats))
print(str(occupied_count))

final_seats, gens = evolve_until_stable(seats, 10000, 5)
print(gens)
occupied_count = sum(map(lambda row: sum(map(lambda c: 1 if c == '#' else 0, row)), final_seats))
print(str(occupied_count))

    
