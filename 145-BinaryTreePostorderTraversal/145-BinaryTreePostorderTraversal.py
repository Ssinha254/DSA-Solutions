# Last updated: 4/21/2026, 11:26:44 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.tr = []
        self._postorder(root)
        return self.tr
   def _postorder(self, root):
        if root is None: return
        self._postorder(root.left)
        self._postorder(root.right)
        self.tr.append(root.val)
        