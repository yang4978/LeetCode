class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k < 1 or k > 9 or n < (k+1)*k//2 or n >  10*k - k*(k+1)//2 : 
            return []
        
        stack = [[[i],k-1,n-i] for i in range(1,10-k+1)]
        res = []

        while stack:
            arr, num, rest = stack.pop()
            
            for i in range(arr[-1]+1,10-num+1):
                if num == 1 and i == rest:
                    res.append(arr+[i])
                elif i < rest:
                    stack.append([arr+[i],num-1,rest - i])
        
        return res
