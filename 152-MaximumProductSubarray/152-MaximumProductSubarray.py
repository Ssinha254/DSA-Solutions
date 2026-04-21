# Last updated: 4/21/2026, 11:26:37 PM
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_ending = nums[0]
        min_ending = nums[0]
        if len(nums) == 1:
            return nums[0]
        result = nums[0]
        for i in range(1,len(nums)):
            
            max_temp = max(nums[i], nums[i] * max_ending, nums[i]* min_ending )
            min_temp = min(nums[i], nums[i]* min_ending, nums[i] * max_ending)
            result = max(result, max_temp)
            max_ending = max_temp
            min_ending = min_temp

        return result