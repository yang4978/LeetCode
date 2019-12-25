# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:

        dummy = ListNode(-float('inf'))
        dummy.next = head
        prev = dummy
        tail = dummy
        current = head

        while current:
            if tail.val<current.val:
                tail = current
                current = current.next
            
            else:
                tail.next = current.next

                node = dummy
                while node.next and node.next.val<current.val:
                    node = node.next

                current.next = node.next
                node.next = current
                
                current = tail.next
        
        return dummy.next
