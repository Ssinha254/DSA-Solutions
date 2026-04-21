# Last updated: 4/21/2026, 11:25:10 PM
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def check_palindrome(i, j):
            left = i
            right = j
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def helper(i,j):
            count = 0
            while i >= 0 and i < len(s) and j>=0 and j < len(s):        
                if s[i] != s[j]:
                    return count
                i -= 1
                j += 1
                count += 1
            return count

        n = len(s)
        count = 0
        for i in range(n):
            centre = s[i]
            count += helper(i, i)  
            if i+1 < n:
                count += helper(i, i+1)
        return count

