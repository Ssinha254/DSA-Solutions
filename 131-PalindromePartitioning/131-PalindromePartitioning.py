# Last updated: 4/21/2026, 11:26:53 PM
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def check_palindrome(part):
            left = 0
            right = len(part) - 1
            while left <right:
                if part[left] != part[right]:
                    return False
                left += 1
                right -= 1
            return True

        def f(i, curr_list):
            if i == len(s):
                res.append(curr_list[:])
                return
            curr_word = ""
            for j in range(i , len(s)):
                curr_word = s[i:j +1]
                if check_palindrome(curr_word):
                    curr_list.append(curr_word)
                    f(j + 1, curr_list)
                    curr_list.pop()
            return
        res = []
        f(0,[])
        return res
