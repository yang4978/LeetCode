# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        queue = [(root,1,1)]

        while queue:
            node,greatfather,father = queue.pop(0)

            if greatfather%2 == 0:
                res += node.val
            
            if node.left:
                queue.append((node.left,father,node.val))

            if node.right:
                queue.append((node.right,father,node.val))
        
        return res
