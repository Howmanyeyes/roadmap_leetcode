"""
202. Happy Number
https://leetcode.com/problems/happy-number/?envType=problem-list-v2&envId=hash-table&difficulty=EASY
"""

"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

1) Starting with any positive integer, replace the number by the sum of the squares of its digits.
2) Repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
3) Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        got_squares = set()
        while 1:
            square = self.square(n)
            if square == 1:
                return True
            if square not in got_squares:
                got_squares.add(square)
                n = square
            else:
                return False

    def square(self, n):
        return sum(int(x)**2 for x in str(n))