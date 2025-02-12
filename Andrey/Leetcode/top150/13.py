"""
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-interview-150
"""

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        buffer = [1]*len(nums)
        answ = [1]*len(nums)
        
        curr_product = 1
        for i in range(1, len(nums)):
            curr_product *= nums[i - 1]
            answ[i] = curr_product
        
        curr_product = 1
        for i in range(len(nums) - 2, -1, -1):
            curr_product *= nums[i + 1]
            buffer[i] = curr_product
        
        for i in range(len(answ)):
            answ[i] *= buffer[i]
        
        return answ

# 4
# [1,2,3,4]
# [1,1,1,1] answ
# [1,1,1,1] buff
# answ => [1, 1, 2, 6]
# buff => [24, 12, 4, 1]
