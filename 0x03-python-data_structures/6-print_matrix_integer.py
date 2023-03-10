#!/usr/bin/python
# A function that prints a matrix of integers
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print("{}".format(matrix[i][j]), end=' '
                      if matrix[i][j] != matrix[i][-1]
                      else '\n')
