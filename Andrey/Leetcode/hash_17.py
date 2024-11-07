"""
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=problem-list-v2&envId=hash-table
"""

"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that 
the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

I can sence that iterating through given list is what will be done but i am not sure what to do
in the end we need to return list of strings so maybe we dyuunamicly generate our strings in each 
iteration?

I just have no god damn idea. Fuck me.

Copied solution for anti time waste. If 3 problems in a row go like this i will have to do something
with it, maybe watch courses or give up programming
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = set()
        size = 1
        for i in range(len(digits)):
            digit = digits[i]
            size = size * len(keyboard[digit]) 
            
        return size
    
if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('22'))

