# Binary search using recursion

"""

input: [-1, 2, 4, 5, 6]  find = 4
return 2

find = 7
return None

"""

def binarySearch(arr, num):

    first_1 = 0
    last_1 = len(arr)- 1
    # mid = (last - first) // 2

    def helpersearch(first, last, num):

        if first == last:
            if arr[first] == num:
                return first
            else:
                return None

        mid = ((last - first) // 2) + first

        if arr[mid] == num:
            return mid
        else:
            if num < arr[mid]:
                last = mid - 1
            elif num > arr[mid]:
                first = mid + 1

            return helpersearch(first, last, num)

    res = helpersearch(first_1, last_1, num)

    return res

print(binarySearch([-1, 2, 4, 5, 6, 7], 8))