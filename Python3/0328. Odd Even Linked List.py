# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
    
        even = head.next
        odd = head
        evenHead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = evenHead

        return head

        # if not head or not head.next or not head.next.next:
        #     return head
    
        # dummy = ListNode(-1)
        # odd = dummy

        # n = 0
        # node = head
        # while node:
        #     node = node.next
        #     n += 1

        # node = head
        # while node and node.next and node.next.next:
        #     odd.next = node.next

        #     node.next = node.next.next
        #     node = node.next
        #     odd = odd.next

        # if n%2==0:
        #     odd.next = odd.next.next
        #     odd = odd.next

        # odd.next = None
        # node.next = dummy.next

        # return head
