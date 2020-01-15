from operator import truediv, mul, add, sub
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return 24*(1-0.005)<=nums[0]<=24*(1+0.005)

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                temp = [nums[k] for k in range(len(nums)) if i!=k!=j]

                if self.judgePoint24(temp+[nums[i]+nums[j]]):
                    return True

                if self.judgePoint24(temp+[abs(nums[i]-nums[j])]):
                    return True 

                if self.judgePoint24(temp+[nums[i]*nums[j]]):
                    return True
                
                if nums[i] and self.judgePoint24(temp+[nums[j]/nums[i]]):
                    return True
                
                if nums[j] and self.judgePoint24(temp+[nums[i]/nums[j]]):
                    return True

        return False

        # def allResult(arr):
        #     n = arr[0]
        #     m = arr[1]
        #     temp = set()
        #     temp.add(n+m)
        #     temp.add(abs(n-m))
        #     temp.add(n*m)
        #     if n:
        #         temp.add(m/n)
        #     if m:
        #         temp.add(n/m)
        #     return temp
        
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         arr1 = list(allResult([nums[i],nums[j]]))
        #         arr2 = list(allResult(nums[:i]+nums[i+1:j]+nums[j+1:])) 
                
        #         for a in arr1:
        #             for b in arr2:
        #                 for k in allResult([a,b]):
        #                     if 24*(1-0.005)<=k<=24*(1+0.005):
        #                         return True
                
        #         for a in arr2:
        #             arr3 = allResult([a,nums[i]])
        #             for b in arr3:
        #                 for k in allResult([b,nums[j]]):
        #                     if 24*(1-0.005)<=k<=24*(1+0.005):
        #                         return True
                
        #         for a in arr2:
        #             arr3 = allResult([a,nums[j]])
        #             for b in arr3:
        #                 for k in allResult([b,nums[i]]):
        #                     if 24*(1-0.005)<=k<=24*(1+0.005):
        #                         return True
        
        # return False
