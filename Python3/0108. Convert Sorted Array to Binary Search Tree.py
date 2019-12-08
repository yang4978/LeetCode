# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums:
            l = len(nums)
            i = l//2
            root = TreeNode(nums[i])
            root.left = self.sortedArrayToBST(nums[:i])
            root.right = self.sortedArrayToBST(nums[i+1:])
            return root
