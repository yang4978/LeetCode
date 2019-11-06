# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if(t1==None):
            return t2
        stack = [[t1,t2]]
        while(stack!=[]):
            t = stack.pop()
            if(t[0]==None or t[1]==None):
                continue
            t[0].val+=t[1].val
            
            if(t[0].left==None):
                t[0].left = t[1].left
            else:
                stack.append([t[0].left,t[1].left])
            
            if(t[0].right==None):
                t[0].right = t[1].right
            else:
                stack.append([t[0].right,t[1].right])
        return t1
        
    # def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    #     if(t1==None):
    #         return t2
    #     if(t2==None):
    #         return t1
    #     t1.val += t2.val
    #     t1.left = self.mergeTrees(t1.left,t2.left)
    #     t1.right = self.mergeTrees(t1.right,t2.right)
    #     return t1
    
#     def mergeNode(self,t1,t2):
#         if(t1==None and t2==None):
#             return None
#         elif(t1!=None and t2==None):
#             t3 = t1
#             return t3
#         elif(t1==None and t2!=None):
#             t3 = t2
#             return t3
#         else:
#             t3 = TreeNode(t1.val+t2.val)
#             t3.left = self.mergeNode(t1.left,t2.left)
#             t3.right = self.mergeNode(t1.right,t2.right)
#             return t3
    
#     def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
#         dummy = TreeNode(0)
#         t3 = self.mergeNode(t1,t2)
#         return t3
