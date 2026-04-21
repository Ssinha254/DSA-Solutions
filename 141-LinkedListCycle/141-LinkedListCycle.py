# Last updated: 4/21/2026, 11:26:48 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        mpp = defaultdict(int)
        temp  = head
        while temp != None:
            if( mpp[temp] == 1):
                return True
            mpp[temp] += 1
            temp = temp.next




        