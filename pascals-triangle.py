"""
https://leetcode.cn/problems/pascals-triangle/
"""

from typing import List


class SolutionR:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        def fun(n):
            if n == 1:
                return [1]
            if n == 2:
                return [1, 1]
            if n > 2:
                R = []
                for i in range(n):
                    if i == 0:
                        R.append(1)
                    elif i != 0 and i == n - 1:
                        R.append(1)
                    else:
                        R.append(fun(n - 1)[i - 1] + fun(n - 1)[i])
                return R

        for i in range(numRows):
            result.extend([fun(i + 1)])
        return result


class Solution1:
    def generate(self, numRows: int) -> List[List[int]]:
        res = list()


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]]
        while len(res) < numRows:
            newRow = [a + b for a, b in zip([0] + res[-1], res[-1] + [0])]
            res.append(newRow)
        return res


numRows = 5
a = SolutionR()
b = Solution1()
c = Solution()
print(a.generate(numRows))
print(b.generate(numRows))
print(c.generate(numRows))
