# Last updated: 4/21/2026, 11:24:04 PM
class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        diff =  start ^ goal
        count = 0
        while diff != 0:
            diff = diff & diff - 1
            count += 1
        return count
