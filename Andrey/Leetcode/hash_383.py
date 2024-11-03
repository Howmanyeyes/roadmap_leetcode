"""
383. Ransom Note
https://leetcode.com/problems/ransom-note/description/?envType=problem-list-v2&envId=hash-table&difficulty=EASY
"""

"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by
using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Sets wouldn't work, cuz of repeatability of objects, but hash map can work again, i can copy from
350 but for the sake of learning i won't 

As i turned out there exist this little thingy: from collections import Counter
which does exactly what i did with my code. I should google more.
"""
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        magazine_map = {}
        for letter in magazine:
            if letter in magazine_map:
                magazine_map[letter] += 1
            else:
                magazine_map[letter] = 1
        ransom_map = {}
        for letter in ransomNote:
            if letter in magazine_map:
                if magazine_map[letter] >= 1:
                    ransom_map[letter] -= 1
                else:
                    return False
            else:
                return False
        
        return True
