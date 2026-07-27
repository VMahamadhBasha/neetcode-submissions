# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,m):
            if not root:
                return 0
            g=1 if root.val>=m else 0
            m=max(m,root.val)
            g+=dfs(root.left,m)
            g+=dfs(root.right,m)
            return g
        return dfs(root,root.val)