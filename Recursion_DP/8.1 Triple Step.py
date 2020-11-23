"""
A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the stairs.

"""

def tripleStep(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    else:
        return tripleStep(n-3) + tripleStep(n-2) + tripleStep(n-1)
        # We multiply the values when it's "we do this then this:' We add them when it's "we do this or this:'


print(tripleStep(3))