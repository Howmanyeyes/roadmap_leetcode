"""
496. Next Greater Element I
https://leetcode.com/problems/next-greater-element-i/description/?envType=problem-list-v2&envId=hash-table&difficulty=EASY
"""

"""
The next greater element of some element x in an array is the first greater element that is to the
right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2,
where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the
next greater element of nums2[j] in nums2. If there is no next greater element, then the answer
for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as
described above.

Time is up :( This solution is not done to the end and it's terrible, i should use hash maps
somehow
"""

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums1:
            good_val = False
            right_nums = nums2[nums1.index(num) + 1:]
            for num2 in right_nums:
                if num2 > num:
                    res.append(num2)
                    good_val = True
                    break
            if not good_val:
                res.append(-1)
                good_val = False
        return res