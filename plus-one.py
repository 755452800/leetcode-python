"""
link: https://leetcode-cn.com/problems/plus-one/
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int, str(int("".join(map(str, digits))) + 1)))


class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                for j in range(i + 1, len(digits)):
                    digits[j] = 0
                return digits
        else:
            return [1] + len(digits) * [0]


digits = [8, 9, 9, 9]
a = Solution2()
print(a.plusOne(digits))
