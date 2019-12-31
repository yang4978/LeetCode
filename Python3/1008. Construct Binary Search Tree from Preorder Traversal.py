# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        head = TreeNode(preorder.pop(0))
        stack = [head]

        while preorder:
            node = TreeNode(preorder.pop(0))

            if node.val < stack[-1].val:
                stack[-1].left = node
            else:
                while stack and node.val > stack[-1].val:
                    temp = stack.pop()
                temp.right = node
            
            stack.append(node)
        
        return head
            
