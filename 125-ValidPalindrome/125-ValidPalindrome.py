# Last updated: 8/21/2026, 1:03:39 PM
1import re
2class Solution:
3    def isPalindrome(self, s: str) -> bool:
4        s= s.lower()
5        s = re.sub(r'[^a-z0-9]','',s)
6        s = s.replace(" ","")
7        if s == s[::-1]:
8            return True
9        return False
10