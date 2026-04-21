# Last updated: 4/21/2026, 11:26:26 PM
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(32):
            res  = res << 1 | (n & 1)
            n = n >> 1
        return res