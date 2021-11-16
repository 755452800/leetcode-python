"""
link: https://leetcode-cn.com/problems/rotate-array/
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[- k % len(nums):] + nums[:- k % len(nums)]


nums = [1, 2]
k = 3
a = Solution()
a.rotate(nums, k)
print(nums)
