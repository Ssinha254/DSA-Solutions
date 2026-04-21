# Last updated: 4/21/2026, 11:24:56 PM
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        adj = [[] for _ in range(len(graph))]
        for i in range(len(graph)):
            for j in graph[i]:
                adj[j].append(i)

        q  = deque()
        V = len(graph)
        indegree = [0] * V
        res = []
        for i in range(V):
                for j in adj[i]:
                    indegree[j] += 1

        for i in range(V):
                if indegree[i] == 0:
                    q.append(i)
            
        while q:
                item = q.popleft()
                res.append(item)
                for i in adj[item]:
                    indegree[i] -= 1
                    if indegree[i] == 0 :
                        q.append(i)
            
        return  sorted(res)
