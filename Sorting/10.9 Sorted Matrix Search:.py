"""
Sorted Matrix Search: Given an M x N matrix in which each row and each column is sorted in ascending
order, write a method to find an element.

"""

import numpy as np
from bisect import bisect_left


def sorted_matrix_search(matrix, value):
    matrix = np.array(matrix)
    #print(matrix)
    first_column = matrix[:, 0]
    #print(first_column)

    element_index = bisect_left(first_column, value)
    if element_index != len(first_column) and first_column[element_index] == value:
        return element_index
    else:
        print(np.min(value - first_column))




m = [[-6, -5, -3, -1, 0],
     [-1, 0, 1,	2, 3],
     [1, 2, 2, 4, 5],
     [2, 2, 4, 5, 6],
     [4, 5,	6, 7, 8],
     [6, 7, 8, 9, 10],
     [10, 11, 12, 13, 14]]

sorted_matrix_search(m, 9)