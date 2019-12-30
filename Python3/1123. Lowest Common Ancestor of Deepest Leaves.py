# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getDepth(self,root):
        if not root:
            return 0,None
        
        l = self.getDepth(root.left)
        r = self.getDepth(root.right)

        if l[0]==r[0]:
            node = root
        elif l[0]>r[0]:
            node = l[1]
        else:
            node = r[1]
        
        return max(l[0],r[0])+1,node

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        return self.getDepth(root)[1]

    # def height(self,root):
    #     if not root:
    #         return 0
        
    #     return 1 + max(self.height(root.left),self.height(root.right))

    # def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
    #     h = self.height(root)

    #     stack = [(root,set()|{root})]

    #     layer = {root:1}

    #     temp = None

    #     while stack:
    #         node,s = stack.pop(0)

    #         if layer[node] == h:
    #             if temp:
    #                 temp &= s
    #             else:
    #                 temp = s
            
    #         if node.left:
    #             layer[node.left] = layer[node] + 1
    #             stack.append((node.left,s|{node.left}))
            
    #         if node.right:
    #             layer[node.right] = layer[node] + 1
    #             stack.append((node.right,s|{node.right}))

    #     max_res = 0
    #     for node in temp:
    #         if layer[node]>max_res:
    #             max_res = layer[node]
    #             res = node
        
    #     return res
