"""
link: https://leetcode-cn.com/problems/find-pivot-index/
"""

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == 0:
                if sum(nums[1:]) == 0:
                    return i
            if sum(nums[0:i]) == sum(nums[i + 1:]):
                return i
            if i == len(nums) - 1:
                if sum(nums[0:-1]) == 0:
                    return i
        else:
            return -1


class Solution2:
    def pivotIndex(self, nums: List[int]) -> int:
        numSum = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            if numSum - leftSum - nums[i] == leftSum:
                return i
            leftSum += nums[i]
        return -1


nums = [1, 7, 3, 6, 5, 6]
a = Solution2()
print(a.pivotIndex(nums))
