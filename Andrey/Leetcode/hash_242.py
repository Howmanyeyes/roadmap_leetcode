"""
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/description/?envType=problem-list-v2&envId=hash-table
"""

"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
using all the original letters exactly once. (appple -> ppplea)

maybe we can make str into set and after that we can compare them. 

Not into sets, but with dicts worked like magic
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_s = {}
        dict_t = {}        
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in dict_s:
                dict_s[s[i]] += 1
            else:
                dict_s[s[i]] = 1
            if t[i] in dict_t:
                dict_t[t[i]] += 1
            else:
                dict_t[t[i]] = 1
        if dict_s == dict_t:
            return True
        return False