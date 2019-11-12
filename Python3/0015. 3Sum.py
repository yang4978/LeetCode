class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        res = []

        for k in range(l-2):
            if(nums[k]>0):
                return res
            if(k>0 and nums[k]==nums[k-1]):
                continue
            i,j = k+1, l-1
            while(i<j):
                temp = nums[k]+nums[i]+nums[j]
                if(temp<0):
                    i += 1
                    while(i<j and nums[i]==nums[i-1]):
                        i += 1
                elif(temp>0):
                    j -= 1
                    while(i<j and nums[j]==nums[j+1]):
                        j -= 1
                else:
                    res.append([nums[k],nums[i],nums[j]])
                    i += 1
                    j -= 1
                    while(i<j and nums[i]==nums[i-1]):
                        i += 1
                    while(i<j and nums[j]==nums[j+1]):
                        j -= 1
        return res
