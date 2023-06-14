#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    for i in matrix:
        column = []
        for j in i:
            column.append(j**2)
        new_matrix.append(column)
    return new_matrix
