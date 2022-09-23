#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for elem in row:
            if row.index(elem) < len(row) - 1:
                print("{}".format(elem), end=' ')
            else:
                print("{}".format(elem), end='')
        print("")
