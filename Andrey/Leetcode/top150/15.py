"""
135. Candy
https://leetcode.com/problems/candy/description/?envType=study-plan-v2&envId=top-interview-150
"""

"""
There are n children standing in a line. Each child is assigned a rating value given in the integer
array ratings.

You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.

Тут надо либо много ифов городить чтобы рассмотреть все случаи взаимоотношения соседних детей, либо
хз. Очень тяжелвя задача, не понятно нихуя как ее решить.
"""

class Solution:
    def candy(self, ratings: list[int]) -> int:
        if len(ratings) == 1:
            return 1
        elif len(ratings) == 2:
            return 3
        candies = len(ratings)
        dist = [1] * len(ratings)
        while True:
            done_something = False
            for i in range(1, len(ratings) - 1):
                if ratings[i - 1] > ratings[i] and dist[i - 1] <= dist[i]:
                    candies += (dist[i] - dist[i - 1]) + 1 
                    dist[i-1] = dist[i] + 1
                    done_something = True
                elif ratings[i + 1] > ratings[i] and dist[i + 1] <= dist[i]:
                    candies += (dist[i] - dist[i + 1]) + 1 
                    dist[i + 1] = dist[i] + 1
                    done_something = True
            
            if not done_something:
                return candies
            
if __name__ == '__main__':
    s = Solution()
    print(s.candy([1,0,2]))