# find all possible anagrams

"""

Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string.
 Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

For example , the list of all anagrammatic pairs is  at positions  respectively.


"""
from collections import Counter

def sherlockAndAnagrams(s):
    arr = []
    # all possible strings
    for i in range(1, len(s)):
        for j in range(0, len(s)- i + 1):
            arr.append("".join(sorted(s[j:j+i])))

    count = Counter(arr)
    #return v > 1 for k, v in count.items():

print(sherlockAndAnagrams("mom"))


