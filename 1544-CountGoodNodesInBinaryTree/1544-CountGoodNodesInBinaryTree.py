# Last updated: 4/21/2026, 11:24:28 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
            """
        
        def dfs(root, highest):
           
            if root is None:
                return 0
            if root.val >= highest:
                count = 1
                highest = root.val
            else: 
                count = 0 
            count += dfs(root.left, highest)
            count += dfs(root.right, highest)
            return count
        
        count =dfs(root, root.val)
        return count