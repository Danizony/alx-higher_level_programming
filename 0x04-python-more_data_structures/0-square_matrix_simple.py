#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared_values = []

    for x in matrix:
        squared_row = [item ** 2 for item in x]
        squared_values.append(squared_row)
    return (squared_values)
