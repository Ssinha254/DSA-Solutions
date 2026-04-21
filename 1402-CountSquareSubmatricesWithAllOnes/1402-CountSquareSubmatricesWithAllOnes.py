# Last updated: 4/21/2026, 11:24:33 PM
class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
       
        def f(i, j):
            if i <0 or j < 0 or i >= m or j >=n:
                return 0
            if dp[i][j] != 0:
                return dp[i][j]
            count = 0
            if matrix[i][j] == 1:
                count = 1 + min(dp[i-1][j], dp[i-1][j-1] , dp[i][j-1])
                
            dp[i][j] = count 
            return count
        total = 0
        for i in range(m):
            for j in range(n):
                total += f(i,j)
        return total