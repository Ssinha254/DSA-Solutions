# Last updated: 4/21/2026, 11:27:24 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if head is None or left == right:
            return head
        def reverse_list(head, k):
            temp = head
            prev = None
            count = 0
            while temp is not None  and count < k:
                succ = temp.next
                temp.next = prev
                prev = temp
                temp = succ
                count += 1
            return prev, temp
        k = right - left + 1
        dummy = ListNode()
        prev =dummy
        dummy.next = head
        temp = head
        for i in range(left - 1):
            prev = temp
            temp = temp.next
        rev_temp, succ = reverse_list(temp , k)
        prev.next = rev_temp
        temp.next  = succ
        return dummy.next