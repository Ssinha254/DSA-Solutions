# Last updated: 4/21/2026, 11:24:22 PM
class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        m = len(cuts)
        cuts = [0] + cuts + [n]
        cuts = sorted(cuts)
        dp = [[-1 for _ in range(m + 1)]for _ in range(m + 1)]
        def f(i, j):
            if (i > j):
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            mini = float('inf')
            for ind in range(i, j + 1):
                length = cuts[j + 1] - cuts[i - 1] + f(i, ind - 1) + f(ind+ 1, j)
                mini= min(mini, length)
                dp[i][j] = mini
            return dp[i][j] 
    
        return f(1,m)
