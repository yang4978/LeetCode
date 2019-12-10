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
        # import heapq
        # heap = [-float('inf')]*k
        # heapq.heapify(heap)
        # for i in nums:
        #     if i>heap[0]:
        #         heapq.heappop(heap)
        #         heapq.heappush(heap,i)
        # return heap[0]
        if k > len(nums):
            return
        index = random.randint(0,len(nums)-1)
        pivot = nums[index]
        less_part = [i for i in nums[:index]+nums[index+1:] if i < pivot]
        great_part = [i for i in nums[:index]+nums[index+1:] if i >= pivot]
        if len(great_part) == k-1:
            return pivot
        elif len(great_part) > k-1:
            return self.findKthLargest(great_part,k)
        else:
            return self.findKthLargest(less_part,k-len(great_part)-1)

        # if k>len(nums):
        #     return
        # l = []
        # r = []
        # for i in nums[1:]:
        #     if i<nums[0]:
        #         l.append(i)
        #     else:
        #         r.append(i)

        # if len(r)==k-1:
        #     return nums[0]
        # elif len(r)>k-1:
        #     return self.findKthLargest(r,k)
        # else:
        #     return self.findKthLargest(l,k-len(r)-1)
