#!/usr/bin/python3
"""function that computes the square value ofa matrix"""
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (new_matrix)
