# Last updated: 4/21/2026, 11:27:36 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        less = ListNode(0)
        more = ListNode(0)
        less_head = less
        more_head = more
        temp = head
      
        while temp is not None:
            if temp.val >=x:
                more.next = temp
                more = more.next
            else:
                less.next = temp
                less = less.next
            temp = temp.next
            
        less.next = more_head.next
        more.next = None
        return less_head.next