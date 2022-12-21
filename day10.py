
with open('inputs/day10.txt') as f:
    data = f.read().splitlines()

X, cycle_n = 1, 1
ss, draw = [], []
sprite = [1, 2, 3]

def next_cycle():
    global cycle_n
    if cycle_n == 20 or (cycle_n-20) % 40 == 0:
        ss.append(cycle_n*X)
    if cycle_n % 40 in sprite:
        draw.append('#')
    else:
        draw.append('.')
    cycle_n += 1

for line in data:
    next_cycle()
    if line == 'noop':
        continue
    next_cycle()
    _, V = line.split()
    V = int(V)
    X += V
    sprite = [i+V for i in sprite]

print(sum(ss))
print('\n'.join([''.join(draw[n:n+40]) for n in range(0,240,40)]))

