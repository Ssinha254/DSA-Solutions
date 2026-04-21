# Last updated: 4/21/2026, 11:24:11 PM
class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        dp = [-1] * len(questions)
        def f(i):
            if i >= len(questions):
                return 0 
            if dp[i] != -1:
                return dp[i]
            take = questions[i][0]+ f(i + questions[i][1]+ 1)
            nottake =  f(i + 1)
            dp[i] = max(take, nottake)
            return dp[i]

        return f(0)