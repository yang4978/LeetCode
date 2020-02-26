# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        index = 0

        node = dummy
        while index + 1 < m:
            node = node.next
            index += 1
        
        prex = node

        new_head = None
        cur = node.next
        tail = node.next
        t = None

        while index < n:
            t = cur.next
            cur.next = new_head
            new_head = cur
            cur = t
            index += 1
       
        prex.next = new_head
        if tail:
            tail.next = t

        return dummy.next
