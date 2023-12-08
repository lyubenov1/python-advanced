mm = [
 [10, 2, 21, 4],
 [5, 20, 41, 9],
 [6, 2, 4, 99],
]

n = len(mm)
m = len(mm[0])

result = 0

for row_index in range(n):
    for column_index in range(m):
        result += mm[row_index][column_index]

print(result)
