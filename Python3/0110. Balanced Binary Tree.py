# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def height(self,root):
    #     if not root:
    #         return 0
    #     return max(self.height(root.left),self.height(root.right))+1

    # def isBalanced(self, root: TreeNode) -> bool:
    #     if root == None:
    #         return True

    #     if abs(self.height(root.left)-self.height(root.right))>1:
    #         return False
        
    #     return self.isBalanced(root.left) and self.isBalanced(root.right)

    def isBalanced(self, root: TreeNode) -> bool:
        # self.res = True
        # def helper(root):
        #     if not root:
        #         return 0
        #     left = helper(root.left)+1
        #     right = helper(root.right)+1
        #     if abs(left-right)>1:
        #         self.res = False
            
        #     return max(left,right)
        # helper(root)
        # return self.res

        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)

            if left==-1 or right==-1:
                return -1
            
            return max(left,right)+1 if abs(left-right)<=1 else -1

        return helper(root)!=-1
