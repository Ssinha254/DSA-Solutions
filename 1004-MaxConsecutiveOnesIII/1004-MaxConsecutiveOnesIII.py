# Last updated: 6/1/2026, 7:42:27 PM
1class Solution(object):
2    def longestOnes(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: int
7        """
8        left = 0
9        flips = 0
10        result = 0
11        for right in range(len(nums)):
12            if nums[right] == 0:
13                if flips < k:
14                      flips += 1
15                else:
16                    while flips>=k and left<=right  :
17                        if nums[left] == 0:
18                            flips-= 1
19                        left += 1
20                    flips+=1
21            result = max(result,right -left+ 1)
22
23        return result
24                            