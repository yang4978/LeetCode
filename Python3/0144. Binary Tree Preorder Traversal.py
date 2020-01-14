# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        stack = []

        while root:
            stack.append(root)
            res.append(root.val)
            root = root.left

        while stack:
            node = stack.pop()
            node = node.right
            while node:
                stack.append(node)
                res.append(node.val)
                node = node.left
                
        return res

        # if not root:
        #     return []

        # t = [root.val]

        # if root.left:
        #     t += self.preorderTraversal(root.left)
        
        # if root.right:
        #     t += self.preorderTraversal(root.right)
        
        # return t

        # if not root:
        #     return []
        # return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)
