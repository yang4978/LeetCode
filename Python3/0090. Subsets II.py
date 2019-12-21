class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        def trackback(arr,index):
            res.append(arr)

            if index==n:
                return

            for i in range(index,n):
                if i>index and nums[i]==nums[i-1]:
                    continue
                
                trackback(arr+[nums[i]],i+1)
        trackback([],0)
        return res
