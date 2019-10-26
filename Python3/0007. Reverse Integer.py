class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        if(x<0):
            x = -x
            flag = -1
        res = 0
        while(x):
            res = res*10 + x%10
            x //= 10
        res *= flag
        if(res<-2**31 or res>2**31-1):
            res = 0
        return res
