from ast import literal_eval

with open('inputs/day13.txt') as f:
    data = f.read().split('\n\n')

def run(a, b):
    match a, b:
        case int(), int():
            return a - b
        case int(), list():
            return run([a], b)
        case list(), int():
            return run(a, [b])
        case list(), list():
            for x, y in zip(a, b):
                if (r := run(x, y)) != 0:
                    return r
            return run(len(a), len(b))

packets = [[[2]], [[6]]]

p1 = 0
for i, d in enumerate(data):
    a_raw, b_raw = d.split()
    a = literal_eval(a_raw)
    b = literal_eval(b_raw)
    packets += [a, b]
    if run(a, b) <= 0:
        p1 += i+1

print(p1)

from functools import cmp_to_key

packets = sorted(packets, key=cmp_to_key(run))
print((packets.index([[2]])+1)*(packets.index([[6]])+1))

