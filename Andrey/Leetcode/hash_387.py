"""
387. First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=hash-table&difficulty=EASY
"""

"""
Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.

I just tested and it turns out that you can turn sting into set of it's characters using naitive 
method set(). Which means that i am able to make set and then pop from it every time letter appears

Fuck, sets didn't work cuz of repetition of letters and Counter proved to be very very usless:
it is easy to use but very time inefficient 
"""
from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # cnt = Counter(s)
        
        
        magazine_map = {}
        for letter in s:
            if letter in magazine_map:
                magazine_map[letter] += 1
            else:
                magazine_map[letter] = 1
        for i in range(len(s)):
            if magazine_map[s[i]] == 1:
                return i
        return -1