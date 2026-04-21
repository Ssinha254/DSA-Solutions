# Last updated: 4/21/2026, 11:26:28 PM
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        dp = [[[-float('inf') for _ in range(k + 1)] for _  in range(2)]for _ in range(n + 1 )]
        for i in range(n + 1):
            for j in range(2):
                dp[i][j][0] = 0
        for i in range(k + 1):
            for j in range(2):
                dp[n][j][i] = 0        
        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                for cap in range(1,k + 1):
                    if buy == 1:
                        dp[ind][buy][cap] = max( - prices[ind] +dp[ind + 1][ 0] [cap], dp[ind+1][1][cap])
                    else:
                        dp[ind][buy][cap] = max(prices[ind]+dp[ind+1][1][cap-1], dp[ind+1][0][cap])
        return dp[0][1][k]
