# Last updated: 5/27/2026, 1:38:18 PM
1class Solution(object):
2    def solve(self, board):
3        """
4        :type board: List[List[str]]
5        :rtype: None Do not return anything, modify board in-place instead.
6        """
7      
8        n = len(board)
9        m = len(board[0])
10
11        visited = set()
12        def dfs(i,j):
13            if (i,j) in visited:
14                return
15            visited.add((i,j))
16            dirs=[(0,1), (1,0),(-1,0), (0,-1)]
17            for r, c in dirs:
18                ni = i + r
19                nj = j + c
20                if ni < 0 or ni >= n or nj < 0 or nj >= m:
21                    continue
22                if (ni,nj) in visited:
23                    continue
24                if board[ni][nj] == 'O':
25                    dfs(ni,nj)
26        
27        for i in range(n):
28            if board[i][0] == 'O':
29                dfs(i, 0)
30            if board[i][m - 1] =='O':
31                dfs(i, m -1)
32        for j in range(m):
33            if board[0][j] == 'O':
34                dfs(0,j)
35            if board[n - 1][j] == 'O':
36                dfs(n-1, j)
37
38        for i in range(n):
39            for j in range(m):
40                if (i,j) not in visited:
41                    board[i][j] = 'X'
42        return board