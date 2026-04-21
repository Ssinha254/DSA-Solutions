# Last updated: 4/21/2026, 11:27:46 PM
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        def f(i, j, dp, grid):
            if grid[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            up = f(i - 1, j, dp, grid )
            down = f(i ,  j- 1, dp, grid)
            dp[i][j] =  up + down
            return dp[i][j]  
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        return f(m -1, n - 1, dp, obstacleGrid)