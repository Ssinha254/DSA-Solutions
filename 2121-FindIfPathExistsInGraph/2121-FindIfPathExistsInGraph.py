# Last updated: 4/21/2026, 11:24:16 PM
from collections import defaultdict
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph = defaultdict(list)
        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)

        
        def dfs(node,visited):
            if node == destination:
                return True
            if node is None:
                return False
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    found = dfs(neighbour, visited)
                    if found:
                        return True
            return False
        
        return dfs(source, set())