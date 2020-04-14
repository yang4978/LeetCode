# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        l = len(nums)

        head = TreeNode(nums[l//2])

        head.left = self.sortedArrayToBST(nums[:l//2])
        head.right = self.sortedArrayToBST(nums[l//2+1:])

        return head
