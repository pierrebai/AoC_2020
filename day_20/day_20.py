input_data = list(filter(None, open('day_20/input.txt').read().split('\n\n')))

class Tile:
    def __init__(self, lines):
        lines = lines.split('\n')
        self.id = int(lines[0].split()[1].strip(':'))
        self.image = [line.strip() for line in lines[1:]]
        self.build_borders()

    def build_borders(self):
        lines = self.image
        self.borders = [
            ''.join(lines[0]),
            ''.join([line[-1] for line in lines]),
            ''.join(reversed(lines[-1])),
            ''.join([line[0] for line in reversed(lines)]),
        ]
        self.flipped_borders = [
            ''.join(reversed(lines[0])),
            ''.join([line[-1] for line in reversed(lines)]),
            ''.join(lines[-1]),
            ''.join([line[0] for line in lines]),
        ]

    def flip(self):
        self.image = [''.join(reversed(line)) for line in self.image[:]]
        self.build_borders()

    def rotate(self):
        size = len(self.image)
        new_image = []
        for x in range(0, size):
            new_image.append([])
            for y in range(0, size):
                new_image[x].append(self.image[size - 1 - y][x])
        self.image = [''.join(line) for line in new_image]
        self.build_borders()

tiles = list(map(lambda lines: Tile(lines), input_data))

for tile in tiles:
    borders = tile.borders[:]
    tile.flip()
    if tile.flipped_borders[0] != borders[0]:
        raise Exception('Bad flip.')
    if tile.flipped_borders[1] != borders[3]:
        raise Exception('Bad flip.')
    if tile.flipped_borders[2] != borders[2]:
        raise Exception('Bad flip.')
    if tile.flipped_borders[3] != borders[1]:
        raise Exception('Bad flip.')
    borders = tile.borders[:]
    tile.rotate()
    tile.rotate()
    tile.rotate()
    tile.rotate()
    if tile.borders[0] != borders[0]:
        raise Exception('Bad rotate.')
    if tile.borders[1] != borders[1]:
        raise Exception('Bad rotate.')
    if tile.borders[2] != borders[2]:
        raise Exception('Bad rotate.')
    if tile.borders[3] != borders[3]:
        raise Exception('Bad rotate.')

def print_tile(tile, file):
    print('Tile %d:' % tile.id, file=file)
    for line in tile.image:
        print(line, file=file)
    print('', file=file)

#with open('day_20/output.txt', 'w') as file:
#    for tile in tiles:
#        print_tile(tile, file)

from collections import defaultdict
border_id_counts = defaultdict(int)

for tile in tiles:
    for border in tile.borders:
        border_id_counts[border] += 1
    for border in tile.flipped_borders:
        border_id_counts[border] += 1

#print(border_id_counts)

unique_border_count = len(list(filter(lambda b: b == 1, border_id_counts.values())))
duo_border_count = len(list(filter(lambda b: b == 2, border_id_counts.values())))
other_border_count = len(list(filter(lambda b: b >  2, border_id_counts.values())))

print('tiles:       %d' % len(tiles))
print('uniques:     %d' % unique_border_count)
print('duos:        %d' % duo_border_count)
print('others:      %d' % other_border_count)
print('total:       %d' % (unique_border_count + 2 * duo_border_count))
print('total sides: %d' % (144 * 4))
print('borders      %d' % (12 * 4))

def count_unique_borders(borders):
    count = 0
    for border in borders:
        if border_id_counts[border] == 1:
            count += 1
    return count

def find_corners(tiles):
    corners = set()
    corners_total = 1
    for tile in tiles:
        if count_unique_borders(tile.borders) == 2 or count_unique_borders(tile.flipped_borders) == 2:
            corners.add(tile)
            corners_total *= tile.id
    return corners, corners_total

corners, corners_total = find_corners(tiles)
print(corners_total)

top_left = corners.pop()
while border_id_counts[top_left.borders[0]] != 1 or border_id_counts[top_left.borders[3]] != 1:
    top_left.rotate()

done = set()
done.add(top_left.id)
image = [[top_left]]
image_size = 12

def find_matching_tile(searched, border_index):
    for tile in tiles:
        if tile.id in done:
            continue
        if searched in tile.flipped_borders:
            tile.flip()
            if searched not in tile.borders:
                raise Exception('Bad flip.')
        if searched in tile.borders:
            while searched != tile.borders[border_index]:
                tile.rotate()
            done.add(tile.id)
            return tile
    raise Exception('Image tile not found.')

x = 0
for y in range(1, image_size):
    searched = image[x][y-1].flipped_borders[2]
    tile = find_matching_tile(searched, 0)
    if border_id_counts[tile.borders[3]] != 1:
        raise Exception('Not a proper border tile: %d.' % border_id_counts[tile.borders[1]])
    image[x].append(tile)

for x in range(1, image_size):
    image.append([])
    for y in range(0, image_size):
        searched = image[x-1][y].flipped_borders[1]
        tile = find_matching_tile(searched, 3)
        image[x].append(tile)

def make_full_image_tile(image):
    lines = ['Tile 0:']
    for y in range(0, image_size):
        for sub_y in range(1, len(image[0][0].image) - 1):
            line_parts = []
            for x in range(0, image_size):
                line_parts.append(image[x][y].image[sub_y][1:-1])
            lines.append(''.join(line_parts))
    return Tile('\n'.join(lines))

full_image = make_full_image_tile(image)
print_tile(full_image, open('day_20/full_image.txt', 'w'))


monster = [
    (18, 0),
    (0, 1), (5, 1), (6, 1), (11, 1), (12, 1), (17, 1), (18, 1), (19, 1), 
    (1, 2), (4, 2), (7, 2), (10, 2), (13, 2), (16, 2), 
]

size = len(full_image.image[0])
count = 0
for flip in range(0, 2):
    full_image.flip()
    for rot in range(0, 4):
        full_image.rotate()
        for x in range(0, size):
            for y in range(0, size):
                for delta in monster:
                    mx = x+delta[0]
                    my = y+delta[1]
                    if mx >= size or my >= size:
                        break
                    if full_image.image[my][mx] != '#':
                        break
                else:
                    count += 1

dot_count = 0
for x in range(0, size):
    for y in range(0, size):
        if full_image.image[y][x] == '#':
            dot_count += 1


print(dot_count - count * len(monster))