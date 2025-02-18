class Solution:
    def romanToInt(self, s: str) -> int:
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        answ = 0
        for letter in s:
            if letter == "I":
                answ += 1
            elif letter == "V":
                answ += 5
            elif letter == "X":
                answ += 10
            elif letter == "L":
                answ += 50
            elif letter == "C":
                answ += 100
            elif letter == "D":
                answ += 500
            elif letter == "M":
                answ += 1000
            
        return answ

if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("MMMXLV"))