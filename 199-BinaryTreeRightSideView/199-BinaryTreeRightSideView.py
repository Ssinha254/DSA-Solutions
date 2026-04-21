# Last updated: 4/21/2026, 11:26:22 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rev_preorder(self, root, level, ans):
        if root is None:
            return ans
        if len(ans) == level:
            ans.append(root.val)
        if root.right:
            self.rev_preorder(root.right, level+1, ans)
        if root.left:
            self.rev_preorder(root.left, level+1, ans)

    def rightSideView(self, root):
        ans = []
        self.rev_preorder(root, 0, ans)
        return ans
      
        