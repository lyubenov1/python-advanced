rows, columns = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

best_sum = float('-inf')
start_row = 0
start_column = 0

for row in range(rows - 2):
    for column in range(columns - 2):
        current_sum = matrix[row][column] + matrix[row][column + 1] + matrix[row + 1][column] + matrix[row][column + 2] + \
                matrix[row + 1][column + 1] + matrix[row + 1][column + 2] + matrix[row + 2][column] + matrix[row + 2][column + 1] + \
                matrix[row + 2][column + 2]
        if current_sum > best_sum:
            best_sum = current_sum
            start_row = row
            start_column = column


print(f'Sum = {best_sum}')
print(f'{matrix[start_row][start_column]} {matrix[start_row][start_column + 1]} {matrix[start_row][start_column + 2]}')
print(f'{matrix[start_row + 1][start_column]} {matrix[start_row + 1][start_column + 1]} {matrix[start_row + 1][start_column + 2]}')
print(f'{matrix[start_row + 2][start_column]} {matrix[start_row + 2][start_column + 1]} {matrix[start_row + 2][start_column + 2]}')

