# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0

        queue = [(root,[root.val])]
        res = 0

        while queue:
            node, arr = queue.pop(0)
            res += arr.count(sum)

            if node.left:
                queue.append((node.left,[node.left.val]+[node.left.val + i for i in arr]))
            
            if node.right:
                queue.append((node.right,[node.right.val]+[node.right.val + i for i in arr]))
        
        return res
