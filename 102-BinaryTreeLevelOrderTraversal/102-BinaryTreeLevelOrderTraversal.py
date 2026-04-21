# Last updated: 4/21/2026, 11:27:16 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        q = deque()
        q.append(root)
        i = 1
        ans = []
        while(len(q) != 0):
            size = len(q)
            level = []
            for i in range(size):
                curr = q.popleft()
                level.append(curr.val)
                if (curr.left):
                    q.append(curr.left)
                if(curr.right):
                    q.append(curr.right)
            ans.append(level)
        return ans

