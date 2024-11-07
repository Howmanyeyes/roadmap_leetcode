"""
36. Valid Sudoku
https://leetcode.com/problems/valid-sudoku/description/?envType=problem-list-v2&envId=hash-table
"""

"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

Checks of rows and cols are not difficult, but i am not sure of how to check 3x3 boxes, maybe i can
pre-make indexes in a way to get what i need. Or maybe i can get amount of numbers and compare it to
amount of numbers in a set. That sounds better

I am as pissed off as it could be, i am so angry at this problem, i can't describe it enough.
I can't make out theese 'medium' problems, it's so bad that i hit my table.

The solution i know would work but inefficiently is one where you first check rows and cols
then check arrays made from pre-made list pointers? that describe 3x3 squares. I am going to 
implement it to show myself that i'm not a pussy, but i hate this fucking non-hash related material
desguised as hash so fucking much.

as I said solution is very very bad, it beats only 20% which is so bad i don't want to save this.
Much optimization is possible, though I don't deep them nessesary as they won't change core method
of solution.

Best solution O(1) for time DOES NOT use hash fucking maps. Either I don't understand this concept
or this is leetcode's falt
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        c1 = []
        c2 = []
        c3 = []
        c4 = []
        c5 = []
        c6 = []
        c7 = []
        c8 = []
        c9 = []
        for row in board:
            tmpshit = [x for x in '-'.join(row).replace('.', '').replace('-', '')]
            if len(tmpshit) != len(set(tmpshit)):
                return False
            c1.append(row[0])
            c2.append(row[1])
            c3.append(row[2])
            c4.append(row[3])
            c5.append(row[4])
            c6.append(row[5])
            c7.append(row[6])
            c8.append(row[7])
            c9.append(row[8])
        for col in [c1, c2, c3, c4, c5, c6, c7, c8, c9]:
            tmpshit = [x for x in '-'.join(col).replace('.', '').replace('-', '')]
            if len(tmpshit) != len(set(tmpshit)):
                return False
            
        sq1 = board[0][0:3] + board[1][0:3] + board[2][0:3]
        sq2 = board[0][3:6] + board[1][3:6] + board[2][3:6]
        sq3 = board[0][6:9] + board[1][6:9] + board[2][6:9]
        sq4 = board[3][0:3] + board[4][0:3] + board[5][0:3]
        sq5 = board[3][3:6] + board[4][3:6] + board[5][3:6]
        sq6 = board[3][6:9] + board[4][6:9] + board[5][6:9]
        sq7 = board[6][0:3] + board[7][0:3] + board[8][0:3]
        sq8 = board[6][3:6] + board[7][3:6] + board[8][3:6]
        sq9 = board[6][6:9] + board[7][6:9] + board[8][6:9]
        for col in [sq1, sq2, sq3, sq4, sq5, sq6, sq7, sq8, sq9]:
            tmpshit = [x for x in '-'.join(col).replace('.', '').replace('-', '')]
            if len(tmpshit) != len(set(tmpshit)):
                return False

        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))