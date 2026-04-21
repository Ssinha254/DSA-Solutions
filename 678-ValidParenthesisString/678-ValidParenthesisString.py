# Last updated: 4/21/2026, 11:25:07 PM
class Solution(object):  
            
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        min = 0
        max = 0
        for i in s:
            if i == '(':
                min += 1
                max += 1
            elif i ==')':
                min -= 1
                max -= 1
                if min < 0 and max < 0:
                    return False
                elif min < 0 and max >= 0:
                    min = 0
            if i == '*':
                min -= 1
                max += 1
                if min - 1 < 0:
                    min = 0

        if min == 0:
            return True
        else:
            return False
