
with open('inputs/day12.txt') as f:
    data = f.read().splitlines()

from string import ascii_lowercase

grid = []
for line in data:
    li = []
    for c in line:
        if c.islower():
            li.append(ascii_lowercase.index(c))
        else:
            li.append(c)
    grid.append(li)

def get_coords(letter):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == letter:
                return (x, y)

coord_start = get_coords('S')
coord_end = get_coords('E')
dirs = [(-1,0), (1,0), (0,1), (0,-1)]

max_x = len(grid[0])
max_y = len(grid)
solutions = []

def find_paths_recursive(current_path):
    print(len(current_path))
    last_cell = current_path[-1]

    for x, y in dirs:
        dx = last_cell[0] + x
        dy = last_cell[1] + y

        # outside grid
        if dx<0 or dx>=max_x or dy<0 or dy>=max_y:
            continue

        cell_v_now = grid[dy][dx]
        cell_v_last = grid[last_cell[1]][last_cell[0]]

        if cell_v_now == 'S':
            solutions.append(current_path_copy)
            continue

        # travel allowed?
        #if cell_v_last == 'E':
        #    print('hit 0')
        #    cell_v_last = cell_v_now
        if type(cell_v_now) == str or type(cell_v_last) == str:
            continue
        if not (cell_v_now + 1 >= cell_v_last):
            continue
        if (dx, dy) in current_path:
            continue

        # Add cell to current path
        current_path_copy = current_path.copy()
        current_path_copy.append((dx, dy))

        # Create new current_path array for every direction
        find_paths_recursive(current_path_copy)

    return solutions

for x, y in dirs:
    coord_x, coord_y = coord_end
    current_path = [(coord_x+x, coord_y+y)]
    print(find_paths_recursive(current_path))

#current_path = [coord_end]
#print(find_paths_recursive(current_path))
