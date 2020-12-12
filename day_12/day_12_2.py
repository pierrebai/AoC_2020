input_data = map(lambda s: (s[0], int(s[1:])), filter(None, open('day_12/input.txt').read().split('\n')))

wx, wy = 10, 1
x, y = 0, 0
d = 'E'

def turn(d, v):
    global wx, wy
    if v == 0:
        return d
    elif v == 90:
        wx, wy = wy, -wx
    elif v == 270:
        wx, wy = -wy, wx
    elif v == 180:
        wx, wy = -wx, -wy
    else:
        pass


def move(c, v):
    global x, y, d, wx, wy
    if c == 'N':
        wy += v
    elif c == 'S':
        wy -= v
    elif c== 'E':
        wx += v
    elif c == 'W':
        wx -= v
    elif c == 'F':
        x += wx * v
        y += wy * v
    elif c ==  'R':
        turn(d, v)
    elif c == 'L':
        turn(d, 360 - v)

for c, v in input_data:
    move(c, v)

print(str(abs(x) + abs(y)))
