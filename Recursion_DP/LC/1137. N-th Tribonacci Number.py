"""
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

"""

# Normal recursion
def tribonacci(n):

    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

# top down
def tribonacci2(n):

    a, b, c = 0, 1, 1

    for _ in range(n-2):
        a, b, c = b, c, a + b + c
        print(a, b, c)

    return c


# with memoization
h_map = {0: 0, 1: 1, 2: 1}
def tribonacci3(n):


    if n in h_map:
        return h_map[n]
    else:
        value =  tribonacci3(n-1) + tribonacci3(n-2) + tribonacci3(n-3)
        h_map[n] = value
        return value

def tribonacci4(n):
    hmap = {0: 0, 1: 1, 2: 1}

    def trib(n):
        if n in hmap:
            return hmap[n]
        else:
            value = trib(n - 1) + trib(n - 2) + trib(n - 3)
            hmap[n] = value
            return value

    return trib(n)

print(tribonacci3(500))
