class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        dic = []
        result = []
        n = len(nums)
        
        for i in range(n):
            for j in range(i+1,n):
                if(nums[j]>=nums[i]):
                    dic.append([[nums[i],nums[j]],j])        
        
        flag = len(set(nums))==n            
        
        while(len(dic)!=0):
            arr,index = dic.pop()
            if(flag==1 or arr not in result):
                result.append(arr)
            for i in range(index+1,n):
                if(index==-1 or nums[i]>=nums[index]):
                    dic.append([arr+[nums[i]],i])
        return result
