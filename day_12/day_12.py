def input():
    return list(map(lambda s: (s[0], int(s[1:])), filter(None, open('day_12/input.txt').read().split('\n'))))

dirs = { 'E': 0, 'S': 1, 'W': 2, 'N': 3 }
rots = { 'R': 1, 'L': 3 }
moves = [(1, 0), (0, -1), (-1, 0), (0, 1)]

class ship:
    x, y, dir = (0, 0, 0)

    def turn(ship, cmd, value):
        amount = rots[cmd] * value // 90
        ship.dir = (ship.dir + amount) % 4

    def move_in_dir(ship, dir, value):
        deltas = moves[dir]
        ship.x += deltas[0] * value
        ship.y += deltas[1] * value

    def move(ship, cmd, value):
        ship.move_in_dir(dirs[cmd], value)
        
    def forward(ship, cmd, value):
        ship.move_in_dir(ship.dir, value)

    def execute_commands(ship, cmds):
        cmd_ops = {
            'E': ship.move,
            'S': ship.move,
            'W': ship.move,
            'N': ship.move,
            'L': ship.turn,
            'R': ship.turn,
            'F': ship.forward,
        }
        for c, v in cmds:
            cmd_ops[c](c, v)

def part_1(input_data):
    s = ship()
    s.execute_commands(input_data)
    return abs(s.x) + abs(s.y)

class waypoint_ship(ship):
    wx, wy = (10, 1)

    def turn(ship, cmd, value):
        amount = (rots[cmd] * value // 90) % 4
        for i in range(0, amount):
            ship.wx, ship.wy = ship.wy, -ship.wx

    def move(ship, cmd, value):
        deltas = moves[dirs[cmd]]
        ship.wx += deltas[0] * value
        ship.wy += deltas[1] * value
        
    def forward(ship, cmd, value):
        ship.x += ship.wx * value
        ship.y += ship.wy * value

def part_2(input_data):
    s = waypoint_ship()
    s.execute_commands(input_data)
    return abs(s.x) + abs(s.y)

if __name__ == '__main__':
    print(part_1(input()))
    print(part_2(input()))
