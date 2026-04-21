# Last updated: 4/21/2026, 11:26:00 PM
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if  n == 0:
            return False
        return n & n - 1 == 0