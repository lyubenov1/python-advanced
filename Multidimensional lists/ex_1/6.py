def is_valid_coordinates(matrix, coordinates):
    for list1 in coordinates:
        row, col = list1
        if not (0 <= row < len(matrix) and 0 <= col < len(matrix[0])):
            return False
    return True


n, m = list(map(int, input().split()))
matrix = [input().split() for i in range(n)]
command = input()

while command != 'END':
    command = command.split()
    coordinates = [(int(command[i]), int(command[i + 1])) for i in range(1, len(command) - 1, 2)]
    if command[0] == 'swap' and len(command) == 5 and is_valid_coordinates(matrix, coordinates):
        i1, j1, i2, j2 = [int(x) for x in command[1:]]
        matrix[i1][j1], matrix[i2][j2] = matrix[i2][j2], matrix[i1][j1]

        for i in matrix:
            print(' '.join(map(str, i)))

    else:
        print('Invalid input!')

    command = input()
