# Last updated: 4/21/2026, 11:27:04 PM
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minimum = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i]  - minimum
            max_profit = max(profit, max_profit)
            minimum= min(prices[i], minimum)
        return max_profit
