class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def dfs(index,arr,used,s,temp,res,target):
            if s>target:
                return

            if s == target:
                res.append(temp[:])
                return
            
            for i in range(index+1,len(arr)):
                if not used[i]:
                    if i>index+1 and arr[i]==arr[i-1]:
                        continue
                    used[i] = True
                    dfs(i,arr,used,s+arr[i],temp+[arr[i]],res,target)
                    used[i] = False

        used = [False]*len(candidates)
        s = 0
        temp = []
        res = []

        dfs(-1,candidates,used,s,temp,res,target)

        return res
