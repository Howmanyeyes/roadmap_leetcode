"""
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/description/?envType=problem-list-v2&envId=hash-table
"""

"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

It is possible to iterate over array and add element to set if there's no such element in set. And
return True if there's such element.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)
        return False
        