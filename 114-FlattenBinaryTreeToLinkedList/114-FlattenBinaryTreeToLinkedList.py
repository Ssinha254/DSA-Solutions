# Last updated: 4/21/2026, 11:27:08 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def make_list(root):
            if root is None:
                return None
            left_node = make_list(root.left)
            right_node = make_list(root.right)
          
            
            if root.left:
                left_node.right = root.right
                root.right = root.left
                root.left = None
            
            return right_node or left_node or root
        root = make_list(root)
        