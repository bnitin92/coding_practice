# is palindrome

# recursively

def palindrome(s):

    if len(s) == 0:
        return True

    return isPalindrome(s, 0, len(s)-1)

def isPalindrome(s, start, end):

    # base case 1 if it reaches 1 element in odd sceanrio
    if start == end:
        return True

    # base case 2 if it isn't palindrome
    if s[start] != s[end]:
        return False

    if start < end:
        return isPalindrome(s, start + 1, end - 1)

    return True


print(palindrome("nitin"))