# Last updated: 4/21/2026, 11:27:12 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        hashmap = {val:idx for idx, val in enumerate(inorder)}
        self.pre_ind = 0
        def build(left, right):
            if left > right:
                return None

            root = TreeNode(preorder[self.pre_ind])
            self.pre_ind+= 1
            mid = hashmap[root.val]
            root.left = build(left, mid - 1)
            root.right = build(mid+1, right)
            return root

        return build(0, len(inorder)-1)

            
