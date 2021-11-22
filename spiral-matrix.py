"""
link: https://leetcode-cn.com/problems/spiral-matrix/
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        mat = []
        row = len(matrix)
        col = len(matrix[0])
        r = row
        c = col
        direction = "right"
        right, left, up, down = 0, 0, 0, 0
        vertical = list(zip(*matrix))
        vertical.reverse()
        while r > 0 and c > 0:
            if direction == "right":
                mat.extend(matrix[right][up:col - down])
                right += 1
                r -= 1
                if r <= 0:
                    break
                direction = "down"
            if direction == "down":
                mat.extend(vertical[down][right:row - left])
                down += 1
                c -= 1
                if c <= 0:
                    break
                direction = "left"
            if direction == "left":
                tmp = matrix[row - 1 - left][up:col - down]
                tmp.reverse()
                mat.extend(tmp)
                left += 1
                r -= 1
                if r <= 0:
                    break
                direction = "up"
            if direction == "up":
                tmp = list(list(zip(*matrix))[up][right:row - left])
                tmp.reverse()
                mat.extend(tmp)
                up += 1
                c -= 1
                if c <= 0:
                    break
                direction = "right"
        return mat


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
a = Solution()
print(a.spiralOrder(matrix))
