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

I can't understand myself, wtf? I can try inefficient solution with generator with if statement.

Won't work bc of repeating values, maybe make hash map of one list then iterate throug another?

My solution is O(n) but it is still effective enough to get best place
"""


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hash_map = {}
        for i in range(len(nums1)):
            if nums1[i] in hash_map:
                hash_map[nums1[i]] += 1
            else:
                hash_map[nums1[i]] = 1
        sol = []
        for x in nums2:
            if x in hash_map:
                if hash_map[x] > 0:
                    hash_map[x] -= 1
                    sol.append(x)
        return sol
    

if __name__ == '__main__':
    s = Solution()
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(s.intersect(nums1, nums2))
