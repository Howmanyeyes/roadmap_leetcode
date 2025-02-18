"""
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150
"""

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

можно пройтись по минимальной длине слова и  смотреть на буквы во всех словах, в худшем случае это 
n^2, однако чтобы сделать лучше я не знаю как, надо попробовать ореализовать сначала
"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        set_letters = set()
        prefix = []
        for i in range(min([len(x) for x in strs])):
            prefix.append(strs[0][i])
            for string in strs:
                if string[i] == prefix[-1]:
                    pass
                else:
                    return "".join(prefix[:-1])
            
        return "".join(prefix)