"""
350. Intersection of Two Arrays II
https://leetcode.com/problems/intersection-of-two-arrays-ii/description/?envType=problem-list-v2&envId=hash-table
"""

"""
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays
and you may return the result in any order.

probably can just iterate through smaller list and just replace already seen vals, but this will be
very inefficient as search in list will be made several times, so worst case it would be something
like O(max(n, m) * log(max(n, m))). Time is up
"""

