# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        sum_value = 0
        temp = 0
        stack = [(root,0)]

        while stack:
            node,layer = stack.pop(0)

            if temp==layer:
                sum_value += node.val
            else:
                temp = layer
                sum_value = node.val
            
            if node.left:
                stack.append((node.left,layer+1))
            
            if node.right:
                stack.append((node.right,layer+1))
            
        return sum_value
