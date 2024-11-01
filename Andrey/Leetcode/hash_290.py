"""
290. Word Pattern
https://leetcode.com/problems/word-pattern/description/?envType=problem-list-v2&envId=hash-table
"""

"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a 
non-empty word in s. Specifically:

    Each letter in pattern maps to exactly one unique word in s.
    Each unique word in s maps to exactly one letter in pattern.
    No two letters map to the same word, and no two words map to the same letter.

map each word to dict when it apears, when it doesn't match, return False
"""

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        hash_map = {}
        s = s.split()
        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in hash_map:
                if s[i] in hash_map.values():
                    return False
                hash_map[pattern[i]] = s[i]
            else:
                if hash_map[pattern[i]] != s[i]:
                    return False
                
        return True