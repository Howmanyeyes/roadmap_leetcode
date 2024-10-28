""" Hash Table problem #1"""

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

list is the input len < 10^4, it's values are in the range of -10^9 to 10^9,
target is in range of -10^9 to 10^9

most of time | target | < max(list) probably? Filter numbers that are too big

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Great, because we can make only one pass per pass, so we hav maximum of len(list) ! combinatios, but it's still too much to brute force


You can return the answer in any order.

Suggestion that we can sort and go backwards?
"""

class Solution:
    """Solution class"""
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Solution itself"""
        hash_map = {}
        for i in range(len(nums)):
            hash_map.update({nums[i]: i})
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hash_map.keys() and hash_map[compliment] != i:
                return [i, hash_map[compliment]]
if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3, 2, 4], 6))
    # Done, made progress with hash tables :^)
