# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d==1:
            head = TreeNode(v)
            head.left = root
            return head
        
        queue = [root]

        while queue and d>2:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            d -= 1

        while queue:
            node = queue.pop(0)

            temp = TreeNode(v)
            if node.left:
                temp.left = node.left
            node.left = temp

            temp = TreeNode(v)
            if node.right:
                temp.right = node.right
            node.right = temp
            
        return root
