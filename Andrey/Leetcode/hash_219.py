"""
219. Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/description/?envType=problem-list-v2&envId=hash-table
"""

"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j 
in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Maybe keep in hash map indexes and distance to previous element, so we iterate once and maybe find
answer on the way.
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = i
            else:
                if abs(i - hash_map[nums[i]]) <= k:
                    return True
                hash_map[nums[i]] = i
        
        return False