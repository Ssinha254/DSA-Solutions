# Last updated: 4/21/2026, 11:27:30 PM
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        counts = 2**n
        res = []
        for i in range(counts):
            gray = i ^ (i >> 1)
            res.append(gray)


        return res