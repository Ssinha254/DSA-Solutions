# Last updated: 4/21/2026, 11:25:24 PM
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while(b !=0 ):
            c = (a&b) & MASK
            a = (a ^ b) & MASK
            b = ((c)<<1) & MASK
        if a > MAX_INT : return ~(a ^ MASK)
        return a