# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        count, num = 0, 0                            # 初始化-的个数count和数字num
        stack = []                                   # 对栈进行初始化
        S += '-'                                     # 为处理最后一个数字，在S后添加'-'

        for c in S:
            if c == '-':                             # c为'-'时
                if num:                              # 如果num不为0
                    node = TreeNode(num)             # 建立新的节点
                    if count==len(stack):            # 如果count和stack长度相同
                        if stack:                    # 说明该节点是栈顶节点的左节点
                            stack[-1].left = node
                    else:                            # 如果count和stack长度不同 
                        while count<len(stack):      # 说明该节点是栈中某节点的右节点
                            stack.pop()              # 弹出栈顶节点，直到栈的长度=count
                        stack[-1].right = node       # 此时节点是栈顶的右节点

                    stack.append(node)               # 将节点加入栈顶
                    count, num = 0, 0                # 并对count和num进行初始化
                
                count += 1                           # 不论num是否为0，count都递增
                                                     # 作为对'-'的计数
            else:
                num = num*10 + int(c)                # 否则对数字进行处理
        
        return stack[0]                              # 最后返回栈底元素，即根节点
