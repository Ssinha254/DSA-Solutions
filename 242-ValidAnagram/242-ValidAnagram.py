# Last updated: 4/21/2026, 11:25:47 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st1 = {}
        for i in s:
            if i not in st1:
                st1[i] = 1
            else: st1[i] += 1
        for i in t:
            if i not in st1:
                return False
            else: st1[i] -= 1
        for i in st1.values():
            if i != 0:
                return False
        return True