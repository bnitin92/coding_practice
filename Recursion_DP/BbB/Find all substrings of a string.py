# find all substrings

# Concept (pick or dont pick)
res = []

def substring(s):
    findSubstring(s, "")

    return res

# see notebook for the diagram

def findSubstring(s, ans):

    if len(s) == 0:
        res.append(ans)
        return

    findSubstring(s[1:], ans + s[0]) #picking firs element

    findSubstring(s[1:], ans) # not picking first element

print(substring("abc"))
