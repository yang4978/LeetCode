# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None

        slow = head
        fast = head

        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow==fast:
                ptr = slow
                node = head
                while(ptr!=node):
                    ptr = ptr.next
                    node = node.next
                return ptr
                
        return None
