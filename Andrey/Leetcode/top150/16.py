"""
42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/description/?envType=study-plan-v2&envId=top-interview-150
"""

"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
Думаю мы можем итерировать держа в голове высоту левой стенки и глубину самого низа. Самый тяжелый 
случай будет когда в середине у нас непонятно какая форма, с множеством пиков и разными глубинами а
правая стенка короче левой. Чтобы такое решить, надо, а вот не знаю что надо, я не могу придумать 
хоть какое то решение, кроме О(n^2), что плохо, да и даже так не очень понятно что делать
"""