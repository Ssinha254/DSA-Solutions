# Last updated: 8/19/2026, 12:15:15 AM
1from collections import defaultdict
2class Solution(object):
3    def sortColors(self, nums):
4        """
5        :type nums: List[int]
6        :rtype: None Do not return anything, modify nums in-place instead.
7        """
8        low = 0
9        mid = 0
10        high = len(nums) -1
11        while low <= mid and mid <= high:
12            if nums[mid] == 0:
13                nums[mid], nums[low] = nums[low], nums[mid]
14                low += 1
15                mid +=1 
16            elif nums[mid] == 2:
17                nums[mid], nums[high] = nums[high], nums[mid]
18                high -= 1
19               
20            else:
21                mid+=1
22            
23