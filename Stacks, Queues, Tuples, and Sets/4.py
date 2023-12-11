from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque([x for x in input().split()])
total = 0

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '/': lambda a, b: a / b if b != 0 else 0,
    '*': lambda a, b: a * b,
}

while bees and nectar:
    if bees[0] > nectar[-1]:
        nectar.pop()
    else:
        total += abs(operations[symbols.popleft()](bees.popleft(), nectar.pop()))


print(f'Total honey made: {total}')
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")