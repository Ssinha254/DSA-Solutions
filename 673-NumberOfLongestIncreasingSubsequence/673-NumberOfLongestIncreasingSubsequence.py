# Last updated: 4/21/2026, 11:25:06 PM
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [1 for _ in range(n)]
        cnt = [1 for _ in range(n)]
        maxi = 1
        for i in range(n):
            for prev in range(i):
                if nums[i]>nums[prev] and dp[prev] + 1 > dp[i]:
                    dp[i] = dp[prev] + 1
                    cnt[i] = cnt[prev] 
                elif nums[i]>nums[prev] and dp[prev] + 1 == dp[i]:
                    cnt[i] += cnt[prev] 
            maxi = max(maxi, dp[i])
        total = 0
        for i in range(n):
            if dp[i] == maxi:
                total += cnt[i]

        return total