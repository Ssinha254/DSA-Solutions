# Last updated: 8/11/2026, 3:00:15 PM
1class Solution(object):
2    def nextPermutation(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: None Do not return anything, modify nums in-place instead.
6        """
7        def swap(i):
8            """ 
9            Find the element next largest to nums[i] to the right of i and swap
10            """
11            candidate = None
12            for j in range(i+ 1,len(nums)):
13                if nums[j]> nums[i]:
14                    candidate = j
15                if nums[candidate] < nums[j] and nums[j] > nums[i]:
16                    candidate = j
17            nums[i], nums[candidate] = nums[candidate], nums[i]
18            nums[i+1:] = nums[i + 1:][::-1]
19        
20        flag = False
21        for i in range(len(nums) - 2, -1, -1):
22            if nums[i] < nums[i + 1]:
23                swap(i)
24                flag = True
25                break
26           
27        if flag is False:
28            return nums.sort()
29        
30        return nums