"""
438. Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
"""

"""
Given two strings s and p, return an array of all the start indices of p's anagrams
in s. You may return the answer in any order.


Можно прогнать S побуквенно, и для каждой буквы делать слудщее:
составляется "слово" из len(p) букв, начиная с текущей рассматриваемой буквы, слово сортируется 
и записывается в словарь

после составления такого словаря у нас есть буквально все возможные варианты "слов"
далее сортируем p и сравниваем со словарем, делаем ответ

Впервые в жизни я увидел мемори лимит ексидед, ВАУ!

По идее нам не нужна вторая итерация по дикту, можно прям сразу ответ писать

Счетчик тупых ошибок += 1

Теперь тайм лимит, возможно каждый раз сортировать p - плохое решение)

Сортировка по скорости не приемлима вообще, ну чтож, тогда делаем мап каждого слова и если он 
совпадет с мапом p то тогда это ответ

Похоже существует лишь одно правильное решение, которое заключается в том, чтобы двигать "окно" 
длиной в p по строке s, и при вхождении буквы в окно, прибавлять 1 к мапу, и убавлять единицу из мапа 
когда из окна выходят
Счетчик тупых ошибок += 1
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []
        p_dict = {}
        for letter in p:
            if letter in p_dict:
                p_dict[letter] += 1
            else:
                p_dict[letter] = 1
        len_p = len(p)
        len_s = len(s)

        for i in range(len(p) - 1):
            if s[i] in p_dict:
                p_dict[s[i]] -= 1
        ans = []
        for i in range(-1, len_s - len_p + 1):
            if i != -1 and s[i] in p_dict:
                
                p_dict[s[i]] += 1
            if i+ len_p < len_s and s[i + len_p] in p_dict:
                p_dict[s[i + len_p]] -= 1
            if all(value == 0 for value in p_dict.values()):
                ans.append(i + 1)
        
        return ans