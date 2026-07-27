# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        dq=deque()
        if not root:
            return []
        dq.append(root)
        while dq:
            l=len(dq)
            temp=[]
            for i in range(l):
                ele=dq.popleft()
                temp.append(ele.val)
                if ele.left:
                    dq.append(ele.left)
                if ele.right:
                    dq.append(ele.right)
            res.append(temp)
        return res