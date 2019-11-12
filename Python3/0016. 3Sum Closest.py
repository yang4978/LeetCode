class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        nums.sort()
        for k in range(len(nums)):
            i,j = k+1,len(nums)-1

            if(k>0 and nums[k]==nums[k-1]):
                continue

            while(i<j):
                temp = nums[k]+nums[i]+nums[j]
                if(temp==target):
                    return temp
                elif(temp>target):
                    if(abs(res-target)>abs(temp-target)):
                        res = temp
                    j -= 1
                else:
                    if(abs(res-target)>abs(target-temp)):
                        res = temp
                    i += 1

        return res
