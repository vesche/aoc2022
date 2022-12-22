
with open('inputs/day11.txt') as f:
    data = f.read().strip().split('\n\n')

import re

pattern = r"""Monkey [0-9]:
  Starting items: (?P<items>[0-9, ]*)
  Operation: new = (?P<op>[a-z0-9+\-\*\/= ]*)
  Test: divisible by (?P<test>[0-9]*)
    If true: throw to monkey (?P<if_true>[0-9])
    If false: throw to monkey (?P<if_false>[0-9])"""

monkeys = []
for d in data:
    m = re.match(pattern, d)
    md = m.groupdict()
    md['items'] = list(map(int, md['items'].split(', ')))
    md['test'] = int(md['test'])
    md['if_true'] = int(md['if_true'])
    md['if_false'] = int(md['if_false'])
    md['inspected'] = 0
    monkeys.append(md)

for _ in range(20):
    for monkey in monkeys:
        for item in monkey['items']:
            monkey['inspected'] += 1
            worry = eval(monkey['op'].replace('old', str(item)))
            worry = worry // 3
            if worry % monkey['test'] == 0:
                monkeys[monkey['if_true']]['items'].append(worry)
            else:
                monkeys[monkey['if_false']]['items'].append(worry)
        monkey['items'] = []

a, b = sorted([i['inspected'] for i in monkeys])[::-1][:2]
print(a*b)

