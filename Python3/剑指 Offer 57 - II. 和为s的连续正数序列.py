class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # res = []
        # for x in range(1,target//2+1):
        #     n = (-(2*x+1)+math.sqrt((2*x+1)**2-4*(2*x-2*target)))/2.0

        #     if n - int(n) == 0:
        #         res.append([x+i for i in range(int(n)+1)])
        
        # return res

        res = []
        l = 1
        r = 2

        while l < target//2+1:
            temp = (r-l+1)*(r+l)//2
            if temp == target:
                res.append([i for i in range(l,r+1)])
                l += 1
                r += 1
            elif temp < target:
                r += 1
            else:
                l += 1 

        
        return res
