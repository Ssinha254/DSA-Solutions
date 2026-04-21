# Last updated: 4/21/2026, 11:26:25 PM
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def f(n):
            if n == 0:
                return 0
            return (n%2) + f(n // 2)

        return f(n)