# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        res = float('inf')

        while root:
            if abs(res-target)>abs(root.val-target):
                res = root.val

            if target<root.val:
                root = root.left
            else:
                root = root.right

        return res
