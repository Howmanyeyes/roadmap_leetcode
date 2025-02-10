"""
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150
"""

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different
day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit,
return 0.

Тупой и простой подход - перебрать все варианты, тогда у нас будет два указателя, один слева другой
справа, тогда у нас сложность О(n^2) и О(1) по памяти, потому что нам нужно хранить лишь
максимальный профит.
Более хороший по моему мнению подход - пройтись слева на право по каждому числу и смотреть все даты
впереди него и записывать максимальный профит. Сложность та же, но интуитивно проще, более того 
теперь мы можем пользоваться max(), что должно увеличить скорость.
Этот подход дал тайм лимит) Теперь можно попробовать отсортировать список, и получить хуй в рот.

Посмотрел решение опять, к сожаоению мозгов не хватает думать и об индексах и о значениях, я честно
старался минут 20 что то придумать.
Хорошее решение же в том, чтобы следить за минимальной ценой входа и поинтером проходить по списку.

Так же трюк в том, чтобы всегда хранить максимальный профит и при подсчете нового профита сравнивать
его с лучшим уже достигнутым, чтобы никогда не получить значение меньше 
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for p in prices[1:]:
            if buy_price > p:
                buy_price = p
            
            profit = max(profit, p - buy_price)
        
        return profit
    
if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([100,300,5,99,98,299,1,10]))