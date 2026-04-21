# Last updated: 4/21/2026, 11:27:05 PM
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        def f(i, j, triangle):
            if i == 0 and j == 0:
                return triangle[i][j]
            if i < 0 or j < 0 or j > i:
                return float('inf')
            if dp[i][j] != -1:
                return dp[i][j]
            
            
            curr = triangle[i][j] + f(i - 1, j , triangle)
            prev = triangle[i][j] + f(i - 1, j - 1, triangle)
            dp[i][j] = min(curr, prev)
            return min(curr, prev)
            
        m = len(triangle)
        n = len(triangle[m - 1])
        dp = [[-1 for _ in range(len(triangle[i]))] for i in range(m)] #
        mini = float('inf')
        for i in range(n):
            mini = min(mini, f(m - 1, i, triangle))
        return mini