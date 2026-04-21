# Last updated: 4/21/2026, 11:25:51 PM
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = deque()
        res = []
        for i, cur in enumerate(nums):
            while q and nums[q[-1]] <= cur:
                q.pop()
            q.append(i)
            if q[0] == i - k :
                q.popleft()
            if i >= k -1:
                res.append(nums[q[0]])
        return res