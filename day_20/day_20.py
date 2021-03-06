def input():
    input_data = list(filter(None, open('day_20/input.txt').read().split('\n\n')))
    return list(map(lambda lines: Tile(lines), input_data))

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


from collections import defaultdict

def count_border_ids(tiles):
    border_id_counts = defaultdict(int)

    for tile in tiles:
        for border in tile.borders:
            border_id_counts[border] += 1
        for border in tile.flipped_borders:
            border_id_counts[border] += 1
    return border_id_counts

def count_unique_borders(borders, border_id_counts):
    count = 0
    for border in borders:
        if border_id_counts[border] == 1:
            count += 1
    return count

def find_corners(tiles, border_id_counts):
    corners = set()
    corners_total = 1
    for tile in tiles:
        if count_unique_borders(tile.borders, border_id_counts) == 2 or count_unique_borders(tile.flipped_borders, border_id_counts) == 2:
            corners.add(tile)
            corners_total *= tile.id
    return corners, corners_total

def part_1(tiles):
    border_id_counts = count_border_ids(tiles)
    corners, corners_total = find_corners(tiles, border_id_counts)
    return corners_total


def find_matching_tile(tiles, searched, border_index, done):
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

def find_first_image_column(tiles, image, image_size, done, border_id_counts):
    x = 0
    for y in range(1, image_size):
        searched = image[x][y-1].flipped_borders[2]
        tile = find_matching_tile(tiles, searched, 0, done)
        if border_id_counts[tile.borders[3]] != 1:
            raise Exception('Not a proper border tile: %d.' % border_id_counts[tile.borders[1]])
        image[x].append(tile)

def find_other_image_columns(tiles, image, image_size, done):
    for x in range(1, image_size):
        image.append([])
        for y in range(0, image_size):
            searched = image[x-1][y].flipped_borders[1]
            tile = find_matching_tile(tiles, searched, 3, done)
            image[x].append(tile)

def make_full_image_tile(tiles, top_left, border_id_counts):
    while border_id_counts[top_left.borders[0]] != 1 or border_id_counts[top_left.borders[3]] != 1:
        top_left.rotate()

    done = set()
    done.add(top_left.id)

    image = [[top_left]]
    image_size = 12

    find_first_image_column(tiles, image, image_size, done, border_id_counts)
    find_other_image_columns(tiles, image, image_size, done)

    lines = ['Tile 0:']
    for y in range(0, image_size):
        for sub_y in range(1, len(image[0][0].image) - 1):
            line_parts = []
            for x in range(0, image_size):
                line_parts.append(image[x][y].image[sub_y][1:-1])
            lines.append(''.join(line_parts))
    return Tile('\n'.join(lines))

def count_monster_dots(full_image):
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
    return count * len(monster)

def count_image_dots(full_image):
    dot_count = 0
    size = len(full_image.image[0])
    for x in range(0, size):
        for y in range(0, size):
            if full_image.image[y][x] == '#':
                dot_count += 1
    return dot_count


def part_2(tiles):
    border_id_counts = count_border_ids(tiles)
    corners, corners_total = find_corners(tiles, border_id_counts)
    full_image = make_full_image_tile(tiles, corners.pop(), border_id_counts)
    return count_image_dots(full_image) - count_monster_dots(full_image)

if __name__ == '__main__':
    print(part_1(input()))
    print(part_2(input()))
