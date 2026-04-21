# Last updated: 4/21/2026, 11:24:12 PM
from collections import deque
class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        
        queue = deque([(tickets[i], i) for i in range(len(tickets))])
        
        curr = 0 
        while len(queue) != 0:
            curr += 1
            ele, i  = queue.popleft()
            if ele > 1 :
                queue.append((ele - 1, i))
            else:
                if i == k:
                    return curr
           
             

