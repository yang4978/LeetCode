class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums,temp,res,used,l,n):
            if(l==n):
                res.append(temp[:])
                return

            for j in range(n):
                if used[j]!=True:
                    if j>0 and nums[j]==nums[j-1] and used[j-1]==False:
                        continue

                    temp.append(nums[j])
                    used[j] = True
                    l += 1
                    dfs(nums,temp,res,used,l,n)
                    used[j] = False
                    temp.pop()
                    l -= 1

        nums.sort()
        res = []
        n = len(nums)
        used = [False]*n
        temp = []
        l = 0
        dfs(nums,temp,res,used,l,n)
        
        return res
        
        
