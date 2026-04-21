# Last updated: 4/21/2026, 11:25:36 PM
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [[-1 for _ in range(amount+1)]for _ in range(len(coins))]
        def f(i, rem_sum):
            if rem_sum == 0:
                return 0
            if rem_sum < 0 :
                return float('inf')
            if i == len(coins):
                return float('inf')
            if dp[i][rem_sum] != -1:
                return dp[i][rem_sum]

            take = 1 + f(i , rem_sum - coins[i])
            not_take = f(i + 1, rem_sum)
            dp[i][rem_sum] = min(take, not_take)
            return dp[i][rem_sum] 
        res = f(0,amount)
        if res == float('inf'):
            return -1
        return res