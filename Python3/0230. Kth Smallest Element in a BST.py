# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root
        num = []
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                num.append(node.val)
                if len(num)==k:
                    return num[-1]

                curr = node.right
        # queue = [root]
        # num = []

        # while queue:
        #     node = queue.pop(0)
        #     num.append(node.val)

        #     if node.left:
        #         queue.append(node.left)
        #     if node.right:
        #         queue.append(node.right)
            
        # num.sort()
        # return num[k-1]
