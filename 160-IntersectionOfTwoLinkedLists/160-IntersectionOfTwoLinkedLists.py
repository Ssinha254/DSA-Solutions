# Last updated: 4/21/2026, 11:26:32 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1 = headA
        temp2 = headB
        nodes = set()
        while temp1:
            nodes.add(temp1)
            temp1 = temp1.next
        while temp2:
            if temp2 in nodes:
                return temp2
            temp2 = temp2.next
        return None
