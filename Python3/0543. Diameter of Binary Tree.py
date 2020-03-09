# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        def depth(node):
            if not node:
                return 0
            
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans,L+R)

            return max(L,R)+1

        depth(root)
        return self.ans
        
    # def road_length(self,root):
    #     if not root:
    #         return 0
    #     else:
    #         return 1 + max(self.road_length(root.left),self.road_length(root.right))

    # def diameterOfBinaryTree(self, root: TreeNode) -> int:
    #     return max(self.road_length(root.left) + self.road_length(root.right),self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right)) if root else 0
