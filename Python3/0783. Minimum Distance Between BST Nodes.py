# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        stack = []
        res = float('inf')
        last = float('inf')

        while root:
            stack.append(root)
            root = root.left
        
        while stack:
            node = stack.pop()
            res = min(res,abs(node.val-last))
            last = node.val

            node = node.right
            while node:
                stack.append(node)
                node = node.left
        
        return res
        # stack = []
        # num = []

        # while root:
        #     stack.append(root)
        #     root = root.left
        
        # while stack:
        #     node = stack.pop()
        #     num.append(node.val)

        #     node = node.right
        #     while node:
        #         stack.append(node)
        #         node = node.left
        
        # return min(num[i]-num[i-1] for i in range(1,len(num)))
