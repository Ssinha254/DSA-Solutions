# Last updated: 4/21/2026, 11:27:26 PM
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp =[0] * (len(s) + 1)
        dp[len(s)] = 1
        for i in range(len(s) - 1 ,-1,-1):
            if s[i] == '0':
                dp[i] = 0
                continue
            dp[i] = dp[i + 1]
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                dp[i] += dp[i + 2]

        return dp[0]