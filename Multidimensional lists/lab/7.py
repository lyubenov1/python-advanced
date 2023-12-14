n, m = map(int, input().split(', '))
matrix = [list(map(int, input().split(', '))) for i in range(n)]

max_sum = float('-inf')
max_submatrix = None
for i in range(n - 1):
    for j in range(m - 1):
        current_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]

        if current_sum > max_sum:
            max_sum = current_sum
            max_submatrix = [
                [matrix[i][j], matrix[i][j + 1]],
                [matrix[i + 1][j], matrix[i + 1][j + 1]]
            ]

for i in max_submatrix:
    print(' '.join(map(str, i)))

print(max_sum)
