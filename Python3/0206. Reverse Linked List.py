# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ###递归法###
        if not head or not head.next:
            return head
        
        h1 = self.reverseList(head.next)

        head.next.next = head
        
        head.next = None

        return h1

        ###递归法 笨办法###
        # if not head or not head.next:
        #     return head
        
        # h1 = self.reverseList(head.next)

        # head.next = None
        
        # node = h1
        # while node.next:
        #     node = node.next
        
        # node.next = head

        # return h1


        ###迭代法###
        # new_head = None                # 新头部
        # cur = head                     # 遍历原链表所用的节点

        # while cur:                     # 遍历链表
        #     t = cur.next               # 保存cur节点在原来链表中的下一个节点
        #     cur.next = new_head        # 由于每次新遍历的节点都是new_head的上位节点
        #                                # 因此cur.next = new_head    
        #     new_head = cur             # 重新把new_head移到头部的位置，即cur所在的位置
        #     cur = t                    # 让cur转移到原来链表的下一个节点，继续遍历
        
        # return new_head                # 最终返回new_head
