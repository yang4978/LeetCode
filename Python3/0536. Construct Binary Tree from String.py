# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def str2tree(self, s: str) -> TreeNode:
        def insert_node(num,stack):            # 插入节点函数，在每次整数输入完成后调用
            node = TreeNode(num)               # 创建以num为值的节点node
            if stack:                          # 如果stack非空，则node节点为栈顶节点的子节点
                if not stack[-1].left:         # 如果栈顶节点没有左子树，node为其左子树
                    stack[-1].left = node
                else:
                    stack[-1].right = node     # 反之，node为其右子树
            stack.append(node)                 # 将node压入栈中
            return [None,1]                    # 返回None和1，分别作为整数num和标志flag的初始值

        num, flag, stack = None, 1, []         # 对num, flag和栈进行初始化

        for c in s:                            # 遍历s中的每一个字符c
            if c == '(':                       # 如果c=='('，且num为数字，插入节点
                if num!=None:
                    num,flag = insert_node(num,stack)
                              
            elif c == ')':
                if num!=None:                  # 如果c==')'，且num为数字，插入节点
                    num,flag = insert_node(num,stack)
                stack.pop()                    # ')'标志着该子树输入完成，因此将其弹出栈

            elif c == '-':                     # 如果有-出现，flag置为-1
                flag = -1
            
            else:                              # 如果c为数字，读入整数
                num = (num*10 + flag*int(c)) if num else flag*int(c)
        
        return stack[-1] if stack else (TreeNode(num) if num != None else None)    
                                                # 如果stack非空，返回最顶端的节点，即root
                                                # 否则，
                                                # 如果num为整数，返回以num为值的节点
                                                # 否则返回None

# class Solution:
#     def str2tree(self, s: str) -> TreeNode:
#         if s=="":                              # 当输入字符串为空时，返回None
#             return None

#         def insert_node(num,stack):            # 插入节点函数，在每次整数输入完成后调用
#             node = TreeNode(num)               # 创建以num为值的节点node
#             if stack:                          # 如果stack非空，则node节点为栈顶节点的子节点
#                 if not stack[-1].left:         # 如果栈顶节点没有左子树，node为其左子树
#                     stack[-1].left = node
#                 else:
#                     stack[-1].right = node     # 反之，node为其右子树
            
#             return [None,1,node]               # 返回None,1分别作为整数num和标志flag的初始值
#                                                # 返回node，以便压入栈中

#         num, flag, stack = None, 1, []         # 对num, flag和栈进行初始化

#         for c in s:                            # 遍历s中的每一个字符c
#             if c == '(':                       # 如果c=='('，且num为数字，插入节点
#                 if num!=None:
#                     num,flag,node = insert_node(num,stack)
#                     stack.append(node)         # 将node压入栈中
                              
#             elif c == ')':
#                 if num!=None:                  # 如果c==')'，且num为数字，插入节点
#                     num,flag,node = insert_node(num,stack)                           
#                                                # 对于该情况，为了减少压入栈和弹出栈的额外开销
#                                                # 不必将node压入栈中
                    
#                 else:
#                     stack.pop()                # num非整数，说明')'为前面节点的子树输入完成的标志
#                                                # 此时弹出的为前面的节点

#             elif c == '-':                     # 如果有-出现，flag置为-1
#                 flag = -1
            
#             else:                              # 如果c为数字，读入整数
#                 num = (num*10 + flag*int(c)) if num else flag*int(c)
        
#         return stack[-1] if stack else TreeNode(num)    # 如果stack非空，返回最顶端的节点，即root
#                                                         # 否则返回以num为值的节点


# class Solution:
#     def str2tree(self, s: str) -> TreeNode:
#         if s=="":                              # 当输入字符串为空时，返回None
#             return None

#         def insert_node(num,stack):            # 插入节点函数，在每次整数输入完成后调用
#             node = TreeNode(num)               # 创建以num为值的节点node
#             if stack:                          # 如果stack非空，则node节点为栈顶节点的子节点
#                 if not stack[-1].left:         # 如果栈顶节点没有左子树，node为其左子树
#                     stack[-1].left = node
#                 else:
#                     stack[-1].right = node     # 反之，node为其右子树
#             stack.append(node)                 # 将node压入栈中
#             return [None,1]                    # 返回None和1，分别作为整数num和标志flag的初始值

#         num, flag, stack = None, 1, []         # 对num, flag和栈进行初始化

#         for c in s:                            # 遍历s中的每一个字符c
#             if c == '(':                       # 如果c=='('，且num为数字，插入节点
#                 if num!=None:
#                     num,flag = insert_node(num,stack)
                              
#             elif c == ')':
#                 if num!=None:                  # 如果c==')'，且num为数字，插入节点
#                     num,flag = insert_node(num,stack)
#                 stack.pop()                    # ')'标志着该子树输入完成，因此将其弹出栈

#             elif c == '-':                     # 如果有-出现，flag置为-1
#                 flag = -1
            
#             else:                              # 如果c为数字，读入整数
#                 num = (num*10 + flag*int(c)) if num else flag*int(c)
        
#         return stack[-1] if stack else TreeNode(num)    # 如果stack非空，返回最顶端的节点，即root
#                                                         # 否则返回以num为值的节点
