class Solution:
    def countPrimes(self, n: int) -> int:
        num = [0]*n
        if(n<=2):
            return 0
        for i in range(2,int(n**0.5+1)):
            if(num[i]==0):
                num[i*i:n:i] = ((n-1-i*i)//i+1)*[1]
        return n-sum(num)-2
