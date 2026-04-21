# Last updated: 4/21/2026, 11:27:28 PM
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        def f(i, curr_list):
            if i == len(nums):
                res.append(curr_list[:])
                return

            curr_list.append(nums[i])
            take =  f(i + 1, curr_list)
            curr_list.pop()
            j = i
            while j < len(nums) and nums[i] == nums[j]:
                j+= 1
            not_take = f(j , curr_list)

            return
        f(0,[])
        return res
