# Last updated: 4/21/2026, 11:28:01 PM
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # Dummy node to handle edge cases
        slow = dummy
        fast = dummy

        # Move fast n+1 steps ahead so that slow stops at the node before the target
        for _ in range(n + 1):
            if fast:
                fast = fast.next

        # Move both fast and slow until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next

        # Remove the nth node
        slow.next = slow.next.next

        return dummy.next  # Return new head (in case first node is removed)
