"""
73. Set Matrix Zeroes
https://leetcode.com/problems/set-matrix-zeroes/description/?envType=problem-list-v2&envId=hash-table
"""

"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

It seems that if i just iterate throug every zero and right away replace values the cycle will be
endless and i will jsut return all - zero matrix. To combat this i can keep set of all locations
which need to be turned into zeroes and then just iterate throug set. 

Fucking best solution as for time complexity. But could be better in terms of space. 
"""

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_set = set()
        skipping_cols = set()
        skipping_rows = set()
        i = 0
        j = 0
        len_row = len(matrix[0])
        while j < (len(matrix)):
            i=0
            while i < len_row:
                #if i in skipping_cols:
                #    pass
                if matrix[j][i] == 0:
                    skipping_rows.add(j)
                    skipping_cols.add(i)
                i += 1
            j += 1

        # print(1)
        
        for row in skipping_rows:
            matrix[row] = [0] * len_row
        
        for row in matrix:
            for col in skipping_cols:
                row[col] = 0


              

if __name__ == '__main__':
    s = Solution()
    print(s.setZeroes([[0,0,0,5],
                       [4,3,1,4],
                       [0,1,1,4],
                       [1,2,1,3],
                       [0,0,1,1]]))