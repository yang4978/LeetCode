# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root,root]

        while queue:
            r1 = queue.pop(0)
            r2 = queue.pop(0)

            if r1==None and r2==None:
                continue
            
            elif r1==None or r2==None or r1.val!=r2.val:
                return False
            
            else:
                queue.append(r1.left)
                queue.append(r2.right)
                queue.append(r1.right)
                queue.append(r2.left)
    
        return True

        # def isMirror(r1,r2):
        #     if r1==None and r2==None:
        #         return True
        #     elif r1==None or r2==None:
        #         return False
        #     else:
        #         return r1.val==r2.val and isMirror(r1.left,r2.right) and isMirror(r1.right,r2.left)

        # return isMirror(root,root)
