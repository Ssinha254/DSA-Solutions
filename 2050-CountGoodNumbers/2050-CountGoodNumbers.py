# Last updated: 4/21/2026, 11:24:19 PM
import math 
class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n % 2 == 0:
            odd = n//2
            even = n//2
        else:
            odd = (n-1)//2
            even = (n+1)//2
        total = pow(5,even,10**9 + 7)*pow(4,odd,10**9 + 7)
        return total%(10**9 + 7)
