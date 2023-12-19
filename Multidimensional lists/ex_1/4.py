n, m = list(map(int, input().split()))

matrix = [list(map(int, input().split(' '))) for i in range(n)]
max_sum = float('-inf')
square_3x3 = None

for i in range(len(matrix) - 2):
    for j in range(len(matrix[0]) - 2):
        current_sum = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + \
                      matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+1][j+2] + \
                      matrix[i+2][j] + matrix[i+2][j+1] + matrix[i+2][j+2]

        if current_sum > max_sum:
            max_sum = current_sum
            square_3x3 = [[matrix[i][j], matrix[i][j+1], matrix[i][j+2]],
                        [matrix[i+1][j], matrix[i+1][j+1], matrix[i+1][j+2]],
                        [matrix[i+2][j], matrix[i+2][j+1], matrix[i+2][j+2]]]

print(f'Sum = {max_sum}')
for i in square_3x3:
    print(' '.join(map(str, i)))
