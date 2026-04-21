# Last updated: 4/21/2026, 11:24:39 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        def dfs(root, parent, grandparent):
            if root is None:
                return
            total = 0
            if grandparent is not None and  grandparent.val % 2 == 0:
                total += root.val
            if root.left is not None:
                total+= dfs(root.left, root, parent)
            if root.right is not None:
                total += dfs(root.right, root, parent)
            return total

        return dfs(root, None, None)
        