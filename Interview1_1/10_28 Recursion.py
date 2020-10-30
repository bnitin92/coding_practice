# Power set

"""
input = set (1,2,3) or array --- integers

output = [[1], [2], [3], [1,2], [2,3], [1,3], [1,2,3]]

"""

"""
solution:

powerset(array)

return = [[]]

1 - res.append([1])
2 - res.append([1],[2],[1,2])
3 - res.append([1], [2], [3], [1,2], [2,3], [1,3],[1,2,3]) 
n - append
"""

def powerset(input):
    total = len(input)
    size = total
    res = []

    res.append(input)
    size -= 1
    powerset(input[1:])

    if len(input) ==  0:
        return
