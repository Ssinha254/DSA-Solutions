# Last updated: 4/21/2026, 11:26:49 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.tr = []  
        self._preorder_helper(root) 
        return self.tr

   def _preorder_helper(self, node: Optional[TreeNode]):
        if node is None:
            return
        self.tr.append(node.val)  
        self._preorder_helper(node.left)  
        self._preorder_helper(node.right)  
        
        

        