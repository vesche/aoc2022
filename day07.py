
with open('inputs/day07.txt') as f:
    data = f.read().splitlines()

from pathlib import Path
from collections import Counter
path = Path()
folders = Counter()

for line in data:
    if line.startswith('$ '):
        if 'cd' in line:
            path = path.joinpath(line.split()[-1]).resolve()
        continue

    if line.startswith('dir '):
        continue

    for p in [path, *path.parents]:
        folders[p] += int(line.split()[0])

print(sum(v for v in folders.values() if v <= 100000))

root = folders[Path('/')]
print(min(v for v in folders.values() if v >= root - 70000000+30000000))

