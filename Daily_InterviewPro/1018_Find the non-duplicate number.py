"""
Given a list of numbers, where every number shows up twice except for one number, find that one number.

"""

def singleNumber(nums):
    # Fill this in.
    nums.sort()

    for i in range(0, len(nums), 2):
        if i == len(nums):
            return nums[i]
        else:
            if nums[i] != nums[i+1]:
                return nums[i]


print(singleNumber([4, 3, 2, 4, 1, 3, 2]))