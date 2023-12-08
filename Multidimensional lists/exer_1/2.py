n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

primary = []
secondary = []

for index in range(n):
    primary.append(matrix[index][index])
    secondary.append(matrix[index][n - 1 - index])

abs_value = abs(sum(primary) - sum(secondary))
print(f'{abs_value}')
