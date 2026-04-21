# Last updated: 4/21/2026, 11:26:10 PM
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        prev = nums[0]
        prev2 = 0
        for i in range(1,len(nums) - 1):
            take = nums[i]
            if i > 1:
                take +=  prev2
            not_take = prev
            curr1 = max(take, not_take)
            prev2, prev =prev,  curr1
        prev_1 = prev
        prev = nums[1]
        prev2 = 0
        for i in range(2,len(nums)):
            take = nums[i]
            if i > 1:
                take +=  prev2
            not_take = prev
            curr2 = max(take, not_take)
            prev2, prev =prev,  curr2
        prev_2 = prev
        res = max(prev_1, prev_2)
        return res