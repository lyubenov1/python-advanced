a = [[2, 4, 6, 8],
     [1, 3, 5, 7],
     [8, 6, 4, 2],
     [7, 5, 3, 1]]

for list in range(len(a)):
    for element in range(len(a[list])):
        print(a[list][element], end=" ")
    print()
