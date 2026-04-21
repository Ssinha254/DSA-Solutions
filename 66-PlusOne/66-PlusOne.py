# Last updated: 4/21/2026, 11:27:43 PM
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] == 10:
                digits[i] = 0
                digits[i - 1] += 1
        if digits[0] == 10:
            digits[0] = 0 
            return [1] + digits
        return digits