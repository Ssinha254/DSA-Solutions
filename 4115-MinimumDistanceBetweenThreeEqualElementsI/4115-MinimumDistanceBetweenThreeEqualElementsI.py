# Last updated: 4/21/2026, 11:24:05 PM
from collections import defaultdict
class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = defaultdict(list)
        for i in range(len(nums)):
            hashmap[nums[i]].append(i)
        res = float('inf')
        for i, ind in hashmap.items():
            if len(ind) >= 3:
                for j in range(len(list(ind)) - 2):
                    p, q, r = ind[j], ind[j +1], ind[j+2]
                    res = min(res, ( abs(p - q) + abs(q - r) + abs(r - p)))

        return res if res != float('inf') else -1