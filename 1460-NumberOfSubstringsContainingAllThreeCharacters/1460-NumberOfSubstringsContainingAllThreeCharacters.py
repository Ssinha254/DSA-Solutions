# Last updated: 4/21/2026, 11:24:29 PM
from collections import defaultdict
class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = defaultdict(int)
        i = 0
        j = 0
        count = 0
        while j < len(s) :
            hashmap[s[j]] += 1
            while hashmap['a'] >= 1 and hashmap['b'] >= 1 and hashmap['c'] >= 1:
                count += len(s)- j
                hashmap[s[i]] -= 1
                i += 1
                
            else:
                
                j += 1
        return count