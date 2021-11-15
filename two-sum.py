class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if (target - nums[i]) in nums[i+1:]:
                return [i, nums[i+1:].index(target - nums[i]) + i + 1]


nums = [2,7,11,15]
target = 100
a = Solution()
print(a.twoSum(nums, target))
