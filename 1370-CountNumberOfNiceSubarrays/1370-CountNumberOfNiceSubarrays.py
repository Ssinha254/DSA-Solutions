# Last updated: 4/21/2026, 11:24:34 PM
from collections import defaultdict
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
      
        prefix = defaultdict(int)
        prefix[0] = 1
        odds = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                odds +=1
            if odds - k in prefix:
                count += prefix[odds - k] 
            prefix[odds] += 1
        return count