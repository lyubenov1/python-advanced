matrix = []

row = 0
col = 0
targets = 0
targets_hit = 0
indexes = []

for a in range(5):
    row_elements = input().split()
    matrix.append(row_elements)
    for b in range(5):
        if matrix[a][b] == 'A':
            row = a
            col = b
        if matrix[a][b] == 'x':
            targets += 1


directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}


def is_valid(matrix, row, col):
    if row >= len(matrix) or col >= len(matrix[0]) or row < 0 or col < 0:
        return False
    return True


n = int(input())

for i in range(n):
    command = input().split()
    direction = command[1]

    if command[0] == 'move':
        steps = int(command[2])
        matrix[row][col] = '.'

        for y in range(steps):
            next_row, next_col = directions[direction](row, col)

            if not is_valid(matrix, next_row, next_col) or matrix[next_row][next_col] == 'x':
                break

            else:
                row, col = next_row, next_col

        matrix[row][col] = 'A'

    elif command[0] == 'shoot':
        row1, col1 = row, col
        while is_valid(matrix, row1, col1):
            row1, col1 = directions[direction](row1, col1)
            if is_valid(matrix, row1, col1):
                if matrix[row1][col1] == 'x':
                    targets_hit += 1
                    indexes.append([row1, col1])
                    matrix[row1][col1] = '.'
                    row1, col1 = directions[direction](row1, col1)
                    if targets_hit == targets:
                        break
                    continue
            else:
                continue


if targets_hit == targets:
    print(f'Training completed! All {targets} targets hit.')
else:
    print(f'Training not completed! {targets - targets_hit} targets left.')

for row in indexes:
    print(row)
