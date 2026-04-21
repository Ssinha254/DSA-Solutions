# Last updated: 4/21/2026, 11:27:53 PM
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        l = []
        def f(i, total, l):
            if total == target:
                res.append(l[:])
                return
            if i == len(candidates):
                return
            if total > target:
                return
            
            l.append(candidates[i])
            total += candidates[i]
            f(i , total, l)
            l.pop()
            total -= candidates[i]
            f(i + 1, total, l)
        f(0,0,l)
        return res