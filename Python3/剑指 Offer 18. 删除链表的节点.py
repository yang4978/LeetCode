# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        
        cur = head
        pre = head
        while cur:
            if cur.val == val:
                if cur.next:
                    cur.val = cur.next.val
                    cur.next = cur.next.next
                else:
                    pre.next = None
                return head
            
            pre = cur
            cur = cur.next
            

        # if not head:
        #     return head
        
        # if head.val == val:
        #     return head.next
        
        # pre = head
        # cur = head.next

        # while cur:
        #     if cur.val == val:
        #         pre.next = cur.next
        #         return head
            
        #     else:
        #         pre = cur
        #         cur = cur.next
