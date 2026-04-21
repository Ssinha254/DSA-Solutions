# Last updated: 4/21/2026, 11:26:17 PM
from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj = [[] for _ in range(numCourses)]
        for i in range(len(prerequisites)):
            u, v = prerequisites[i]
            adj[v].append(u)
        q  = deque()
        V = numCourses
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
        if  len(res) == V:  
            return res
        else:
            return []

            
            