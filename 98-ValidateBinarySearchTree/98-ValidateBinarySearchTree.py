# Last updated: 4/21/2026, 11:27:21 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def isBST(node, min_val, max_val):
            if node is None:
                return True
            if not (min_val < node.val < max_val):
                return False
            return isBST(node.left, min_val, node.val) and isBST(node.right, node.val, max_val)
        return isBST(root,-99999999999,99999999999)