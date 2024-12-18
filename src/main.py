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

def IsMagicSquare(matrix):
    size = len(matrix)
    # Check if our matrix is square shaped.
    if not isSquare(matrix):
        return False

    # Check if values are distinct and in the range of 1 to n^2.
    if not validateMatrixValues(matrix):
        return False

    magic_sum = getMagicSum(matrix)

    # Check if all rows have the same sum i.e. magic sum.
    if not checkRows(matrix, magic_sum):
        return False

    # Check if all columns have the same sum i.e. magic sum.
    if not checkColumns(matrix, magic_sum):
        return False



    return True

test_matrix_1 = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

print(IsMagicSquare(test_matrix_1))