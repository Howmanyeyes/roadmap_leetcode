"""
189. Rotate Array
https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
"""

"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.


Самый тупой способ - удлинить список в 2 раза и считать только нужное кол-во переходов, более
сложный подход - сделать что то с слайсами, сперва реализуем более простой. 

Пришлось подсмотреть решение, но лишь только потому что надо делать in-place, что просто пиздец
как же я ебал ебанистику питона с объектами, хотя наверно это именно моя проблема.
"""

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        actual_disp = k % len(nums) 
        nums[actual_disp:actual_disp + len(nums)]

if __name__ == "__main__":
    s = Solution()
    a = [1,2,3,4,5,6,7]
    s.rotate(k=3, nums=a)
    print(a)