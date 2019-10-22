class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # n = len(nums)
        # limit = sum(nums)//n
        # matrix = [limit]*(n+1)
        # for i in range(n):
        #     j = i+1
        #     temp = nums[i]
        #     while(j<n and temp+nums[j]>0):
        #         matrix[i] = max(matrix[i],temp)
        #         temp += nums[j]
        #         j += 1
        #     matrix[i] = max(matrix[i],temp)
        # return max(matrix)
        
        num_sum = 0
        result = nums[0]
        for i in nums:
            if(num_sum>0):
                num_sum += i
            else:
                num_sum = i
            result = max(result,num_sum)
        return result
        
        
