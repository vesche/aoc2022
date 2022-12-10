
with open('inputs/day09.txt') as f:
    data = f.read().splitlines()

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'<Coord (x={self.x}, y={self.y})>'

H = Coord(0, 0)
T = Coord(0, 0)

def touching(c1: Coord, c2: Coord) -> bool:
    if abs(c1.x - c2.x) > 1 or abs(c1.y - c2.y) > 1:
        return False
    return True

for line in data:
    direction, steps = line.split()
    steps = int(steps)

    for _ in range(steps):
        if direction == 'U':
            H.y += 1
        elif direction == 'D':
            H.y -= 1
        elif direction == 'L':
            H.x -= 1
        elif direction == 'R':
            H.x += 1

        print(direction, steps)
        print(f'H={H}, T={T}')
        if not touching(H, T):
            # correct here
            print('NOT TOUCHING!')
            pass
        input()

    print(H.x, H.y)

