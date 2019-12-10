# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        r = self.sortList(slow.next)
        slow.next = None
        l = self.sortList(head)

        dummy = ListNode(-1)
        node = dummy
        while l and r:
            if l.val<r.val:
                node.next = l
                l = l.next
            else:
                node.next = r
                r = r.next
            node = node.next
        
        if l:
            node.next = l
        else:
            node.next = r
        
        return dummy.next
