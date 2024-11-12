"""
136. Single Number
https://leetcode.com/problems/single-number/description/
"""

"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

I can make set and then make sum of it, then i can make rest from division to that summ that will
give me something for example: 2 + 2 + 1 = 5 % (2 + 1) = 1. this will not work as I thought

I just can make dict and filter through it but this will take space and time to filter and time to
iterate.

I can append set and if it is in set then remove from it.

I iterate through list so it's basically instant, then i lookup num in set whick is O(1), and then
I add or remove which is also O(1), so it's O(2*n) ~ O(n). Worst case for space is O(n/2) ~ O(n)
"""

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        temp_set = set()
        for num in nums:
            if num in temp_set:
                temp_set.remove(num)
            else:
                temp_set.add(num)
        return list(temp_set)[0]