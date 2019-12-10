class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     stack = []

    #     for i in nums:
    #         if len(stack)<k:
    #             stack.append(i)
    #             stack.sort()
    #         elif i>stack[0]:
    #             stack.pop(0)
    #             stack.append(i)
    #             stack.sort()
    #     return stack[0]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap = [-float('inf')]*k
        heapq.heapify(heap)
        for i in nums:
            if i>heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,i)
        return heap[0]
