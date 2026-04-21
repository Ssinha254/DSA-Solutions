# Last updated: 4/21/2026, 11:28:05 PM
from itertools import combinations
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl","6": "mno","7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        def dfs(index, path):
            if index == len(digits):
                res.append(path)
                return
            letters = mapping[digits[index]]
            for l in letters:
                dfs(index + 1, path + l)
            return res
        return dfs(0, "")