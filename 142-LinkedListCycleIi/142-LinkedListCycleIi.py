# Last updated: 4/21/2026, 11:26:43 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
           mpp = defaultdict(int)
           temp  = head
           while temp != None:
                if( mpp[temp] == 1):
                    return temp
                mpp[temp] += 1
                temp = temp.next
