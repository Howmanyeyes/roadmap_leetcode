"""
349. Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/description/?envType=problem-list-v2&envId=hash-table
"""

"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element 
in the result must be unique and you may return the result in any order.

Why not use set? We can make lists into sets to get rid of reappearing elements and then make
new list with only encountarable values. Solution is good, but not the best, as python offers
build-in tool to get intersection of sets:
>>> a = {1,2,3}
>>> b = {1,1,1}
>>> a & b
{1} 

It would be good if I could use it elsewhere, but for now I will try to remember that boolean 
algebra applies to sets.
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1, nums2 = set(nums1), set(nums2)
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        decision_dict = {
            "nums2": nums2,
            "nums1": nums1
        }
        if len_nums1 < len_nums2:
            min_list_nums = decision_dict["nums1"]
            other_set = decision_dict["nums2"]
        else:
            min_list_nums = decision_dict["nums2"]
            other_set = decision_dict["nums1"]
        return [num for num in min_list_nums if num in other_set]
        
if __name__ == '__main__':
    n1 = [4,9,5]
    n2 = [9,4,9,8,4]
    s = Solution()
    s.intersection(n1, n2)