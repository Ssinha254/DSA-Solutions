# Last updated: 4/21/2026, 11:25:39 PM
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        dp = [[-1 for _ in range(2)] for _ in range(n + 2)]
        for i in range(2):
            dp[n][i] = 0
            dp[n + 1][i] = 0
        for i in range(n - 1, -1, -1):
            dp[i][1] = max(-prices[i] + dp[i + 1][0], dp[i+1][1])
            dp[i][0] = max(prices[i] + dp[i + 2][1], dp[i+1][0])
        return dp[0][1]