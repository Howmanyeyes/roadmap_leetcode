class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_list = nums1 + nums2
        new_list.sort()
        len_list = len(new_list)
        if len_list % 2 == 1:
            return new_list[int(len_list/2)]
        else:
            print(len_list/2-1)
            return (new_list[int(len_list/2-1)] + new_list[int(len_list/2)])/2
# код принялся. даже не верится, ибо решил, по сути, в лоб...