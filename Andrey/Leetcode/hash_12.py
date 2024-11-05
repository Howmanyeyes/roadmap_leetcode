"""
12. Integer to Roman
https://leetcode.com/problems/integer-to-roman/description/?envType=problem-list-v2&envId=hash-table&difficulty=MEDIUM
"""

"""
Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be 
subtracted from the input, append that symbol to the result, subtract its value, and convert the
remainder to a Roman numeral.

If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from
the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I)

less than 10 (X): IX. Only the following subtractive forms are 
used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).

Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent
multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append
a symbol 4 times use the subtractive form.

Given an integer, convert it to a Roman numeral.

Pre make a map of letters and then use those to construct a number?
map is made but how to use it i have NO idea

quite possible with long list of spaggetti code, tho i am convinced that that realization will be
faster, i know for a fact that it is very ugly. I don't know how to use hash fucking map here,
but i suspect it has to do with deviding number into digits and then deviding them into possible 
digits and thn using map to convert them into roman 

On the next day made quite inefficient algo that is just bleeding with lists, i am dissappointed with myself

It turn out that you can use sorted list of int-roman pairs and just iterate through it, it works 
beacause romans try to use biggest numbers and in sorted list biggest numbers get used automatically

"""
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        digits_to_roman = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        devider = {
            9: '9',
            8: '5 1 1 1',
            7: '5 1 1',
            6: '5 1',
            5: '5',
            4: '4',
            3: '1 1 1',
            2: '1 1',
            1: '1'
        }
        thousands = {
            1: 'M'
        }
        hundreds = {
            1: 'C',
            4: 'CD',
            5: 'D',
            9: 'CM',
        }
        tens = {
            1: 'X',
            4: 'XL',
            5: 'L',
            9: 'XC',
        }
        ones = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
        }
        thousand = (num // 1000) * 1
        hundred = ((num // 100) % 10) * 1
        ten = ((num // 10) % 10) * 1
        one = num % 10
        res = ''
        if thousand != 0:
            res += ''.join([thousands[int(x)] for x in devider[thousand].split(' ')])
        if hundred != 0:
            res += ''.join([hundreds[int(x)] for x in devider[hundred].split(' ')])
        if ten != 0:
            res += ''.join([tens[int(x)] for x in devider[ten].split(' ')])
        if one != 0:
            res += ''.join([ones[int(x)] for x in devider[one].split(' ')])
        return res
    
if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(3749))