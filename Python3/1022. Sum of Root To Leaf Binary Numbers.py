# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        temp = 1
        res = 0
        stack = [(root,root.val)]

        while stack:
            node,sum_value = stack.pop(0)
            
            if not node.left and not node.right:
                res += sum_value

            if node.left:
                stack.append((node.left,sum_value*2+node.left.val))

            if node.right:
                stack.append((node.right,sum_value*2+node.right.val))

        return res%(10**9+7)
