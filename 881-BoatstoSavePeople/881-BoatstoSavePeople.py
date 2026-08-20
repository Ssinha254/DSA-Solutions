# Last updated: 8/20/2026, 11:18:21 PM
1class Solution(object):
2    def numRescueBoats(self, people, limit):
3        """
4        :type people: List[int]
5        :type limit: int
6        :rtype: int
7        """
8        people.sort()
9        start = 0
10        end = len(people)-1
11        num = 0
12        while start <= end:
13            if (people[start] + people[end]> limit):
14                if people[end] <= limit:
15                    num+=1
16                end-=1
17            else:
18                num+=1
19                end-=1
20                start+=1
21        return num