# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        node = dummy

        while(node.next and node.next.next):
            temp = node.next #1
            node.next = node.next.next
            temp.next = node.next.next
            node.next.next = temp
            node = temp

        return dummy.next
