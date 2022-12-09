with open('inputs/day08.txt') as f:
    data = f.read().splitlines()

width = len(data[0])
height = len(data)

def is_visible(tree, x, y):
    up, down, left, right = True, True, True, True
    v1, v2, v3, v4 = 0, 0, 0, 0

    # up
    for y_step in range(0, y)[::-1]:
        v1 += 1
        if int(data[y_step][x]) >= tree:
            up = False
            break

    # down
    for y_step in range(y+1, height):
        v2 += 1
        if int(data[y_step][x]) >= tree:
            down = False
            break

    # left
    for x_step in range(0, x)[::-1]:
        v3 += 1
        if int(data[y][x_step]) >= tree:
            left = False
            break

    # right
    for x_step in range(x+1, width):
        v4 += 1
        if int(data[y][x_step]) >= tree:
            right = False
            break

    return up or down or left or right, v1*v2*v3*v4

visible = 0
scores = []
for y, row in enumerate(data):
    for x, cell in enumerate(row):
        tree = int(cell)
        # edges
        if (x == 0) or (x == width-1) or (y == 0) or (y == height-1):
            visible += 1
            continue

        vis, score = is_visible(tree, x, y)
        if vis:
            visible += 1
        scores.append(score)

print(visible)
print(max(scores))

