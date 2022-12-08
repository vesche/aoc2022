
with open('inputs/day01.txt') as f:
    data = f.read().splitlines()

elves = []
cals = 0
for n in data:
    if n == '':
        elves.append(cals)
        cals = 0
        continue
    cals += int(n)

print(max(elves))

import heapq
print(sum(heapq.nlargest(3, elves)))
