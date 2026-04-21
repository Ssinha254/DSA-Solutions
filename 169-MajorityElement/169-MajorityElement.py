# Last updated: 4/21/2026, 11:26:30 PM
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i] += 1
        for i, val in hashmap.items():
            if val >= len(nums) // 2 + 1:
                return i
        return None
        