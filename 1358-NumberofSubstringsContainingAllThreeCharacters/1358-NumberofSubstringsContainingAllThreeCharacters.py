# Last updated: 6/1/2026, 12:37:36 PM
1from collections import defaultdict
2class Solution(object):
3    def numberOfSubstrings(self, s):
4        """
5        :type s: str
6        :rtype: int
7        """
8        left = 0
9        hashmap = {}
10        count = 0
11        right = 0
12        while right < len(s) and left <= right:
13            hashmap[s[right]] = hashmap.get(s[right], 0)+ 1
14            while len(hashmap) == 3:
15                count+= len(s) -right
16                hashmap[s[left]] = hashmap.get(s[left], 0)- 1
17                if hashmap[s[left]] == 0:
18                    hashmap.pop(s[left],None)
19                left+=1
20            right+=1
21        return count
22