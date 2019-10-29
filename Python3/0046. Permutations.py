class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0):
            if first==n:
                output.append(nums[:])
            for i in range(first,n):
                nums[first],nums[i] = nums[i],nums[first]
                backtrack(first+1)
                nums[first],nums[i] = nums[i],nums[first]
        
        n = len(nums)
        output = []
        backtrack()
        return output
    ######         DFS          #####
    def permute(self, nums: List[int]) -> List[List[int]]:                
        n = len(nums)
        result = []
        temp = []
        used = [False]*n
        length = 0
        self.dfs(nums,temp,used,result,length,n)
        return result
    
    def dfs(self,nums,temp,used,result,length,n):
        if(length==n):
            result.append(temp[:])
            return
        
        for i in range(n):
            if not used[i]:
                temp.append(nums[i])
                used[i] = True
                self.dfs(nums,temp,used,result,length+1,n)
                used[i] = False
                temp.pop()
