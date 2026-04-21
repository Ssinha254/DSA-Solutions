# Last updated: 4/21/2026, 11:25:29 PM
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        odd_present = False
        cnt = 0
        for i in counts.values():
            if i % 2 :
                cnt += i - 1
                odd_present = True
            else:
                cnt += i
        if odd_present == True:
            cnt += 1
        return cnt

                 

