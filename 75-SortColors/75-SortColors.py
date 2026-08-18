# Last updated: 8/18/2026, 11:57:32 PM
1from collections import defaultdict
2class Solution(object):
3    def sortColors(self, nums):
4        """
5        :type nums: List[int]
6        :rtype: None Do not return anything, modify nums in-place instead.
7        """
8        hashmap = defaultdict(int)
9        for i in nums:
10            hashmap[i]+= 1
11        zeros = hashmap[0]
12        ones = hashmap[1]
13        twos = hashmap[2]
14        i = 0
15        for j in range(zeros):
16            nums[i] = 0
17            i += 1
18        for j in range(ones):
19            nums[i] = 1
20            i +=1 
21        for j in range(twos):
22            nums[i] = 2
23            i+= 1
24        