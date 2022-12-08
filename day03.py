
from string import ascii_letters

with open('inputs/day03.txt') as f:
    data = f.read().splitlines()

p1 = 0
for line in data:
    length = len(line)//2
    c1, c2 = line[:length], line[length:]
    char = list(set(c1).intersection(c2))[0]
    p1 += ascii_letters.index(char)+1
print(p1)

p2 = 0
for group in zip(*(iter(data),) * 3):
    char = list(set(group[0]).intersection(group[1]).intersection(group[2]))[0]
    p2 += ascii_letters.index(char)+1
print(p2)
