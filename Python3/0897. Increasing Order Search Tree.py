# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def increasingBST(self, root: TreeNode) -> TreeNode:
    #     def vistAllLeft(root):
    #         res = []
    #         while root:
    #             res.append(root)
    #             root = root.left
            
    #         return res
        
    #     dummy = TreeNode(-1)
    #     temp = dummy
    #     stack = vistAllLeft(root)
        
    #     while stack:
    #         node = stack.pop()
    #         temp.right = TreeNode(node.val)
    #         temp = temp.right

    #         node = node.right
    #         stack += vistAllLeft(node)
        
    #     return dummy.right
    
    
    # def increasingBST(self, root: TreeNode) -> TreeNode:
    #     if not root:
    #         return

    #     temp = dummy = TreeNode(-1)

    #     temp.right = self.increasingBST(root.left)

    #     while temp.right:
    #         temp = temp.right
        
    #     temp.right = TreeNode(root.val)
        
    #     temp.right.right = self.increasingBST(root.right)

    #     return dummy.right
    

    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        
        temp = ans = TreeNode(-1)
        temp.right = self.increasingBST(root.left)

        while temp.right:
            temp = temp.right
        
        root.left = None
        temp.right = root

        root.right = self.increasingBST(root.right)

        return ans.right

        
