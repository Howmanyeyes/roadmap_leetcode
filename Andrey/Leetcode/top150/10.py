"""
45. Jump Game II
https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150
"""

"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words,
if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Можно проходиться по списку справа налево, пытаясь найти максимально удаленую точку прыжка, так мы
ничего не пропустим

Сделано правильно, но опять же невнимательно
"""

class Solution:
    def jump(self, nums: list[int]) -> int:
        dist = 1
        jumps = 0
        curr_max = 0
        pos = len(nums) - 1
        while pos > 0:
            for j in range(pos - 1, -1, -1):
                if nums[j] >= dist:
                    if dist > curr_max:
                        curr_max = dist
                dist += 1 
            pos -= curr_max   
            jumps += 1
            dist = 1
            curr_max = 0
        return jumps
    
if __name__ == '__main__':
    s = Solution()
    s.jump([2,3,1,1,4])