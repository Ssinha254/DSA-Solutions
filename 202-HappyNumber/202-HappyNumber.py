# Last updated: 4/21/2026, 11:26:20 PM
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def sum_of_squares(n):
            total = 0
            while n :
                total += (n % 10) ** 2
                n //= 10
            return total
        total = sum_of_squares(n)
        start = total
        curr = 0
        while curr != start:
            curr = sum_of_squares(total)
            if curr == 1:
                return True
            if curr< 10:
                return False
            total = curr
        return False
            