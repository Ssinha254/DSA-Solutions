# Last updated: 4/21/2026, 11:25:31 PM

from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        c = Counter(nums)
        c = dict(c)
        c = sorted(c.items(), key = lambda item: item[1], reverse = True)
        for i in range(k):
            res.append(c[i][0])
        return res