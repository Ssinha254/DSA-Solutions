# Last updated: 8/21/2026, 1:30:53 PM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        i = 1
4        j = 1
5        k = len(nums)
6        while i < k:
7            if nums[i] != nums[ j -1]:
8                nums[j] = nums[i]
9                j+=1
10                
11            i+=1
12        return j
13        