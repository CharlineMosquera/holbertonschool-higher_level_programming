#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for fila in range(len(matrix)):
        for value in range(len(matrix[fila])):
            print("{:d}".format(matrix[fila][value]), end="")
            if (value < len(matrix[fila]) - 1):
                print(" ", end="")
        print("")
