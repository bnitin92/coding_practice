# Consecutive Characters

"""
Given a string s, the power of the string is the maximum length of a non-empty substring
that contains only one unique character.

Return the power of the string.
"""
from collections import Counter

def maxPower(s):
    res = 1
    power = 1

    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                power += 1
            else:
                if power > res:
                    res = power
                power = 1
                break
        if power > res:
            res = power
        power = 1

    return res

print(maxPower2("leetcode"))