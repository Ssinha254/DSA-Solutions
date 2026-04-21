# Last updated: 4/21/2026, 11:24:10 PM
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for i in nums:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)
        pos_index = 0
        neg_index = 0
        for i in range(len(nums)):
            if i%2 == 0:
                nums[i] = pos[pos_index]
                pos_index += 1
            else:
                nums[i] =  neg[neg_index]
                neg_index += 1
        return nums


