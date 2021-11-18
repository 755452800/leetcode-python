"""
link: https://leetcode-cn.com/problems/diagonal-traverse/
"""

from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row_num = len(mat)
        col = len(mat[0])






mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = Solution()
print(a.findDiagonalOrder(mat))