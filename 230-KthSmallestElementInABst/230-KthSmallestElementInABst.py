# Last updated: 4/21/2026, 11:26:01 PM
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        sorted_vals = inorder(root)
        return sorted_vals[k - 1]
