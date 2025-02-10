"""
55. Jump Game
https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150
"""

"""
You are given an integer array nums. You are initially positioned at the array's first
index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Сам дошел до решения когда смотрим с конца и пытаемся понять куда мы попали и так переносим все
ближе к началу конечную цель. Но увидив тег greedy подумал что можно просто отметить все индексы
в которых мы были. Это и реализую 
"""

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        need_to_be = len(nums) - 1
        if need_to_be == 0:
            return True
        dist = 1
        for i in range(need_to_be - 1, -1, -1):
            if nums[i] >= dist:
                need_to_be -= dist
                dist = 0
            if need_to_be <= 0:
                return True
            dist += 1
        return False
            
if __name__ == '__main__':
    s = Solution()
    s.canJump([2,3,1,1,4])
