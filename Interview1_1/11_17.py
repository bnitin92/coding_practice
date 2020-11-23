"""
Given a set of integers, find the maximum sum of values that are under a weight W.  
e.g.  vals = [ 7, 10, 4, 3, 17, 8 ] W = 5  Solution: 4  OR  
vals = [ 7, 10, 4, 3, 17, 8 ] W = 19   solution: 18  
BONUS: Bonus 1: Return the maximum subset under the given weight 
Bonus 2: Ensure that no sub problem is calculated more than once  
"""

"""
Sol
base: if index >= len(val) or if sum > W:
return 0

max_val

recursive step:
    value1 = 0
    value1 = sum[set] + max_val(val[1:], set, W, index) #
    value2 = max_val(val, set, W, index+1)
    
    return max(value1, value2)
"""

def maximum_value(val, W):
    return max_possible(val,[], W, 0)

def max_possible(val,combination, W, index):
    # base case
    if index >= len(val) or sum(combination) <= W:
        return 0

    combination = combination.append(val[index])
    # recursive step
    value1 = 0
    # value1 = val[index] + max_possible(val, combination.append(val[index]), W, index+1)
    # value1 = sum(combination) + max_possible(val, combination.append(val[index]), W, index+1)
    value2 = max_possible(val, combination, W, index+1)