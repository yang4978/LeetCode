# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        queue = [root]
        res = 0
        while queue:
            node = queue.pop(0)
            if(node.val >= low and node.val <= high):
                res += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            elif(node.val < low and node.right):
                queue.append(node.right)
            elif(node.val > high and node.left):
                queue.append(node.left)

        return res
