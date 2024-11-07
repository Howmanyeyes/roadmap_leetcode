'''14. Longest Common Prefix
Solved
Easy
Topics
Companies
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prfx = strs[0]
        for i in strs:
            if i == "":
                return ""
            for j in range(len(i)):
                if len(prfx) - 1 < j  or prfx[j] != i[j]:
                    prfx = prfx[:j]
                    break
                elif len(i) == 1 or (len(i) < len(prfx) and j == len(i)-1):
                    prfx = i
                    break
        return prfx
                        