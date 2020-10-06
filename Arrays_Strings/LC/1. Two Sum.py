# finding if the sum is equal to the target

"""
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.
"""


"""
example
nums = [2,7,11,15], target = 9
result = [0,1]
"""

from collections import defaultdict


# O(n^2)
# def twoSum(nums, target):
#
#    # res = []
#
#     for i in range(len(nums)-1):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i,j]
#

"""
if i have a hash table i can find by

for number in list
target - number find in hash table

"""

# O(n+n) as takes time to convert to hash table
def twoSum2(nums, target):

   hashtab = dict(zip(nums, [i for i in range(len(nums))]))
   #print(hashtab)
   for i,vali in enumerate(nums):
       found = hashtab.get(target-vali)
       if found and (i != hashtab[target-vali]):
           return [i,found]

#
def twoSum3(nums, target):

    list_dict = {}
    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in list_dict:
            return list_dict[compliment], i
        list_dict[nums[i]] = i

print(twoSum3([2,7,11,15], 9))