# Last updated: 4/21/2026, 11:27:02 PM
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]

        def f(ind, buy):
            if  ind ==n :
                return 0
            if dp[ind][buy] != -1:
                return dp[ind][buy]
            if buy == 1:
                dp[ind][buy] = max(f(ind +1, 0) - prices[ind], f(ind +1, 1))
            else:
                dp[ind][buy]  = max(prices[ind] + f(ind+ 1, 1), f(ind + 1, 0))
            return dp[ind][buy]

        return f(0,1)