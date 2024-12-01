"""
9. Palindrome Number
https://leetcode.com/problems/palindrome-number/description/
"""

"""
Given an integer x, return true if x is a palindrome, and false otherwise.

An integer is a palindrome when it reads the same forward and backward.

For example, 121 is a palindrome while 123 is not.

можно преобразовать инт в стринг и сделать два указателя которые слева и справа будут по нему идти

Тупые ошибки, внимательнее надо
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        left, right = 0, len(str_x) - 1 
        while left < right:
            if str_x[left] != str_x[right]:
                return False
            left += 1
            right -= 1
        return True