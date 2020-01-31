# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def calculateTilt(self,root):
        if not root:
            return [0,0]
        
        l_sum,l_tilt = self.calculateTilt(root.left)
        r_sum,r_tilt = self.calculateTilt(root.right)


        return [l_sum +  r_sum + root.val, abs(l_sum - r_sum) + l_tilt + r_tilt]

    def findTilt(self, root: TreeNode) -> int:
        return self.calculateTilt(root)[1]
