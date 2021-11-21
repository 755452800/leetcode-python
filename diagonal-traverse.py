"""
link: https://leetcode-cn.com/problems/diagonal-traverse/
"""

from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])
        direction = 1
        list = []
        r, c = 0, 0
        while len(list) < row*col:
            list.append(mat[r][c])
            if direction:
                r = r - 1
                c = c + 1
            else:
                r = r + 1
                c = c - 1
            if c < 0 or c >= col or r < 0 or r >= row:
                if direction:
                    if c >= col:
                        r = r + 2
                        c = c - 1
                    else:
                        r = r + 1
                        c = c
                else:
                    if r >= row:
                        r = r - 1
                        c = c + 2
                    else:
                        r = r
                        c = c + 1
                direction = 1 - direction
        return list


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = Solution()
print(a.findDiagonalOrder(mat))
