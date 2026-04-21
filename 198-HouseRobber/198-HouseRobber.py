# Last updated: 4/21/2026, 11:26:23 PM
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        prev = nums[0]
        prev2 = 0
        curr = nums[0]
        for i in range(1,len(nums)):
            take = nums[i]
            if i > 1:
                take +=  prev2
            not_take = prev
            curr = max(take, not_take)
            prev2, prev =prev,  curr
        return curr
            