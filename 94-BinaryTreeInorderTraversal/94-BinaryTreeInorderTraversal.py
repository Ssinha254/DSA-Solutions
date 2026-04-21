# Last updated: 4/21/2026, 11:27:35 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.tr = []
        self._inorder(root)
        return self.tr
    def _inorder(self, root):
        if root is None: return
        self._inorder(root.left)
        self.tr.append(root.val)
        self._inorder(root.right)
