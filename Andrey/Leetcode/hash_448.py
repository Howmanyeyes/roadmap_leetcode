"""
448. Find All Numbers Disappeared in an Array
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/?envType=problem-list-v2&envId=hash-table&difficulty=EASY
"""

"""
Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.

Trick with sums wouldn't work this time as more than one integet might be missing.
We can make set of all existing numbers and then chack if i in range is in it

Better approach could be to make list out of difference of sets of range and set(nums)
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        set_nums = set(nums)
        return [x for x in range(1,len(nums)+1) if x not in set_nums]
        