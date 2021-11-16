"""
link:https://leetcode-cn.com/problems/concatenation-of-array/
"""


class Solution:
    def getConcatenation(self, nums):
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums


nums = [1, 2, 1]
a = Solution()
print(a.getConcatenation(nums))
