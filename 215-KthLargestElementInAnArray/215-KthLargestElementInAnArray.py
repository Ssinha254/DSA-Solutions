# Last updated: 4/21/2026, 11:26:09 PM
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        heap = heapq.heapify(nums)
        for i in range(len(nums) -k):
            ele = heapq.heappop(nums)
        
        ele = heapq.heappop(nums)
        return ele