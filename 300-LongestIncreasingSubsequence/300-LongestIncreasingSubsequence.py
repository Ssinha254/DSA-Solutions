# Last updated: 4/21/2026, 11:25:40 PM
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        dp =[0 for _ in range(n)]
        dp[0] = 1
        maxi = 1
        for i in range(0,n):
            dp[i] = 1
            for prev in range(0, i):
               
                if nums[i] > nums[prev]:
                    dp[i]= max(dp[i],1 + dp[prev])
                    
            maxi = max(maxi , dp[i])
        return maxi


            