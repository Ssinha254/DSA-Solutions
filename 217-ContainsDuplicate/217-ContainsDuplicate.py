# Last updated: 4/21/2026, 11:26:06 PM
from collections import Counter
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap = set()
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            hashmap.add(nums[i])
        return False
            