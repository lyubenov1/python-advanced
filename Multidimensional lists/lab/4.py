def column_sum1(mm):
    column_sums = [0] * m

    for i in range(n):
        for j in range(m):
            column_sums[j] += mm[i][j]

    return column_sums


def column_sum2(mm):
    column_sums = []
    for j in range(m):
        column_sums.append(0)
        for i in range(n):
            column_sums[-1] += mm[i][j]
    return column_sums


n, m = [int(x) for x in input().split(', ')]
matrix = []


for i in range(n):
    row = [int(x) for x in input().split(' ')]
    matrix.append([j for j in row])

[print(x) for x in column_sum2(matrix)]
