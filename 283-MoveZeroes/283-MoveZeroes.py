# Last updated: 8/21/2026, 11:31:40 AM
1class Solution(object):
2    def moveZeroes(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: None Do not return anything, modify nums in-place instead.
6        """
7        i = 0
8        k = 0
9        while i < len(nums):
10            if nums[i] != 0:
11                nums[k], nums[i] = nums[i], nums[k]
12                k+=1
13            i+=1
14        return nums
15