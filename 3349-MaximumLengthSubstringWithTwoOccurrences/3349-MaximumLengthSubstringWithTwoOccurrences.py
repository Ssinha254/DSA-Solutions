# Last updated: 4/21/2026, 11:24:07 PM
from collections import Counter
class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        j  = 0
        c = Counter()
        max_len = 0

        while j < len(s):
            c[s[j]] += 1
            while c[s[j]] > 2:
                c[s[i]] -= 1
                i+=1
            max_len = max(max_len, j - i + 1)
            j+=1
        return max_len
        