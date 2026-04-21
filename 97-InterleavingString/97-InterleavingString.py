# Last updated: 4/21/2026, 11:27:23 PM
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        dp ={}
        if len(s3) != len(s1) + len(s2):
            return False
        def f(i, j):
            k = i + j
            if k == len(s3):
                return True
            if i == len(s1) and j == len(s2):
                return False
            if (i,j) in dp :
                return dp[(i,j)]
            take, not_take = False,False
            if j < len(s2)  and s2[j] == s3[k]:
                take = f(i, j+1)
               
            if i < len(s1) and s1[i] == s3[k]:
                not_take =f(i +1, j)
            dp[(i,j)] = take or not_take
            return dp[(i,j)]
            
        return f(0,0)