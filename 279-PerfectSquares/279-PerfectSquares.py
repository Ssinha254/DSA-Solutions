# Last updated: 4/21/2026, 11:25:45 PM
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range(n+1)]
        j = 1
        sq = 1
        while sq <= n:
            for i in range(sq, n+1):
                dp[i] = min(dp[i], dp[i - sq] + 1)
                
            sq = (j + 1) ** 2
            j += 1
        return dp[n]