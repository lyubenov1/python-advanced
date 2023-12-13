def get_primary_diagonal_sum(matrix):
    n = len(matrix)
    return sum(matrix[i][i] for i in range(n))


def get_secondary_diagonal(matrix):
    n = len(matrix)
    return sum(matrix[i][n - i - 1] for i in range(n))


n = int(input())

matrix = []

for _ in range(n):
    matrix.append(
        [int(x) for x in input().split(' ')]
    )

print(get_primary_diagonal_sum(matrix))
#print(get_secondary_diagonal(matrix))