# Last updated: 5/22/2026, 7:16:21 PM
1class Solution(object):
2    def maxProfit(self, prices):
3        """
4        :type prices: List[int]
5        :rtype: int
6        """
7        n = len(prices)
8        max_profit = 0
9        for i in range(1,n):
10            if prices[i] > prices[i-1]:
11                max_profit += prices[i] - prices[i- 1]
12
13        return max_profit
14
15