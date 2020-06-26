"""

Given an array of integers, return indices of the two numbers such that they 
add up to a specific target. You may assume that each input would have exactly 
one solution, and you may not use the same element twice

"""

class Solution:
    
    def twoSum(self, nums, target):
        combo_list = []                                              #create empty array for combinations from nums
        for i in range(0, len(nums)):                   
            num          = nums[i]                                   #combinations list first member
            num_idx      = i                                         #index of combination list first member
            compare_list = nums[:i] + nums[i + 1:]                   #create list of remaining combination set
            for j in compare_list:
                idx_pair = [num_idx, nums.index(j)]                  #create array of nums index pairs
                idx_pair.sort()                                      #order array pairs
                if num + j == target and idx_pair not in combo_list: #if pair sum equals target and is not in list, append
                    combo_list.append(idx_pair)
        
        for indices in combo_list:
            print(indices)
            

s = Solution()

s.twoSum([2, 7, 11, 15], 9) #[0, 1]