X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# iterate through rows
for row in range(len(X)):

    # iterate through columns
    for column in range(len(X[0])):
        result[row][column] = X[row][column] + Y[row][column]


Add_result = [[X[row][column] + Y[row][column]
               for column in range(len(X[0]))]
               for row in range(len(X))]

for r in result:
    print(r)

print(Add_result)

X = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# iterate through rows
for i in range(len(X)):
    # iterate through columns
    for j in range(len(X[0])):
        result[j][i] = X[i][j]

for r in result:
    print(r)

