def is_valid(matrix, row, col):
    if row >= len(matrix) or col >= len(matrix[0]) or row < 0 or col < 0:
        return False
    return True


matrix = [[int(x) for x in input().split()] for y in range(int(input()))]

while True:
    command = input()
    if command == 'END':
        break

    command = command.split()
    operation = command[0]

    row, col, value = map(int, command[1:])

    if not is_valid(matrix, row, col):
        print('Invalid coordinates')
        continue

    elif operation == 'Add':
            matrix[row][col] += value

    elif operation == 'Subtract':
            matrix[row][col] -= value

for row in matrix:
    print(' '.join(map(str, row)))
