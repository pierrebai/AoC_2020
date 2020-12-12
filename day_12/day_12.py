input_data = map(lambda s: (s[0], int(s[1:])), filter(None, open('day_12/input.txt').read().split('\n')))

def turn(d, v):
    if v == 0:
        return d
    elif v == 90:
        return {
            'N':'E',
            'E':'S',
            'S':'W',
            'W':'N',
        }[d]
    elif v == 270:
        return {
            'E':'N',
            'S':'E',
            'W':'S',
            'N':'W',
        }[d]
    elif v == 180:
        return {
            'E':'W',
            'S':'N',
            'W':'E',
            'N':'S',
        }[d]
    else:
        return d
    
x, y = 0, 0
d = 'E'

def move(c, v):
    global x, y, d
    if c == 'N':
        y += v
    elif c == 'S':
        y -= v
    elif c== 'E':
        x += v
    elif c == 'W':
        x -= v
    elif c == 'F':
        move(d, v)
    elif c ==  'R':
        d = turn(d, v)
    elif c == 'L':
        d = turn(d, 360 - v)

for c, v in input_data:
    move(c, v)

print(str(abs(x) + abs(y)))
