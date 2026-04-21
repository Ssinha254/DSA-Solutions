# Last updated: 4/21/2026, 11:26:21 PM
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        directions = [(0,1), (1, 0), (-1, 0), (0, -1)]
        def dfs(i, j):
            if i >= n or j >= m or i < 0 or j < 0:
                return 
            if grid[i][j] != "1":
                return
            grid[i][j] = "#"
            for dx, dy in directions:
                dfs(i + dx, j + dy)
            
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1

        return count 

        
