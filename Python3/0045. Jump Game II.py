class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        if(n==1):
            return 0
        index = 0
        step = nums[0]
        res = 1
        while(index+step<n-1):
            temp_sum = 0
            temp_id = index
            for i in range(index+step,index,-1):
                if(i+nums[i]>temp_sum):
                    temp_sum = i+nums[i]
                    temp_id = i
            res += 1
            index = temp_id
            step = nums[temp_id]
        return res
