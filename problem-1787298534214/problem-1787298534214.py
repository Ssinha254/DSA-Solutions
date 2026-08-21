# Last updated: 8/21/2026, 1:18:54 PM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        i = 0
4        j = len(numbers)-1
5        while i < j:
6            if numbers[i]+numbers[j] > target:
7                j -=1
8            elif numbers[i]+numbers[j] < target:
9                i += 1
10            else:
11                return [i+1, j+1]
12       
13            