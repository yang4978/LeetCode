class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:
            return 1
        
        if n==1:
            return 10

        res = 10
        temp = 81
        l = 8
        while(n>1):
            res += temp
            temp *= l
            l -= 1
            n -= 1
        return res
