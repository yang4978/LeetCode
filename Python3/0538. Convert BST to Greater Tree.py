# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        stack = []
        total = 0
        head = root
        while root:
            stack.append(root)
            root = root.right
        
        while stack:
            root = stack.pop()
            root.val += total
            total = root.val
            node = root.left
            while node:
                stack.append(node)
                node = node.right
        
        return head

    # def __init__(self):
    #     self.val = 0

    # def convertBST(self, root: TreeNode) -> TreeNode:
    #     if not root:
    #         return
    #     self.convertBST(root.right)
    #     root.val += self.val
    #     self.val = root.val
    #     self.convertBST(root.left)
    #     return root


    # def travesral(self,root):
    #     if not root:
    #         return
        
    #     self.travesral(root.right)
    #     root.val += self.val
    #     self.val = root.val
    #     self.travesral(root.left)

    # def convertBST(self, root: TreeNode) -> TreeNode:
    #     self.val = 0
    #     self.travesral(root)
    #     return root
