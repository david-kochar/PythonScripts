# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 14:56:22 2020

@author: kocha
"""

#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice

nums = [2, 7, 11, 15]

target_sum = 9

permute_list = []

'''
for i in range(0, len(nums)):
    permute_list.append([nums[i]]+nums[:i]+nums[i+1:])

print(permute_list)

for i in range(0, len(nums)):
    num = nums[i]
    compare_list = nums[:i]+nums[i+1:]
    for j in compare_list:
        if num + j == target_sum:
            permute_list.append([num, j])

print(permute_list)
'''

for i in range(0, len(nums)):
    num     = nums[i]
    num_idx = i
    compare_list = nums[:i]+nums[i+1:]
    for j in compare_list:
        idx_pair = [num_idx, nums.index(j)]
        idx_pair.sort()
        if num + j == target_sum and idx_pair not in permute_list:
            permute_list.append(idx_pair)

for indices in permute_list:
    print(indices)

'''
nums = [2, 11, 7, 15]

print(nums[1])    #11
print(nums[:1])   #every element before 11
print(nums[1+1:]) #every element starting at 7
'''

l = ['3', '1', '2']

l.sort

print(l)