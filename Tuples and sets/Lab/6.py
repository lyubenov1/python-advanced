ll = list(map(int, input().split(' ')))
target = int(input())
targets = set()
values_map = {}
count = 0

for value in ll:
    count += 1
    if value in targets:
        p1 = value
        p2 = values_map[value]
        print(f'{p1} + {p2} = {target}')
    else:
        targets.add(target - value)
        values_map[target - value] = value

print(f'Iterations done: {count}')
