# Last updated: 4/21/2026, 11:25:03 PM
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
      rows = len(image)
      cols = len(image[0])
      q = deque([])
      og_color = image[sr][sc]
      if image[sr][sc] == color:
        return image


      def bfs(node, image, q):
        if node[0] + 1 < rows and image[node[0] + 1][node[1]] == og_color:
                image[node[0] + 1][node[1]] = color
                q.append([node[0] + 1, node[1]])
        if node[0] - 1 >= 0 and image[node[0] - 1][node[1]] == og_color:
                image[node[0] - 1][node[1]] = color
                q.append([node[0] - 1, node[1]])
        if node[1] + 1 < cols and image[node[0]][node[1] + 1] == og_color:
                image[node[0]][node[1] + 1] = color
                q.append([node[0], node[1] + 1])
        if node[1] - 1 >= 0 and image[node[0]][node[1] - 1] == og_color:
                image[node[0]][node[1] - 1] = color
                q.append([node[0], node[1] - 1])
      image[sr][sc] = color
      q.append([sr,sc])
      while q:
        node = q.popleft()
        bfs(node, image, q)
      return image