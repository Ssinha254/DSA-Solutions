# Last updated: 6/1/2026, 7:43:17 PM
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
13                flips += 1
14                
15            while flips>k and left<=right  :
16                if nums[left] == 0:
17                    flips-= 1
18                left += 1
19                    
20            result = max(result,right -left+ 1)
21
22        return result
23                            