crates_p1 = [
    ['G', 'D', 'V', 'Z', 'J', 'S', 'B'],
    ['Z', 'S', 'M', 'G', 'V', 'P'],
    ['C', 'L', 'B', 'S', 'W', 'T', 'Q', 'F'],
    ['H', 'J', 'G', 'W', 'M', 'R', 'V', 'Q'],
    ['C', 'L', 'S', 'N', 'F', 'M', 'D'],
    ['R', 'G', 'C', 'D'],
    ['H', 'G', 'T', 'R', 'J', 'D', 'S', 'Q'],
    ['P', 'F', 'V'],
    ['D', 'R', 'S', 'T', 'J'],
]

import copy
crates_p2 = copy.deepcopy(crates_p1)

with open('inputs/day05.txt') as f:
    data = f.read().splitlines()

for line in data:
    _, n, _, a, _, b = line.split()

    for _ in range(int(n)):
        snag = crates_p1[int(a)-1].pop()
        crates_p1[int(b)-1].append(snag)

    snag = crates_p2[int(a)-1][-int(n):]
    crates_p2[int(a)-1] = crates_p2[int(a)-1][:-int(n)]
    crates_p2[int(b)-1] += snag

def print_tops(crates):
    print(''.join([i[-1] for i in crates]))

print_tops(crates_p1)
print_tops(crates_p2)

