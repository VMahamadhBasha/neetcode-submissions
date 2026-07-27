# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d=0
        def h(root):
            if not root:
                return 0
            l=h(root.left)
            r=h(root.right)
            self.d=max(self.d,l+r)

            return 1+max(l,r)
        h(root)
        return self.d