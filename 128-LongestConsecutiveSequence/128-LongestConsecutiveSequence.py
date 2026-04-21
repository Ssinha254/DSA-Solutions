# Last updated: 4/21/2026, 11:26:56 PM
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        count =0
        for ele in s:
            if ele - 1 not  in s:
                curr = ele
                length = 1
                while curr + 1 in s:
                    length += 1
                    curr += 1
                count = max(count, length)

        return count 
                    