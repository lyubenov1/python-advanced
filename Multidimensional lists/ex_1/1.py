n = int(input())

matrix = [list(map(int, input().split(', '))) for i in range(n)]

primary = [matrix[j][j] for j in range(len(matrix[0]))]
secondary = [matrix[j][n - j - 1] for j in range(len(matrix[0]))]


print(f'Primary diagonal: {", ".join(map(str, primary))}. Sum: {sum(primary)}')
print(f'Secondary diagonal: {", ".join(map(str, secondary))}. Sum: {sum(secondary)}')

