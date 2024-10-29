"""
13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/description/?envType=problem-list-v2&envId=hash-table
"""

"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, 
which is XX + V + II.

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.


Comment:
Done. As far as i understand, hash tables are used when it is easy to know all pre-determined
cases or it is easy to calculate them. Great for lookupable values but probably needs optimization
for large data. But then something like elastic exists, so why bother making up in house solution?

Second solution is made by using hint, it performs way worse (almost 3 times) in terms of time 
complexity. My guess is that using more operateions on such small data is doing more work, than
using fewer operations.

"""


class My_Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        answer = 0
        i = 0
        while i <= len(s) - 1:
            number = s[i:i + 2]
            if number in roman_dict:
                answer += roman_dict[number]
                i += 2
            else:
                answer += roman_dict[number[0]]
                i += 1
        return answer

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        answer = 0
        i = len(s) - 1
        previous_number = 0
        while i >= 0:
            number = roman_dict[s[i]]
            if number >= previous_number:
                answer += number
            else:
                answer -= number
            i -= 1
            previous_number = number
        return answer

if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("III"))
    print(s.romanToInt("LVIII"))
    print(s.romanToInt("MCMXCIV"))
