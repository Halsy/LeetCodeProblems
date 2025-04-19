#=========================================================================================================================#
# Name:                                                  Harold Sy                                                        #
# Title: ............................................... two_sum.py                                                       #
# 1st Method used: ..................................... Brute Force                                                      #
# Submitted program runtime: ........................... 2276 ms                                                          #
# Beats: ............................................... 15.02%                                                           #
# Time complexity: ..................................... O(n^2)                                                           #
# 2nd Method used: ..................................... Using Dictionary map                                             #
# Submitted program runtime: ........................... 0 ms                                                             #
# Beats: ............................................... 100.00%                                                          #
# Time complexity: ..................................... O(n)                                                             #
# Difficulty: .......................................... Easy                                                             #
# Time for completion .................................. 10 minutes                                                       #
#                                                                                                                         #
# Mission: ............................................. Given an array of integers 'nums' and an integer 'target'        #
#                                                        return indices of the two numbers such that they add to 'target' #
#                                                                                                                         #
# Assumptions: ......................................... ** output has one solution meaning return only two elements      #
#                                                        ** elements must be unique                                       #
#                                                        ** elements can be in any order                                  #
#                                                                                                                         #
# Constraints: ......................................... ** 2 <= nums.length <= 10^4                                      #
#                                                        ** -10^9 <= nums[i] <= 10^9                                      #
#                                                        ** -10^9 <= target <= 10^9                                       #
#                                                        ** Only one valid answer exists                                  #
#                                                                                                                         #
# Example 1: ........................................... Input: nums = [2,7,11,15], target = 9                            #
#                                                        Output: =================================================> [0,1] #
#                                                        Explanation: nums[0] + nums[1] == 9, we return [0,1]             #
#                                                                                                                         #
# Example 2: ........................................... Input: nums = [3,2,4], target = 6                                #
#                                                        Output: =================================================> [1,2] #
#                                                                                                                         #
# Example 3: ........................................... Input: nums = [3,3], target = 6                                  #
#                                                        Output: =================================================> [0,1] #
#                                                                                                                         #
# Provided by leetcode ................................. class Solution (object):                                         #
#                                                            def twoSum(self, nums, target):                              #
#                                                                """                                                      #
#                                                                :type nums: List[int]                                    #
#                                                                :type target: int                                        #
#                                                                :rtype: List[int]                                        #
#                                                                """                                                      #
#                                                                                                                         #
#=========================================================================================================================#
#                                                                                                                         #
# Original code submitted:                                                                                                #
#                                                                                                                         #
# class Solution(object):                                                                                                 #
#    def twoSum(self, nums, target):                                                                                      #
#        """                                                                                                              #
#        :type nums: List[int]                                                                                            #
#        :type target: int                                                                                                #
#        :rtype: List[int]                                                                                                #
#        """                                                                                                              #
#        final_list = []                                                                                                  #
#        for index1 in range(0,len(nums)):                                                                                #
#            for index2 in range(index1 + 1,len(nums)):                                                                   #
#                if nums[index1] + nums[index2] == target:                                                                #
#                    final_list.extend([index1,index2])                                                                   #
#        return final_list                                                                                                # 
#                                                                                                                         #
# list_of_numbers1 = [2,7,11,15]                                                                                          #
# list_of_numbers2 = [3,2,4]                                                                                              # 
# list_of_numbers3 = [3,3]                                                                                                #
#                                                                                                                         #
# target1 = 9                                                                                                             #
# target2 = 6                                                                                                             #
# target3 = 6                                                                                                             #
#                                                                                                                         #
# my_solution = Solution()                                                                                                # 
# print(my_solution.twoSum(list_of_numbers1, target1))                                                                    #
# print(my_solution.twoSum(list_of_numbers2, target2))                                                                    #
# print(my_solution.twoSum(list_of_numbers3, target3))                                                                    # 
#                                                                                                                         #
#=========================================================================================================================#
#                                                                                                                         #
# Things learned from this problem: .................. ** instantiating a solution class requires                         #
#                                                         my_solution = Solution()                                        #
#                                                      ** .append only adds one item at a time to a list                  #
#                                                      ** .extend adds multiple items at a time to a list and flattens    #
#                                                         list.extend([item1, item2, ect])                                #
#                                                      ** a better way to do the second loop is to start it at the same   #
#                                                         number as the first loop but + 1, that way the second loop      #
#                                                         does not start at zero again and is ahead by one and still ends #
#                                                         at the correct index! for index2 in range)index1+1, len(nums)): #
#                                                      ** just a list could have been returned like this:                 #
#                                                         return [ num[index1], num[index2] ]                             #
#                                                                                                                         #
#=========================================================================================================================#

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

list_of_numbers1 = [2,7,11,15]
list_of_numbers2 = [3,2,4]
list_of_numbers3 = [3,3]

target1 = 9
target2 = 6
target3 = 6

my_solution = Solution()
print(my_solution.twoSum(list_of_numbers1, target1))
print(my_solution.twoSum(list_of_numbers2, target2))
print(my_solution.twoSum(list_of_numbers3, target3))



