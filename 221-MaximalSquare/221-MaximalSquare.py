# Last updated: 4/21/2026, 11:26:07 PM
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n+1)]for _ in range(m+ 1)]   
        dp[1][1] = 1 if matrix[0][0] == '1' else 0
       
    
        max_size = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1' and i >= 0 and j >= 0:
                    dp[i+1][j+1] = 1 + min(dp[i][j+1], dp[i+1][j ], dp[i][j])
                    max_size = max(dp[i+1][j+1], max_size)
                else:
                    dp[i+1][j+1] = 0
        return max_size* max_size 