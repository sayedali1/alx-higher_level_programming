#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [list(map(lambda v: v**2, submatrix)) for submatrix in matrix]
