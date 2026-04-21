# Last updated: 4/21/2026, 11:25:08 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        def inorder(root,arr):
            if root is None:
                return 
            inorder(root.left,arr)
            arr.append(root.val)
            inorder(root.right,arr)
        
        if root is None:
            return None
        
        arr = []
        inorder(root,arr)
        start = 0 
        end = len(arr) - 1
        while start < end:
            if (arr[start] + arr[end]) < k:
                start += 1
            elif (arr[start] + arr[end]) > k:
                end -= 1
            else:
                return True
        return False
        
        