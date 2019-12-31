# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root or not root.left:
            return root

        res = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root

        root.left = None
        root.right = None

        return res

        # if not root:
        #     return None

        # def visitAllLeft(stack):
        #     while stack[-1].left:
        #         stack.append(stack[-1].left)
            
        # stack = [root]
        # visitAllLeft(stack)
        # head = stack.pop()
        # res = head

        # while stack:
        #     node = stack.pop()
        #     node.left = None
        #     head.right = node
        #     while node.right:
        #         head.left = node.right
        #         node.right = None
            
        #     head = head.right
        
        # return res
