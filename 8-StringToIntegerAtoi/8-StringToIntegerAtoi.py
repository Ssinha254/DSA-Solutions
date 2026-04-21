# Last updated: 4/21/2026, 11:28:16 PM
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s :
            return 0
        factor = 1
        ind = 0
        if s[0] == '-':
            factor = -1
            ind = 1
        elif s[0] == '+':
            ind = 1
        
       
        num = 0
        while ind < len(s) and s[ind].isdigit():
            num = num * 10 + int(s[ind])
            ind += 1
        num= num * factor
        if num > 2**31 - 1:
            return 2**31 - 1
        if num < -2**31:
            return -2**31
        return num

