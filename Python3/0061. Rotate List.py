# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        
        n = 1
        old_tail = head
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        
        old_tail.next = head

        new_tail = head
        t = n - k%n

        while t-1:
            new_tail = new_tail.next
            t -= 1
        
        res = new_tail.next
        new_tail.next = None

        return res


    # def treeHeight(self,head):
    #     if not head:
    #         return 0
        
    #     return self.treeHeight(head.next)+1

    # def rotateRight(self, head: ListNode, k: int) -> ListNode:
    #     if head==None:
    #         return head
    #     h = self.treeHeight(head)
    #     k %= h

    #     if k==0:
    #         return head

    #     t = h-k
    #     dummy = ListNode(-1)

    #     node = head
    #     while(t>1):
    #         node = node.next
    #         t -= 1
        
    #     dummy.next = node.next
    #     node.next = None
    #     node = dummy.next
    #     while(k-1):
    #         node = node.next
    #         k -= 1
    #     node.next = head

    #     return dummy.next
