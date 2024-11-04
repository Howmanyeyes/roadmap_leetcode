"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=problem-list-v2&envId=hash-table&difficulty=MEDIUM
"""

"""
Given a string s, find the length of the longest substring without repeating characters.
A substring is a contiguous non-empty sequence of characters within a string.

I can iterate through every letter and map out it's subsring, then find longest.
Works but comedically inefficient

Much better approach is to use 2 pointers and move them as worm moves:
move right part as far as possible -> move left part as long as nessesary -> repeat

Apperantely this solution is good enough to get into top 30%, but there still are methods that i am
unable to comprehand in this state
"""
"""
First solution

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        :type s: str
        :rtype: int
        
        max_set = set()
        max_len = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] in max_set:
                    sub_len = len(max_set)
                    break
                else:
                    max_set.add(s[j])
                    sub_len = len(max_set)
            max_set = set()
            if sub_len > max_len:
                max_len = sub_len
        
        return max_len
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        letters = set()
        max_len = 0
        for right in range(len(s)):
            if s[right] in letters:
                while s[right] in letters:
                    letters.remove(s[left])
                    left += 1
                letters.add(s[right])
                
            else:
                letters.add(s[right])
                max_len = max(max_len, right - left + 1)
        return max_len

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('a'))