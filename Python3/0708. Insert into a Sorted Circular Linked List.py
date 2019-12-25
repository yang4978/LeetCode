"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        temp = Node(insertVal)      # 建立以insertVal为值的节点temp

        if not head:                # 判断head是否为空节点
            temp.next = temp        # temp.next指向temp，构造循环列表
            return temp             # 返回temp

        flag = 0                    # 列表遍历标志，初始化为0
        node = head                 # 遍历所用的节点

        while 1:
            if (node.val <=insertVal and node.next.val >= insertVal) or (node.val >= node.next.val and flag == 1):

            # 前半部分讨论情况1，后半部分讨论情况2、3、4
            # 满足条件时，把temp插入node和node.next之间，结束循环

                temp.next = node.next
                node.next = temp
                break

            node = node.next        # 遍历列表中的节点
            
            if node.next == head:   # 列表经过一次完整的遍历，标志置1
                flag = 1

        return head
