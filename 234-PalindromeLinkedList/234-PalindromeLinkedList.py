# Last updated: 4/21/2026, 11:25:57 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self,head):
        if not head or not head.next:
            return True

        # Step 1: Find the middle
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev = None
        curr = slow.next  
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Step 3: Compare first and reversed second half
        first = head
        second = prev
        while second:  # only need to compare half
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True

