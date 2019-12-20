class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        def swap(nums,i,j):
            if i==j:
                return
            nums[i] = nums[i]^nums[j]
            nums[j] = nums[i]^nums[j]
            nums[i] = nums[i]^nums[j]

        n = len(nums)

        for i in range(n):
            while nums[nums[i]-1]!=nums[i]:
                swap(nums,nums[i]-1,i)
                #nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
        
        return [ i+1 for i in range(n) if nums[i] != (i+1)]
