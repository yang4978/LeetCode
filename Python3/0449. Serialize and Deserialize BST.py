# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def postorder(root):
            return [root.val] + postorder(root.left) + postorder(root.right) if root else []
        
        return ' '.join(map(str, postorder(root)))

        # if not root:
        #     return ""
        # stack = []
        # s = ""

        # while root:
        #     s += ' '+str(root.val)
        #     stack.append(root)
        #     root = root.left

        # while stack:
        #     node = stack.pop()
        #     node = node.right
            
        #     while node:
        #         s += ' '+str(node.val)
        #         stack.append(node)
        #         node = node.left

        # return s
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if data == "":
            return None

        num = list(map(int,data.split()))
        preorder = num[:]
        inorder = sorted(num)

        def buildTree(preorder,inorder):
            if not preorder or not inorder:
                return None
            
            mid = preorder.pop(0)
            root = TreeNode(mid)
            index = inorder.index(root.val)
            root.left = buildTree(preorder, inorder[:index])
            root.right = buildTree(preorder,inorder[index+1:])

            return root
        
        return buildTree(preorder,inorder)

    
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
