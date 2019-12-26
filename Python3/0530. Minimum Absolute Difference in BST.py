# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        stack = [root]
        num = []

        def visitAllLeft(stack):
            while stack[-1].left:
                stack.append(stack[-1].left)

        visitAllLeft(stack)

        while stack:
            node = stack.pop()
            num.append(node.val)
            if node.right:
                stack.append(node.right)
                visitAllLeft(stack)
        
        return min(num[i]-num[i-1] for i in range(1,len(num)))
