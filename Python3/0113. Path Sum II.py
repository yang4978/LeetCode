# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []

        stack = [(root,sum-root.val,[root.val])]
        res = []

        while stack:
            node,temp,arr = stack.pop()
            if(not node.left and not node.right and temp==0):
                res.append(arr)
            if node.left:
                stack.append((node.left,temp-node.left.val,arr+[node.left.val]))
            if node.right:
                stack.append((node.right,temp-node.right.val,arr+[node.right.val]))
        
        return res
