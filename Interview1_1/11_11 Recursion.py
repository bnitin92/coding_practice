"""
/* Givn a rectangular path in the form of a binary matix, find the length of the
longest possible route form source to destination, by moving to only nonzero adjacent positions, i.e. 
route can be formed from positions having their value as 1. Note, there should not be any cycles in the output path.  */
"""

import numpy

M = [[1, 0, 0, 1, 0],
     [1, 1, 0, 0, 0],
     [0, 1, 1, 1, 1],
     [1, 1, 0, 1, 0],
     [1, 1, 1, 1, 0]]

#const start = [0, 0]; const target = [2,4]; 

"""
probable solution

always check the adjacent cells 
if i find 1 replace that cell wiht X in the resulting matrix
while finding if i get x 
"""

def rpath(start, target):
    result = [[0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0]]

    x = start[0]
    y = start[1]

    left = (x-1, y)
    right = (x+1, y)
    up = (x, y+1)
    down = (x, y-1)

    if M[]
    dfs()

print(rpath(0,0))

function canGoHere( i, j) {      // out of bounds     if (i < 0  || i > 4) {         return false;      // out of bounds     } else if (j < 0 || j > 4) {         return false;      // already been here     } else if (V[i][j] > 0 ) {         return false;      // no path here in the matrix     } else if (M[i][j] === 0) {         return false;     }      return true; }