# Last updated: 4/21/2026, 11:25:00 PM
from collections import defaultdict
import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = [[] for i in range(n + 1)]
        for time in times:
            u, v, w = time
            graph[u].append([v, w])

        heap = []
        heapq.heappush(heap, [0, k])

        visited = defaultdict(lambda: float('inf')) 
        visited[k] = 0

        while heap:
            t, node = heapq.heappop(heap)
            

            for neighbour in graph[node]:
                if  t + neighbour[1] < visited[neighbour[0]]:
                    visited[neighbour[0]] = t + neighbour[1]
                    
                    heapq.heappush(heap, [t + neighbour[1], neighbour[0]])

        if len(visited) < n:
            return -1
        return max(visited.values())