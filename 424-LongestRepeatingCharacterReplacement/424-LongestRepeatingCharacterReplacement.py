# Last updated: 4/21/2026, 11:25:28 PM
from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0
        r = 0
        maxlen = 0
        max_freq = 0
        freqmap = defaultdict(int)
        while r < len(s):
            freqmap[s[r]]+= 1
            max_freq = max(freqmap.values())
            while r - l + 1 - max_freq >k:
                freqmap[s[l]] -= 1
                l = l + 1
            maxlen = max(maxlen, r - l +1 )
            r = r + 1
        return maxlen