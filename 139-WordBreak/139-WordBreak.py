# Last updated: 4/21/2026, 11:26:50 PM
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        max_len = max(len(word) for word in wordDict)
        dp = {}
        def f(i):
            if i == len(s):
               return True
            if i in dp:
                return dp[i]
            curr_word = ""
            for j in range(i,min(len(s), i + max_len)):
                curr_word  = s[i:j+1]
                if curr_word in wordDict:
                    if f(j + 1):
                        dp[i] = True
                        return True
            dp[i] = False    
            return False
                
        return f(0)




       
            
            

        