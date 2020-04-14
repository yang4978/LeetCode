class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    #     temp = res = -float('inf')
    #     for num in nums:
    #         if temp < 0:
    #             temp = num
    #         else:
    #             temp += num
    #         res = max(res,temp)

    #     return res

    # def maxSubArray(self, nums: List[int]) -> int:
    #     l = len(nums)

    #     if l == 1:
    #         return nums[0]
        
    #     sumLeftSub = self.maxSubArray(nums[:l//2])
    #     sumRightSub = self.maxSubArray(nums[l//2:])

    #     left = -float('inf')
    #     temp = 0
    #     for i in range(l//2-1,-1,-1):
    #         temp += nums[i]
    #         left = max(left,temp)
        
    #     right = -float('inf')
    #     temp = 0
    #     for i in range(l//2,l):
    #         temp += nums[i]
    #         right = max(right,temp)
        
    #     return max(right + left, sumLeftSub, sumRightSub)

    def divide(self,nums,left,right):
        
        if left == right: 
            return nums[left]

        mid = (left+right)//2
        sumLeftSub = self.divide(nums,left,mid)
        sumRightSub = self.divide(nums,mid+1,right)

        leftPart = -float('inf')
        temp = 0
        for i in range(mid,left-1,-1):
            temp += nums[i]
            leftPart = max(leftPart,temp)
        
        rightPart = -float('inf')
        temp = 0
        for i in range(mid+1, right+1):
            temp += nums[i]
            rightPart = max(rightPart,temp)
        
        return max(rightPart + leftPart, sumLeftSub, sumRightSub)

    def maxSubArray(self, nums: List[int]) -> int:
        return self.divide(nums,0,len(nums)-1)
