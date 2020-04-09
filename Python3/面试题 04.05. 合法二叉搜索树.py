# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def left_max(self,root):
    #     if not root:
    #         return -float('inf')
    #     else:
    #         return max(self.left_max(root.left),self.left_max(root.right),root.val)

    # def right_min(self,root):
    #     if not root:
    #         return float('inf')
    #     else: 
    #         return min(self.right_min(root.left),self.right_min(root.right),root.val)

    # def isValidBST(self, root: TreeNode) -> bool:
        # if not root:
        #     return True
        # return self.isValidBST(root.left) and self.isValidBST(root.right) and self.left_max(root.left) < root.val < self.right_min(root.right)

    # def isValidBST(self, root: TreeNode) -> bool:
    #     value = []

    #     def visit_all_left(node):
    #         arr = []
    #         while node:
    #             arr.append(node)
    #             node = node.left
    #         return arr

    #     arr = visit_all_left(root)

    #     while arr:
    #         node = arr.pop()
    #         value.append(node.val)
    #         if node.right:
    #             node = node.right
    #             while node:
    #                 arr.append(node)
    #                 node = node.left

    #     return value == sorted(list(set(value)))
        def valid(self, left_max, right_min, root):
            if not root:
                return True
            
            if left_max >= root.val or right_min <= root.val:
                return False
            
            return self.valid(left_max, root.val ,root.left) and self.valid(root.val, right_min, root.right)

        def isValidBST(self, root: TreeNode) -> bool:
            return self.valid(-float('inf'), float('inf'), root)
