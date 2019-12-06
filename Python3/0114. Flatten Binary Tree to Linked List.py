# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return None 

        l = self.flatten(root.left)
        r = self.flatten(root.right)

        root.right = l
        node = root
        while node.right:
            node = node.right
        node.right = r

        root.left = None

        return root
