def isSquare(matrix):
    size = len(matrix)

    if size <= 0:
        return False

    for row in matrix:
        if len(row) < size:
            return False

    return True

def validateMatrixValues(matrix):
    size = len(matrix)
    values = []

    for row in matrix:
        for value in row:
            if not isinstance(value, int) or value < 1 or value > size*size:
                return False
            values.append(value)

    if len(set(values)) != size*size:
        return False

    return True

def IsMagicSquare(matrix):
    size = len(matrix)
    # Check if our matrix is square shaped.
    if not isSquare(matrix):
        return False

    # Check if values are distinct and in the range of 1 to n^2.
    if not validateMatrixValues(matrix):
        return False

    return True

test_matrix_1 = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

print(IsMagicSquare(test_matrix_1))