# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:    
        if not head:
            return None
            
        pp = head
        cur = head.next
    
        while cur:
            if cur.val >= x:
                pp = pp.next

            else:
                pp.next = cur.next
                cur.next = head
                head = cur
            cur = pp.next

        
        return head

        # dummy = ListNode(-1)
        # dummy.next = head

        # node = head
        # l = 0
        # while node and node.next:
        #     node = node.next
        #     l += 1
        
        # pp = dummy
        # cur = head

        # while l>0:
        #     if cur.val >= x:
        #         pp.next = cur.next
        #         node.next = cur
        #         cur.next = None
        #         node =cur

        #     else:
        #         pp = pp.next
        #     cur = pp.next

        #     l -= 1
        
        # return dummy.next
