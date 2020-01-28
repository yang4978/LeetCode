# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        left_val = []

        if root.left or root.right:
            left_val.append(root.val)

        node = root.left

        if node:
            while node.left or node.right:
                left_val.append(node.val)
                node = node.left if node.left else node.right
        
        right_val = []
        node = root.right
        if node:
            while node.left or node.right:
                right_val.append(node.val)
                node = node.right if node.right else node.left        
        
        stack = [root]
        middle = []
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                middle.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return left_val + middle + right_val[::-1]
