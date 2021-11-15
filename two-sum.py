class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if (target - nums[i]) in nums[i + 1:]:
                return [i, nums[i + 1:].index(target - nums[i]) + i + 1]
        return []


class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [d[target - nums[i]], i]
            d[nums[i]] = i
        return []


nums = [3, 3]
target = 6
a = Solution2()
print(a.twoSum(nums, target))

"""
Solution2 uses hashtable (by using dict), here are some useful links about the principle behind hashtable
https://www.jianshu.com/p/55ecbc03c8c1
https://en.wikipedia.org/wiki/Hash_table
https://wiki.python.org/moin/TimeComplexity
"""