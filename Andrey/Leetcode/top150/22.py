"""
возможно есть смысл присваивать поочередно каждой букве ее строку, мы понимаем что строки идут
как бы от 0 до n-1 и потом от n-1 до 0, вообще очевидно, что у нас имеется паттерн, который повторяется столько раз сколько букв на него у нас хватает, паттерн состоит из ветрикаллььной черты и наклонной (не доходящей до конца), такой паттерн требует 2 + 2*(numrows - 2) букв, соответственно по остатку от деления на это число мы можем понимать когда его надо вставлять
давайте да, наполним хэш таблицу, потом из нее составим уже строку

"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows:
            return s
        pattern_len = 2 + 2*(numRows - 2)
        compensation = 0
        letters = {}
        for i in range(len(s)):
            if i % pattern_len >= numRows:
                compensation += 1
            else:
                compensation = 0
            if ((i % pattern_len) - 2*compensation) in letters:
                letters[(i % pattern_len) - 2*compensation].append(s[i])
            else:
                letters[(i % pattern_len) - 2*compensation] = [s[i]]
        ans = ""
        for i in range(numRows):
            ans += "".join(letters[i])
        return ans
    
if __name__ == "__main__":
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))