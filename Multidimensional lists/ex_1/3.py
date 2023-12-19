n, m = list(map(int, input().split()))

matrix = [input().split(' ') for i in range(n)]
count = 0
square_2x2 = None

for i in range(len(matrix) - 1):
    for j in range(len(matrix[0]) - 1):
            if matrix[i][j] == matrix[i][j+1] == matrix[i+1][j] == matrix[i+1][j+1]:
                count += 1

print(count)