class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #return [sum(1 for i in nums if i<k) for k in nums]
        l = len(nums)
        arr = sorted([(nums[i],i) for i in range(l)])
        res = [0]*l
        for i in range(1,l):
            if arr[i-1][0] != arr[i][0]:
                res[arr[i][1]] = i
            else:
                res[arr[i][1]] = res[arr[i-1][1]]
        
        return res
