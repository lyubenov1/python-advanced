n = int(input())

matrix = [list(map(int, input().split())) for i in range(n)]

primary = [matrix[j][j] for j in range(len(matrix[0]))]
secondary = [matrix[j][n - j - 1] for j in range(len(matrix[0]))]

diff = abs(sum(primary) - sum(secondary))

print(diff)
