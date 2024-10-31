"""
169. Majority Element
https://leetcode.com/problems/majority-element/description/?envType=problem-list-v2&envId=hash-table1
"""

"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

"""

class Solution(object):
    def majorityElement(self, nums: list) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_map = {}
        nums_set = set()
        for num in nums:
            if num not in nums_set:
                nums_set.add(num)
                hash_map[num] = 0
            hash_map[num] += 1
        biggest = 0
        for res in hash_map.items():
            if res[1] > biggest:
                biggest = res[1]
                solution = res[0]
        return solution
if __name__ == '__main__':
    nums = [3,2,3,2,2]
    s = Solution()
    print(s.majorityElement(nums))
