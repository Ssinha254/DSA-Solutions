# Last updated: 4/21/2026, 11:25:52 PM
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        answer = [1]* len(nums)
        
        curr = 1
        for i in range(len(nums)):
            answer[i] = answer[i]  * curr
            curr = curr * nums[i]
        curr = 1
        for i in range(len(nums) - 1, -1,-1):
            answer[i] = answer[i] * curr
            curr = curr * nums[i]
        
        return answer