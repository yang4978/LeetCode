class Solution:
    def integerBreak(self, n: int) -> int:
        res = [1]*(n+1)
        for i in range(3,n+1):
            temp = 0
            for j in range(1,i):
                temp = max(temp,res[j]*(i-j),j*(i-j))
            res[i] = temp
        return res[n]
    

        # if(n==2):
        #     return 1
        # elif(n<6):
        #     return 2*(n-2)
        # else:
        #     times = n//3
        #     if(n%3==1):
        #         return pow(3,times-1)*(n%3+3)
        #     elif(n%3==2):
        #         return pow(3,times)*2
        #     else:
        #         return pow(3,times)
        
#         num = [0,1,1]
#         if(n>2):
#             for i in range(3,n+1):
#                 temp = [j*num[i-j] for j in range(1,i//2+1)] + [j*(i-j) for j in range(1,i//2+1)]
#                 num.append(max(temp))
#         return num[n]
