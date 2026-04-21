# Last updated: 4/21/2026, 11:24:43 PM
class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        nums1= list(nums1)
        nums2= list(nums2)
        dp = [[-1 for _ in range(len(nums2))] for _ in range(len(nums1))]

        def f(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if nums1[i] == nums2[j]:
                line = 1 + f(i + 1, j+ 1)
            else:
                line = max(f(i, j + 1),f(i + 1, j))
            dp[i][j] =line
            return dp[i][j]
        return f(0,0)

        