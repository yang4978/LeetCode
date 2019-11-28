# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head
        while cur and cur.next:
            if cur.next and cur.val!=cur.next.val:
                pre = cur
                cur = cur.next
            else:
                while cur.next and cur.val == cur.next.val:
                    cur.next = cur.next.next
                pre.next = cur.next
                cur = cur.next

        return dummy.next
