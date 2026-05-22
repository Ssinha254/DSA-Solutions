# Last updated: 5/22/2026, 8:32:18 PM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8
9class Solution(object):
10    def rob(self, root):
11        """
12        :type root: Optional[TreeNode]
13        :rtype: int
14        """
15        dp ={}
16        def f(root):
17            if root is None:
18                return 0
19            take = root.val  
20            if dp.get(root,-1) != -1:
21                return max(dp[root][0], dp[root][1])
22
23            if root.left:
24                take += f(root.left.left)+  f(root.left.right)
25            if root.right:
26                take += f(root.right.left) +f(root.right.right)
27          
28            not_take = f(root.left) + f(root.right)
29            dp[root] = [take, not_take]
30            return max(take, not_take)
31
32        return f(root)