# Last updated: 4/21/2026, 11:24:40 PM
import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap = []
        for wt in stones:
            heapq.heappush(heap, -1*wt)
        while len(heap) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, y - x)

        return -1 * heap[0] if heap else 0