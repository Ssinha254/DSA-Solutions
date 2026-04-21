# Last updated: 4/21/2026, 11:25:30 PM
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        nums.sort()
        dp = [1 for _ in range(n)]
        hashmap = [i for i in range(n)]
        maxi = 1
       
        for i in range(n):
            for prev in range(i):
                if nums[i] % nums[prev] == 0:
                    if 1 + dp[prev] >dp[i]:
                        dp[i] = 1 + dp[prev]
                        hashmap[i] = prev
            maxi = max(maxi, dp[i])
        res = []
        index = dp.index(maxi)
        res.append(nums[index])
        for i in range(maxi - 1):
            res.append(nums[hashmap[index]])
            index = hashmap[index]
            
        return res


