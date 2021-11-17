"""
link: https://leetcode-cn.com/problems/rotate-image/
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        matrix[:] = map(list, zip(*matrix))
        # matrix[:] = zip(*matrix[::-1])


class Solution2:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        """
        水平翻转+对角线翻转
        """



matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
a = Solution2()
a.rotate(matrix)
print(matrix)
