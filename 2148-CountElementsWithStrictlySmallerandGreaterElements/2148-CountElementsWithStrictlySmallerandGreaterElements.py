# Last updated: 5/29/2026, 1:37:43 PM
1class Solution(object):
2    def countElements(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        count = 0
8        mi = min(nums)
9        ma = max(nums)
10        for i in nums:
11            if  mi < i < ma:
12                count += 1
13        return count 