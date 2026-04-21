# Last updated: 4/21/2026, 11:25:16 PM
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stk = deque()
        res = []
        n = len(nums)
        for i in range(2*n -1 , -1, -1):
            while stk and stk[-1] <= nums[i%n]:
                 stk.pop()
            if i < n:
                if not stk:
                    res.append(-1)
                else:
                    res.append(stk[-1])
            stk.append(nums[i%n])
        return res[::-1]


'''
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stk = deque()
        res = []
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if j!=(n-1):
                    if nums[j] < nums[j+1]:
                        res.append(nums[j+1])
                    else:
                        res.append(-1)
                else:

                index = j % n
                while stk and stk[-1] <= nums[index-1] :
                    stk.pop()
                if j < n:
                    if len(stk) == 0:
                        res.append(-1)
                    else:
                        res.append(stk[-1])
                stk.append(nums[index])
        return res
        '''