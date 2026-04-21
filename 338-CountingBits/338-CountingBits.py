# Last updated: 4/21/2026, 11:25:32 PM
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        ans =[0,1]
        for i in range(2,n +1 ):
            ans.append(ans[i>>1] + (i & 1))
           
        return ans