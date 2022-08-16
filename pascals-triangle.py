"""
https://leetcode.cn/problems/pascals-triangle/
"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        def fun(n):
            if n == 1:
                return [1]
            if n == 2:
                return [1, 1]
            if n > 2:
                R = []
                R[0] = 1
                R[-1] = 1
                for i in range(n - 2):
                    R[i + 1] = fun(n - 1)[i] + fun(i + 1)
                return R
        for i in range(numRows):
            result.extend(fun(i))



numRows = 5
a = Solution()
print(a.generate(numRows))
