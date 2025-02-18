"""
58. Length of Last Word
https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150
"""

"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Тут просто сплит и лен вернуть
стрип все проблемы не решит, тогда просто найдем первый индекс где есть пробел и просто вернем
длину так

5:45 не считая подготовки
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                return len(s) - i