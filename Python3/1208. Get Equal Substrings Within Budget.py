class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
### Sliding Window ###
        l = 0
        r = -1
        diff = 0
        while r < len(s)-1:
            r += 1
            diff += abs(ord(s[r])-ord(t[r]))
            if diff > maxCost:
                diff -=  abs(ord(s[l])-ord(t[l]))
                l += 1
        
        return r-l+1

### Prefix sum + Binary Search ###
        # acc = [0] + list(accumulate(abs(ord(s[i])-ord(t[i])) for i,item in enumerate(s)))
        # res = 0

        # for i in range(1,1+len(s)):
        #     left = 0
        #     right = i

        #     while left<right:
        #         m = (left+right)//2
        #         if acc[i]-maxCost <= acc[m]:
        #             right = m
        #         else:
        #             left = m + 1
        #     res = max(res,i-left)

        # return res 

                
