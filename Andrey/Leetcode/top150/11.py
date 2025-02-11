"""
274. H-Index
https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150
"""

"""
Given an array of integers citations where citations[i] is the number of citations a researcher
received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value
of h such that the given researcher has published at least h papers that have each been cited at
least h times.
"""

class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort()
        max_h = 0
        for i in range(len(citations) - 1, -1, -1):
            if citations[i] < max_h:
                break
            if citations[i] >= max_h:
                max_h = min(citations[i], len(citations) - i)
        return max_h


if __name__ == '__main__':
    s = Solution()
    print(s.hIndex([1,2,2]))