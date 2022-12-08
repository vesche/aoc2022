
same = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}
strat = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
}
lose = {
    'A': 'C',
    'B': 'A',
    'C': 'B',
}

with open('inputs/day02.txt') as f:
    data = f.read().splitlines()

total_p1, total_p2 = 0, 0
for line in data:
    p1, p2 = 0, 0
    i, j = line.split()

    if same[i] == j:
        p1 += 3
    if strat[i] == j:
        p1 += 6
    if j == 'X':
        p1 += 1
        p2 += ord(lose[i])-64
    if j == 'Y':
        p1 += 2
        p2 += 3
        p2 += ord(i)-64
    if j == 'Z':
        p1 += 3
        p2 += 6
        p2 += ord(strat[i])-87

    total_p1 += p1
    total_p2 += p2

print(total_p1, total_p2)

