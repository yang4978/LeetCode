# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def treeHeight(self,root):
        if not root:
            return 0
        return max(self.treeHeight(root.left),self.treeHeight(root.right))+1

    def printTree(self, root: TreeNode) -> List[List[str]]:
        stack = [(root,0,0)]
        h = self.treeHeight(root)
        res = [[""]*((1<<h)-1) for _ in range(h)]
        
        while stack:
            node,layer,num = stack.pop()
            power = 1<<(h-layer-1)
            res[layer][power-1+num*power*2] = str(node.val)

            if node.left:
                stack.append((node.left,layer+1,num<<1))
            
            if node.right:
                stack.append((node.right,layer+1,(num<<1)+1))

        return res
