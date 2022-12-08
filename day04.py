
with open('inputs/day04.txt') as f:
    data = f.read().splitlines()

def check_p2(s1, s2):
    for n1 in s1:
        for n2 in s2:
            if n1 == n2:
                return True

p1, p2 = 0, 0
for line in data:
    x, y = line.split(',')
    a, b = map(int, x.split('-'))
    c, d = map(int, y.split('-'))
    s1 = set(range(a,b+1))
    s2 = set(range(c,d+1))
    if s1.issubset(s2) or s2.issubset(s1):
        p1 += 1
    if check_p2(s1, s2):
        p2 += 1
print(p1, p2)

