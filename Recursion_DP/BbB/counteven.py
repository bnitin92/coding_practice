# counting even numbers in array using recursion

# building result as we return
def countEven(arr):
    return countEvenhelper(arr, 0)


def countEvenhelper(arr, i):
    if i >= len(arr):
        return 0
    result = countEvenhelper(arr, i + 1)
    if arr[i] % 2 == 0:
        result += 1
    return result


#print(countEven([1, 2, 3, 4, 5, 6, 8]))

# passing variable
def countEvenPassed(arr):
    result = 0
    helperfun(arr, 0, result)
    return result

def helperfun(arr, i, result):
    if i >= len(arr):
        return
    if arr[i] % 2 == 0:
        result += 1
    helperfun(arr, i+1, result)

print(countEvenPassed([1, 2, 3, 4, 5, 6, 8]))