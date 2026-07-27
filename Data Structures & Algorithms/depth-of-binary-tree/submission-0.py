# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
            if not root :
                return 0
            res=[]
            dq=deque()
            dq.append(root)
            while dq:
                temp=[]
                for i in range(len(dq)):
                    ele=dq.popleft()
                    temp.append(ele.val)
                    if ele.left:
                        dq.append(ele.left)
                    if ele.right:
                        dq.append(ele.right)
                res.append(temp)
            return len(res)