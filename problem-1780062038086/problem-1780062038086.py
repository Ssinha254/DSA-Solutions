# Last updated: 5/29/2026, 7:10:38 PM
1class Solution(object):
2    def minSwaps(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        n = len(nums)
8        ones = 0
9        nums.extend(nums)
10        for i in range(n):
11            if nums[i] == 1:
12                ones += 1
13        
14        swaps = 0
15        left = 0
16        result = float('inf')
17        right = ones - 1
18        for i in range(ones):
19            if nums[i] == 0:
20                swaps += 1
21       
22        for i in range(ones,2*n):
23            if nums[left] == 0:
24                swaps -= 1
25            left += 1
26            right += 1
27            if nums[right] == 0:
28                swaps+= 1
29            result = min(result, swaps)
30        return result
31            
32
33