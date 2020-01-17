# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traversal(self,root):
        stack = []
        leaf = []
        while root:
            stack.append(root)
            root = root.left
        
        while stack:
            node = stack.pop()

            if not node.left and not node.right:
                leaf.append(node.val)
            
            else:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
        
        return leaf
            
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.traversal(root1) == self.traversal(root2)
