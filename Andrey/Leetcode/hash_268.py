"""
268. Missing Number
https://leetcode.com/problems/missing-number/description/?envType=problem-list-v2&envId=hash-table
"""

"""
Given an array nums containing n distinct numbers in the range [0, n], return 
the only number in the range that is missing from the array.

Here we can get summ of all numbers in array and see if it matches summ of all numbers in range.
But this probably will be inefficient, let's try nevertheless.

That worked wonders!
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(range(len(nums) + 1)) - sum(nums)