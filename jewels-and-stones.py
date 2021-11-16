"""
link:https://leetcode-cn.com/problems/jewels-and-stones/
"""


class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count = 0
        for i in stones:
            if i in jewels:
                count += 1
        return count


class Solution2(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        d = {}
        for i in jewels:
            d[i] = 0
        for j in stones:
            if j in d:
                d[j] += 1
        return sum(d.values())


jewels = "aA"
stones = "aAAbbbb"
a = Solution2()
print(a.numJewelsInStones(jewels, stones))
