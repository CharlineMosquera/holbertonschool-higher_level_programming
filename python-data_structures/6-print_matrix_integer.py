#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for fila in matrix:
        for value in fila:
            if value % 3 == 0:
                print(value)
            else:
                print(value, end=' ')
