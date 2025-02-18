"""
151. Reverse Words in a String
https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150
"""

"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. Do not include any extra spaces.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()
        s = [s[i] for i in range(len(s) - 1,-1,-1)]
        return " ".join(s)