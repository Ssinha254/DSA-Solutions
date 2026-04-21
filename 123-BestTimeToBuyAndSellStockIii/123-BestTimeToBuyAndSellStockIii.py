# Last updated: 4/21/2026, 11:27:01 PM
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        dp = [[[-float('inf') for _ in range(3)] for _  in range(2)]for _ in range(n + 1 )]
        for i in range(n + 1):
            for j in range(2):
                dp[i][j][0] = 0
        for k in range(3):
            for j in range(2):
                dp[n][j][k] = 0        
        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                for cap in range(1,3):
                    if buy == 1:
                        dp[ind][buy][cap] = max( - prices[ind] +dp[ind + 1][ 0] [cap], dp[ind+1][1][cap])
                    else:
                        dp[ind][buy][cap] = max(prices[ind]+dp[ind+1][1][cap-1], dp[ind+1][0][cap])
        return dp[0][1][2]

       