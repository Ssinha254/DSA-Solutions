# Last updated: 4/21/2026, 11:27:42 PM
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i , j = len(a) - 1, len(b) - 1
        carry = 0 
        res = []
        while i >=0 or j >= 0 or carry:
            total = carry
            
            if i >=  0 :
                total += int(a[i])
                i -= 1
            if j >= 0 :
                total += int(b[j])
                j -= 1

            carry = total // 2
            res.append(str(total%2))
        res = ''.join(res[::-1])
        return res