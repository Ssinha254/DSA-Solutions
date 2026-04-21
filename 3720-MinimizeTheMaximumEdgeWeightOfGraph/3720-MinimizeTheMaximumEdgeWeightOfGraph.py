# Last updated: 4/21/2026, 11:24:06 PM
from collections import defaultdict 
class Solution(object):
    def minMaxWeight(self, n, edges, threshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        graph = defaultdict(list)
        for s, d, w in edges:
            graph[d].append((s,w))
        
        def dfs(node,graph, seen, weight_limit):
                if node in seen:
                    return
                seen.add(node)
                for n, w in graph[node]:
                    if w > weight_limit:
                        continue
                    dfs(n, graph, seen, weight_limit)

        l= 1
        weights = [w for _, _, w in edges]
        l = min(weights)
        r = max(weights)
        res = -1
        while l <=r:
            m = (l + r)//2
            seen = set()
            dfs(0, graph, seen, m)

            if len(seen) == n:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
