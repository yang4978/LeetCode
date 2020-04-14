# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def height(self,root):
    #     if not root:
    #         return [0,True]
        
    #     l, l_flag = self.height(root.left)
    #     r, r_flag = self.height(root.right)
    #     return [max(l,r)+1, abs(l-r)<2 and l_flag and r_flag]

    # def isBalanced(self, root: TreeNode) -> bool:
    #     return self.height(root)[1]

    def height(self,root):
        if not root:
            return 0
        
        l = self.height(root.left)
        r = self.height(root.right)
        
        if l == -1 or r == -1 or abs(l-r) > 1:
            return -1
        
        return max(l,r) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        return self.height(root) != -1
    
