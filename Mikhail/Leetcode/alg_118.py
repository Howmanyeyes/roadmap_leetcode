'''Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rt = [[1], [1,1]]
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return rt
        else:
            for i in range(1, numRows - 1):
                c = []
                c.append(1)
                for z in range(0, len(rt[i]) - 1):
                    c.append(rt[i][z] + rt[i][z+1])
                c.append(1)
                rt.append(c)
        return rt