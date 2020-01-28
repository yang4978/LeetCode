# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = [(root,-1)]
        flag_x = 0
        flag_y = 0
        x_father = 0
        y_father = 0

        while queue:
            for _ in range(len(queue)):
                node,father = queue.pop(0)

                if node.val == x: 
                    if flag_y:
                        return father != y_father
                    flag_x = 1
                    x_fahter = father
                
                if node.val == y:
                    if flag_x:
                        return father != x_fahter
                    flag_y = 1
                    y_father = father

                if node.left:
                    queue.append((node.left,node.val))
                
                if node.right:
                    queue.append((node.right,node.val))
            if flag_x or flag_y:
                return False
        
        return False
