# Last updated: 4/21/2026, 11:25:18 PM
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stk = deque()
        res = {}
        for i in range(len(nums2) - 1, -1, -1):
            while stk and stk[-1] <= nums2[i]:
                stk.pop()
            
            if not stk:
                res[nums2[i]] = -1  
            else:
                res[nums2[i]] = stk[-1]

            stk.append(nums2[i])
        return [res[num] for num in nums1]
        
            

        