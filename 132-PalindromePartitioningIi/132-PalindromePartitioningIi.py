# Last updated: 4/21/2026, 11:26:52 PM
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        def is_palindrome(temp):
            return temp == temp[::-1]
        n = len(s)
        dp = [-1 for _ in range(n)]
        def f(i):
            if i == n :
                return 0
            if dp[i] != -1:
                return dp[i]
            temp = ""
            min_part = float('inf')
            for j in range(i,n):
                temp += s[j]
                if is_palindrome(temp) == True:
                    part = 1 + f(j + 1)
                    min_part = min(part, min_part)
            dp[i] = min_part
            return min_part
        return f(0) - 1