def isSquare(matrix):
    size = len(matrix)

    if size <= 0:
        return False

    for row in matrix:
        if len(row) != size:
            return False

    return True

def validateMatrixValues(matrix):
    size = len(matrix)
    values = []

    for row in matrix:
        for value in row:
            if not isinstance(value, int) or value < 1 or value > size * size:
                return False
            values.append(value)

    if len(set(values)) != size * size:
        return False

    return True

def getMagicSum(matrix):
    return sum(matrix[0])

def checkRows(matrix, magic_sum):
    for row in matrix:
        if sum(row) != magic_sum:
            return False

    return True

def checkColumns(matrix, magic_sum):
    for col in zip(*matrix):
        if sum(col) != magic_sum:
            return False

    return True

def checkDiagonals(matrix, magic_sum):
    size = len(matrix)
    diagonal_1 = 0
    diagonal_2 = 0

    for i in range(size):
        diagonal_1 += matrix[i][i]
        diagonal_2 += matrix[i][size - i - 1]

    return diagonal_1 == magic_sum and diagonal_2 == magic_sum

def IsMagicSquare(matrix):
    size = len(matrix)
    # Check if our matrix is square shaped.
    if not isSquare(matrix):
        return False

    # Check if values are distinct and in the range of 1 to n^2.
    if not validateMatrixValues(matrix):
        return False

    # Get the magic sum of the matrix as base value.
    magic_sum = getMagicSum(matrix)

    # Check if all rows have the same sum i.e. magic sum.
    if not checkRows(matrix, magic_sum):
        return False

    # Check if all columns have the same sum i.e. magic sum.
    if not checkColumns(matrix, magic_sum):
        return False

    # Check if both diagonals have the same sum i.e. magic sum.
    if not checkDiagonals(matrix, magic_sum):
        return False

    return True

# Example given in the problem statement
test_matrix_1 = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]
print(IsMagicSquare(test_matrix_1))  # Expected: True

# Another known 3x3 Magic Square
test_matrix_2 = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]
print(IsMagicSquare(test_matrix_2))  # Expected: True

# A non-magic square (incorrect sums)
test_matrix_3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(IsMagicSquare(test_matrix_3))  # Expected: False

# A square missing distinctness (repeated number)
test_matrix_4 = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 3]  # repeated 3 instead of 8
]
print(IsMagicSquare(test_matrix_4))  # Expected: False

# A non-square matrix
test_matrix_5 = [
    [2, 7, 6],
    [9, 5, 1]
]
print(IsMagicSquare(test_matrix_5))  # Expected: False

# Empty matrix
test_matrix_6 = []
print(IsMagicSquare(test_matrix_6))  # Expected: False