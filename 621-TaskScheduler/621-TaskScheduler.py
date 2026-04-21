# Last updated: 4/21/2026, 11:25:11 PM
import heapq
from collections import Counter
from collections import deque
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        c = dict(Counter(tasks))
        heap = []
        for i, f in c.items():
            heapq.heappush(heap, (-1*f, i))
        res = []
        q = deque()
        time = 0
        while heap or q:
            if q and q[0][2] == time:
                task, f, t = q.popleft()
                heapq.heappush(heap, (f, task))
            if heap:
                freq, curr= heapq.heappop(heap)
                freq += 1
                res.append(curr)
                if freq !=0:
                    q.append([curr, freq, time + n + 1])
            else:
                res.append("idle")
            time += 1
        return time
