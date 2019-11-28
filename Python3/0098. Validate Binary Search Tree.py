# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def func(root,lower=-float('inf'),higher=float('inf')):
            if not root:
                return True
            
            if root.val<=lower or root.val>=higher:
                return False
            
            if not func(root.left,lower,root.val):
                return False
            if not func(root.right,root.val,higher):
                return False
            return  True
        
        return func(root)
        # def inOrderTraversal(root):
        #     if not root:
        #         return []
            
        #     return inOrderTraversal(root.left)+[root.val]+inOrderTraversal(root.right)
        
        # arr = inOrderTraversal(root)
        # for i in range(len(arr)-1):
        #     if arr[i+1]<=arr[i]:
        #         return False
        # return True
