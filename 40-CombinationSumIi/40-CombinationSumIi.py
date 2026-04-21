# Last updated: 4/21/2026, 11:27:51 PM
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        
        def f(i, curr_sum, curr_list):
            if curr_sum == target:
                res.append(curr_list[:])
                return
            if i == len(candidates):
                return
            if curr_sum > target:
                return
            
            if curr_sum + candidates[i] <= target:
                curr_list.append(candidates[i])
                f(i + 1, curr_sum + candidates[i], curr_list)
                curr_list.pop()
            j = i
            while j + 1 < len(candidates) and candidates[j] == candidates[j + 1]:
                j += 1
            f(j + 1, curr_sum, curr_list)
            return
        f(0,0,[])
        return res