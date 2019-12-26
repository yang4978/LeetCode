# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        stack = [root]
        num = []

        def input_left(stack):
            while stack[-1].left:
                stack.append(stack[-1].left)
        
        input_left(stack)
        while stack:
            node = stack.pop()
            num.append(node.val)
            if node.right:
                stack.append(node.right)
                input_left(stack)
        
        i = 0
        j = len(num) - 1
        
        while i<j:
            if num[i] + num[j] < k:
                i += 1
            elif num[i] + num[j] >k:
                j -= 1
            else:
                return True

        return False

        # stack = [root]
        # num = []

        # def input_left(stack):
        #     while stack[-1].left:
        #         stack.append(stack[-1].left)
        
        # input_left(stack)
        # while stack:
        #     node = stack.pop()
        #     if k-node.val in num:
        #         return True
        #     num.append(node.val)
        #     if node.right:
        #         stack.append(node.right)
        #         input_left(stack)
        
        
        # return False
