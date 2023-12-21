def is_outside(matrix, row, col):
    if row >= len(matrix) or col >= len(matrix[0]) or row < 0 or col < 0:
        return True
    return False


size = int(input())
matrix = []

alice_row = 0
alice_col = 0
quantity = 0

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == 'A':
            alice_row = row
            alice_col = col
    matrix.append(row_elements)


directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}


success_condition = False
fail_condition = False


while True:
    command = input()
    row, col = directions[command](alice_row, alice_col)

    if is_outside(matrix, row, col):
        matrix[alice_row][alice_col] = '*'
        fail_condition = True
        break

    if matrix[row][col] == 'R':
        matrix[alice_row][alice_col] = '*'
        matrix[row][col] = '*'
        fail_condition = True
        break

    if str(matrix[row][col]).isdigit():
        quantity += int(matrix[row][col])

        if quantity >= 10:
            matrix[alice_row][alice_col] = '*'
            matrix[row][col] = '*'
            success_condition = True
            break

    matrix[alice_row][alice_col] = '*'
    alice_row, alice_col = row, col


if success_condition:
    print('She did it! She went to the party.')
elif fail_condition:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(*row, sep=' ')
