# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        prev = head
        rear = head.next
        t = head

        while rear:
            prev.next = rear.next
            rear.next = t
            t = rear
            rear = prev.next
        
        return t
