# Last updated: 4/21/2026, 11:28:15 PM
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        return s[::] == s[::-1]
