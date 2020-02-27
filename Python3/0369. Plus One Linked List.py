# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        fast = head
        slow = ListNode(0)
        slow.next = head
        head = slow

        while fast:
            if fast.val != 9:
                slow = fast
            fast = fast.next
        
        slow.val += 1
        cur = slow.next

        while cur:
            cur.val = 0
            cur = cur.next
        
        return head if head.val else head.next

    # def reverse_list(self,head):
    #     new_head = None
    #     cur = head

    #     while cur:
    #         t = cur.next
    #         cur.next = new_head
    #         new_head = cur
    #         cur = t
        
    #     return new_head

    # def plusOne(self, head: ListNode) -> ListNode:
    #     head = self.reverse_list(head)

    #     flag = 1
    #     node = head

    #     while node:
    #         node.val,flag = (node.val + flag)%10, (node.val+flag)//10
    #         node = node.next
        
    #     head = self.reverse_list(head)

    #     if flag:
    #         new_head = ListNode(1)
    #         new_head.next = head
    #         return new_head
    #     else:
    #         return head
