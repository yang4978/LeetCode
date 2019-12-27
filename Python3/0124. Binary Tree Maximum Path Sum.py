# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    max_value = -float('inf')
    def PathSum(self,root):
        if not root:
            return -float('inf')

        l = self.PathSum(root.left)
        r = self.PathSum(root.right)

        max_path_sum = max(l,r,0) + root.val
        self.max_value = max(self.max_value, l + r + root.val, max_path_sum)
        
        return max_path_sum

    def maxPathSum(self, root: TreeNode) -> int:

        res = self.PathSum(root)
        return self.max_value

    # def PathSum(self,root):
    #     if not root:
    #         return [-float('inf'),-float('inf')]

    #     max_l, l = self.PathSum(root.left)
    #     max_r, r = self.PathSum(root.right)

    #     max_value = max(max_l, max_r, l, r, l + r + root.val, root.val)
    #     max_path_sum = max(l,r,0) + root.val
        
    #     return [max_value,max_path_sum]

    # def maxPathSum(self, root: TreeNode) -> int:
    #     res = self.PathSum(root)
    #     return max(res)
