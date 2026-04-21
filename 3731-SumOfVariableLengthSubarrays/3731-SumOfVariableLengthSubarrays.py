# Last updated: 4/21/2026, 11:24:14 PM
class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]
        total_sum = 0

        for i in range(n):
            start = max(0, i - nums[i])
            if start == 0:
                curr_sum = prefix[i]
            else:
                curr_sum = prefix[i] - prefix[start - 1]
            total_sum += curr_sum
        return total_sum