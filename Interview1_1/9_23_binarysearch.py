# binary search without recursion

"""
I/P = sorted list and  intergers

-inf to inp

o/p - index of the first reference
None
"""

# from bisect import bisect_left

"""
Iterative step:

variables storing indices - first  last middle

while middle != 1:
1) find the middle element - len(list) // 2 
if equal then I well return the index
if value is less then middle element
#first = first
last  = middle
elseif:
first = middle
#last = last

return None

"""

def binary_search(l, val):
    first = 0        # 0
    last = len(l) - 1 # 3
    middle = len(l) // 2 # 1

    while middle > 0:
        if l[middle] == val:
            return middle
        elif l[middle] < val:
            first = middle
            middle = (last - first) // 2 + first
        else:
            last = middle
            middle = (last - first) // 2

    return None

# Test cases
"""
l1 = [-2, 3, 4, 6, 8, 10]  val= 3



"""

a = binary_search([-10, -2, 3, 4, 6, 8, 10, 19, 21], -2)

print(a)