# Last updated: 4/21/2026, 11:26:55 PM
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def dfs( node, vis):
            if node is None:
                return
            if node[0] + 1 < rows and vis[node[0] + 1][node[1]] == 0 and board[node[0] + 1][node[1]] == "O":
                vis[node[0] + 1][node[1]] = 1
                dfs([node[0] + 1,node[1]],vis)
            if node[1] + 1< cols and vis[node[0]][node[1] + 1] == 0 and board[node[0]][node[1] + 1] == "O" :
                vis[node[0]][node[1] + 1] = 1
                dfs([node[0],node[1] + 1], vis)
            if node[0] - 1 >= 0 and vis[node[0] - 1][node[1]] == 0 and board[node[0] - 1][node[1]] == "O":
                vis[node[0] - 1][node[1]] = 1
                dfs([node[0] - 1,node[1]], vis)
            if node[1] - 1  >=0 and vis[node[0]][node[1] - 1] == 0 and board[node[0]][node[1] - 1] == "O":
                vis[node[0]][node[1] - 1] = 1
                dfs([node[0],node[1] - 1], vis)
              
        rows = len(board)
        cols = len(board[0])
        vis = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            if board[i][0] == "O" and vis[i][0] == 0:
                vis[i][0] = 1
                dfs([i, 0], vis)
            if board[i][cols - 1] == "O" and vis[i][cols - 1] == 0:
                vis[i][cols - 1] = 1
                dfs([i, cols - 1], vis)

        for i in range(cols):
            if board[0][i] == "O" and vis[0][i] == 0:
                vis[0][i] = 1
                dfs([0, i], vis)
            if board[rows - 1][i] == "O" and vis[rows - 1][i] == 0:
                vis[rows - 1][i] = 1
                dfs([rows - 1, i], vis)
  

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and vis[i][j] == 0:
                    board[i][j] ="X"