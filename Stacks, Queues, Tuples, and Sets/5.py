from collections import deque

materials = [int(x) for x in input().split()]
values = deque([int(x) for x in input().split()])

toys = {
    'Doll': 150,
    'Wooden train': 250,
    'Teddy bear': 300,
    'Bicycle': 400,
}

crafted = {}

while materials and values:
    last_material = materials.pop()
    first_value = values.popleft()
    magic = last_material * first_value

    if last_material == 0 and first_value == 0:
        continue

    if last_material == 0:
        values.appendleft(first_value)
        continue

    if first_value == 0:
        materials.append(last_material)
        continue

    if magic < 0:
        materials.append(last_material + first_value)

    elif magic not in toys.values() and magic > 0:
        materials.append(last_material + 15)

    for key, value in toys.items():
        if magic == value:
            if key not in crafted:
                crafted[key] = 0
            crafted[key] += 1

first_condition = ('Doll', 'Wooden train')
second_condition = ('Teddy Bear', 'Bicycle')


if ('Doll' in crafted.keys() and 'Wooden train' in crafted.keys()) or ('Teddy bear' in crafted.keys() and 'Bicycle' in crafted.keys()):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    print(f'Materials left: {", ".join(map(str, reversed(materials)))}')
if values:
    print(f'Magic left: {", ".join(map(str, values))}')

for key, value in crafted.items():
    print(f'{key}: {value}')
