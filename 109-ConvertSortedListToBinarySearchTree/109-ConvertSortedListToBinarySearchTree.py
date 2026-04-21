# Last updated: 4/21/2026, 11:27:11 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        def find_middle(head):
            prev = None
            slow = head
            fast = head.next
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            return prev,slow
        
        def makeTree(head):
            if head is None:
                return None
            if head.next is None:
                return TreeNode(head.val)
            prev, mid = find_middle(head)
            root = TreeNode(mid.val)
            if prev:
                prev.next = None
                root.left = makeTree(head)
            else:
                root.left = None
            root.right = makeTree(mid.next)
            return root
        
        root = makeTree(head)
        return root
