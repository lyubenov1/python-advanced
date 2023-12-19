def generate_palindrome_matrix(rows, cols):
    matrix = []

    for i in range(rows):
        row = []
        for j in range(cols):
            first_letter = chr(ord('a') + i)
            middle_letter = chr(ord('a') + j + i)
            palindrome = f"{first_letter}{middle_letter}{first_letter}"
            row.append(palindrome)
        matrix.append(row)

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))


rows, cols = list(map(int, input().split()))

palindrome_matrix = generate_palindrome_matrix(rows, cols)
print_matrix(palindrome_matrix)
