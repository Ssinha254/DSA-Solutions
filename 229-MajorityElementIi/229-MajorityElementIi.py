# Last updated: 4/21/2026, 11:26:02 PM
from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count1 = 0
        count2 = 0
        n = len(nums)
        ele1= None
        ele2= None
        for i in range(n):
            if nums[i] == ele1:
                count1+= 1
            elif nums[i] == ele2:
                count2 += 1
            elif count1 == 0:
                ele1 = nums[i]
                count1 += 1
            elif count2 == 0:
                ele2 = nums[i]
                count2+= 1
            else:
                count1 -= 1
                count2 -= 1
        result = []
        if nums.count(ele1) > n // 3:
            result.append(ele1)
        if ele1 != ele2 and nums.count(ele2) > n // 3:
            result.append(ele2)
        return result