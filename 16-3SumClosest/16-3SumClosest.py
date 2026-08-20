# Last updated: 8/21/2026, 12:31:37 AM
1class Solution(object):
2    def threeSumClosest(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: int
7        """
8        curr = 0
9        nums.sort()
10        closest = nums[0] + nums[1] + nums[2]
11        while curr< len(nums):
12            i = curr + 1
13            j = len(nums) -1
14            total = target - nums[curr]
15            while i < j:
16                if abs(total - (nums[i] + nums[j])) < abs(target - closest):
17                    closest = (nums[i] + nums[j]+nums[curr])
18                if nums[i] + nums[j] > total:
19                    j-=1
20                else:
21                    i+= 1
22            curr+= 1
23        return  closest