"""
18. 4Sum
https://leetcode.com/problems/4sum/description/
"""

"""
Given an array nums of n integers, return an array of all the unique quadruplets 
[nums[a], nums[b], nums[c], nums[d]] such that:

    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

nums = [1,0,-1,0,-2,2], target = 0
1+0-1+0 = 0 = target
we need to add up to target and any number can be used once, there could be any number of answers

we can check every permutation, but that would be very time consuming

we can make a dict where we associate value with it's indexes, after that we can start making
permutations, worst case after alredy having dict we will have to make n*(n-1)*(n-2)*(n-3) tries
which is O(n^4). I guess permutations are not acceptable.

we can trade speed for memory: we can make first dict for indexes, after that we can make 
dict which will be {sum of all pairs of keys in first dict: list of lists of used indexes}
we can do it 2 more times to get all possible sums and last iteration can append only when target is
met. In the end we will have {target: list of lists of lists of lists of indexes}. Final list will 
have 4 layers of incapsulation, each layer containing 2 lists (except for first where it is any)
it's better that i learn what tree is and then do something like this, cuz in my brain that
list of lists looks perfectly like a tree or a pyramid.

let's make this approach. For cases when we have identical indexes in different lists we won't have
a problem

I can't make this solution work, I will leave this problem be for the time being
"""

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        one_layer = {}
        two_layer = {}
        three_layer = {}
        four_layer = {}

        for i in range(len(nums)):
            if nums[i] in one_layer:
                one_layer[nums[i]].append(i)
            else:
                one_layer[nums[i]] = []
                one_layer[nums[i]].append(i)
        tmp_set = set()
        for num1 in one_layer:
            tmp_set.add(num1)
            for num2 in one_layer:
                if num2 in tmp_set:
                    pass
                
                elif num1 + num2 in two_layer:
                    two_layer[num1 + num2].append((one_layer[num1], one_layer[num2]))
                else:
                    two_layer[num1 + num2] = []
                    two_layer[num1 + num2].append((one_layer[num1], one_layer[num2]))
        tmp_set = set()

        for num1 in two_layer:
            tmp_set.add(num1)
            for num2 in two_layer:
                if num2 in tmp_set:
                    pass
                elif num1 + num2 in three_layer:
                    three_layer[num1 + num2].append((two_layer[num1], two_layer[num2]))
                else:
                    three_layer[num1 + num2] = []
                    three_layer[num1 + num2].append((two_layer[num1], two_layer[num2]))
        tmp_set = set()

        for num1 in three_layer:
            tmp_set.add(num1)
            for num2 in three_layer:
                if num2 in tmp_set:
                    pass
                elif num1 + num2 in four_layer:
                    four_layer[num1 + num2].append((three_layer[num1], three_layer[num2]))
                else:
                    four_layer[num1 + num2] = []
                    four_layer[num1 + num2].append((three_layer[num1], three_layer[num2]))
        
        for num in four_layer:
            if num == target:
                pass

if __name__ == '__main__':
    s = Solution()
    print(Solution().fourSum([1,0,-1,0,-2,2], 0))