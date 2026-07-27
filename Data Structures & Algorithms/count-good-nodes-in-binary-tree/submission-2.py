# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        c=0
        def dfs(root,m):
            if not root:
                return 0
            c=0
            if root.val >=m:
                m=root.val
                c=1
            c += dfs(root.left,m)
            c +=dfs(root.right,m)
            return c
        return dfs(root,root.val)
             