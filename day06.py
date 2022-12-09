
with open('inputs/day06.txt') as f:
    data = f.read().strip()

def get_start(n):
    for i in range(len(data[n-1:])):
        if len(set(data[i:i+n])) == n:
            return i + n

print(get_start(4))
print(get_start(14))

