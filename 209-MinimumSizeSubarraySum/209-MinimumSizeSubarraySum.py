# Last updated: 4/21/2026, 11:26:19 PM
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = 0
        minlen = float('inf')
        curr_sum = 0
        while r < len(nums):
            curr_sum += nums[r]
            while curr_sum >= target:
                minlen = min(minlen, r - l + 1)
                curr_sum -= nums[l]
                l = l + 1
            r = r + 1
        if minlen == float('inf'):
            return 0
        else:
            return minlen