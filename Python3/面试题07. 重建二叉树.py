# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
            
        num = preorder[0]
        head = TreeNode(num)

        i = inorder.index(num)

        head.left = self.buildTree(preorder[1:i+1], inorder[:i])
        head.right = self.buildTree(preorder[i+1:], inorder[i+1:])

        return head
