# Last updated: 4/21/2026, 11:28:09 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mini = min(len(i)  for i in strs)
        res = ""
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if i == len(strs[j]) or strs[j][i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
        
        
