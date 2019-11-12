class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        l = len(nums)
        for m in range(l-3):
            if m>0 and nums[m]==nums[m-1]: continue
            if nums[m]+nums[m+1]+nums[m+2]+nums[m+3]>target: break
            if nums[m]+nums[-1]+nums[-2]+nums[-3]<target: continue


            for k in range(m+1,l-2):
                if(k>m+1 and nums[k]==nums[k-1]): continue
                if nums[m]+nums[k]+nums[k+1]+nums[k+2]>target:break
                if nums[m]+nums[k]+nums[-1]+nums[-2]<target:continue

                i,j = k+1,l-1
                if nums[m]+nums[k]+nums[i]+nums[i+1]>target:break
                while i<j:
                    if nums[i]+nums[j]+nums[k]+nums[m]>target:
                        j -= 1
                        while i<j and nums[j]==nums[j+1]:
                            j -= 1
                    elif nums[i]+nums[j]+nums[k]+nums[m]<target:
                        i += 1
                        while i<j and nums[i]==nums[i-1]:
                            i += 1
                    else:
                        res.append([nums[m],nums[k],nums[i],nums[j]])
                        i += 1
                        while i<j and nums[i]==nums[i-1]:
                            i += 1
                        j -= 1
                        while i<j and nums[j]==nums[j+1]:
                            j -= 1


        
        return res
