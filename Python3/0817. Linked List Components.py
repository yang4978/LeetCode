# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        #G = set(G)
        res = 0

        while head:
            if head.val in G and (not head.next or head.next.val not in G):
                    res += 1
            head = head.next
        
        return res

        # G = set(G)
        # flag = 0
        # res = 0

        # while head:
        #     if head.val in G:
        #         G.remove(head.val)
        #         if not flag:
        #             flag = 1
        #             res += 1
            
        #     else:
        #         flag = 0
            
        #     head = head.next
        
        # return res
