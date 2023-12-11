from collections import deque

try:
    bees = deque([int(x) for x in input("Enter the bees: ").split()])
    nectar = [int(x) for x in input("Enter the nectar: ").split()]
    symbols = deque([x for x in input("Enter the symbols: ").split()])
except ValueError:
    print("Invalid input. Please enter integers for bees and nectar.")
    exit()

total = 0

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '/': lambda a, b: a // b if b != 0 else 0,  # Added division by zero check
    '*': lambda a, b: a * b,
}

if len(bees) != len(nectar) or len(bees) != len(symbols):
    print("Invalid input. Lists must have the same length.")
    exit()

while bees and nectar:
    if bees[0] > nectar[-1]:
        nectar.pop()

    else:
        operation_symbol = symbols.popleft()
        total += abs(operations[operation_symbol](bees.popleft(), nectar.pop()))
        print(f"{operation_symbol} applied.")

print(f'Total honey made: {total}')

if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")