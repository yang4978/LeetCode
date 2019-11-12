class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        res = 0
        nums.sort()
        for k in range(len(nums)):
            i,j = k+1,len(nums)-1
            while(i<j):
                if(nums[k]+nums[i]+nums[j]>=target):
                    j -= 1
                else:
                    res += (j-i)
                    i += 1
        return res
