"""
409. Longest Palindrome
https://leetcode.com/problems/longest-palindrome/description/?envType=problem-list-v2&envId=hash-table&difficulty=EASY
"""

"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest
palindrome that can be built with those letters.
A palindrome is a string that reads the same forward and backward.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Use dict to map all letters and just add oll even and max of odd

This worked but too slow

Good way is to count not every appearence but only amount of odd letters, this way wa can just
know that others are even and our polindrome will be of lenghts len(s) - amount_of_odd + 1

The best approach is to count pairs of letters using set:
we iterate through letters
if letter is not in set, we put it there
if letter is in the set, we take it away from set and add 2 to len of polyndrome
if after itteration set is not empty we add 1 to result
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_dict = {}
        for letter in s:
            if letter in s_dict:
                s_dict[letter] += 1
            else:
                s_dict[letter] = 1
        lenghts = 0
        max_odd = 0
        for letter in s_dict:
            if s_dict[letter] % 2 == 0:
                lenghts += s_dict[letter]
            else:
                max_odd = 1
                lenghts += s_dict[letter] - 1
        return lenghts + max_odd