class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        l = len(nums)
        res = [0]*l

        i = 0
        j = l-1

        if a==0:
            res = [b*i+c for i in nums]
            if b<0:
                res.reverse()
            return res
        elif a<0:
            idx = 0
            delta = 1
        else:
            idx = l-1
            delta = -1

        while i<=j:
            if abs(nums[i]+b/a/2)>abs(nums[j]+b/a/2):
                res[idx] = a*nums[i]*nums[i]+b*nums[i]+c
                i += 1
            else:
                res[idx] = a*nums[j]*nums[j]+b*nums[j]+c
                j -= 1
            idx += delta
        
        return res
