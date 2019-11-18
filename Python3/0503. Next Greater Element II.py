class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        l = len(nums)
        res = [-1]*l

        for i in range(l*2-1,-1,-1):
            while(stack and nums[stack[-1]]<=nums[i%l]):
                stack.pop()

            res[i%l] = -1 if stack==[] else nums[stack[-1]]
            
            stack.append(i%l)

        return res

        # if(nums==[]): return []

        # stack = []
        # l = len(nums)
        # res = [-1]*l

        # for i in range(l*2-1):
        #     if(nums[i%l]<nums[(i+1)%l]):
        #         if(res[i%l]==-1):
        #             res[i%l] = nums[(i+1)%l]
        #         while(stack and nums[stack[-1]]<nums[(i+1)%l]):
        #             res[stack.pop()] = nums[(i+1)%l]
        #     else:
        #         if(res[i%l]==-1):
        #             stack.append(i%l)

        # return res
