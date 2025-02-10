"""
169. Majority Element
https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
"""

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        devider = len(nums) // 2
        return nums[devider]
        