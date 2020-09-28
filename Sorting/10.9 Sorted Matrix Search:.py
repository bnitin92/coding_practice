"""
Sorted Matrix Search: Given an M x N matrix in which each row and each column is sorted in ascending
order, write a method to find an element.

"""

import numpy as np
from bisect import bisect_left


def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1


# returns the element from bottom most row
def sorted_matrix_search(matrix, value):
    matrix = np.array(matrix)
    # print(matrix)
    first_column = matrix[:, 0]
    # print(first_column)

    # element_index = bisect_left(first_column, value)
    # if element_index != len(first_column) and first_column[element_index] == value:
    #     return element_index
    element_index = BinarySearch(first_column, value)
    # print(element_index)
    if element_index != -1:
        return element_index, 0
    else:
        # selecting row index less than value
        row_index = np.argmin(value - first_column[first_column < value])

    while row_index >= 0:
        i = BinarySearch(matrix[row_index], value)
        if i != -1:
            return row_index, i
        else:
            row_index -= 1

    return "Not Found"


m = [[-6, -5, -3, -1, 0],
     [-1, 0, 1,	2, 3],
     [1, 2, 2, 4, 5],
     [2, 2, 4, 5, 6],
     [4, 5,	6, 7, 8],
     [6, 7, 8, 9, 10],
     [10, 11, 12, 13, 14]]

print(sorted_matrix_search(m, -1))