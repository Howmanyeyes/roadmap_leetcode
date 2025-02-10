"""
122. Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150
"""

"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of
the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Это просто пиздец, medium легче изи, хоть мое решенеие и не оптимально, но оно получено сверхбыстро.
UPD: Решение оптимально, приколы литкода, асимптотика как у топ 1%  
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        total = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                total += prices[i + 1] - prices[i]
        return total