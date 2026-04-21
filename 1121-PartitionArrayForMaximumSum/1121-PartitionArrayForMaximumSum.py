# Last updated: 4/21/2026, 11:24:41 PM
class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        n = len(arr)
        dp = [-1 for _ in range(n)]
        def f(i):
            if i == n:
                return 0
            if dp[i] != -1:
                return dp[i]
            max_sum = -float('inf')
            curr = -float('inf')
            for j in range(i, min(i + k, n)):
                curr = max(curr,arr[j])
                l = j - i + 1
                total = curr * l + f(j+ 1)
                max_sum = max(max_sum, total)
            dp[i] = max_sum
            return max_sum
        return f(0)
