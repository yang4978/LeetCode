class Solution:
    def integerBreak(self, n: int) -> int:
        num = [0,1,1]
        if(n>2):
            for i in range(3,n+1):
                temp = [j*num[i-j] for j in range(1,i//2+1)] + [j*(i-j) for j in range(1,i//2+1)]
                num.append(max(temp))
        return num[n]
