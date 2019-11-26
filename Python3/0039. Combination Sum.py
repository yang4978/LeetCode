class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(index,arr,target,temp,t_sum,res):
            if t_sum==target:
                res.append(temp[:])
                return
            
            for i in range(index,len(arr)):
                if arr[i]+t_sum<=target:
                    temp.append(arr[i])
                    dfs(i,arr,target,temp,t_sum+arr[i],res)
                    temp.pop()

        res = []
        t_sum = 0
        temp = []

        dfs(0,candidates,target,temp,t_sum,res)

        return res
