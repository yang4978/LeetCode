# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def recoverTree(self, root: TreeNode) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
############ Use Morris Traversal ##############
    def recoverTree(self, root: TreeNode) -> None:
        first_node = None
        second_node = None
        last_node = TreeNode(-float('inf'))

        while root:

            if not root.left:
                if root.val < last_node.val:
                    second_node = root
                    if not first_node:
                        first_node = last_node

                last_node = root

                root = root.right
            
            else:
                node = root.left
                while node.right and node.right!=root:
                    node = node.right
                
                if not node.right:
                    node.right = root
                    root = root.left

                else:
                    node.right = None
                    
                    if root.val < last_node.val:
                        second_node = root
                        if not first_node:
                            first_node = last_node

                    last_node = root
                    root = root.right

        first_node.val, second_node.val = second_node.val, first_node.val

# ############ Use Inorder Traversal ##############

#     def visitAllLeft(self,stack):
#         while stack[-1].left:
#             stack.append(stack[-1].left)

#     def recoverTree(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         stack = [root]
#         self.visitAllLeft(stack)
#         last_val = -float('inf')
#         first_node = None
#         second_node = None

#         while stack:
#             node = stack.pop()
            
#             if node.right:
#                 stack.append(node.right)
#                 self.visitAllLeft(stack)

#             if first_node and node.val<first_node.val and node.val<last_val:
#                 second_node = node
            
#             if not first_node and stack and node.val>stack[-1].val:
#                 first_node = node

#             last_val = node.val

#         first_node.val, second_node.val = second_node.val, first_node.val


############ Use Hashmap and Inorder Traversal ##############

    # def visitAllLeft(self,stack):
    #     while stack[-1].left:
    #         stack.append(stack[-1].left)

    # def recoverTree(self, root: TreeNode) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
        # arr = []
        # node_map = {}
        # stack = [root]
        # self.visitAllLeft(stack)

        # while stack:
        #     node = stack.pop()
        #     node_map[node.val] = node
        #     arr.append(node.val)

        #     if node.right:
        #         stack.append(node.right)
        #         self.visitAllLeft(stack)
        
        # sorted_arr = sorted(arr)

        # for i in range(len(arr)):
        #     if arr[i] != sorted_arr[i]:
        #         break
        
        # node_map[arr[i]].val = sorted_arr[i]
        # node_map[sorted_arr[i]].val = arr[i]
