#!/usr/bin/python3
# A function that computes the square value of all integers of a matrix
def square_matrix_simple(matrix=[]):
    squared_list = []
    square_val = 0
    for i in matrix:
        for j in i:
            square_val = j ** 2
            squared_list.append(square_val)
    return squared_list
