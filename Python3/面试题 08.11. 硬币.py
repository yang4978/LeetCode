class Solution:
    def waysToChange(self, n: int) -> int:
        f = [1]+[0]*n
        coins = [25,10,5,1]

        for c in coins:
            for i in range(c,n+1):
                f[i] += f[i-c]
        return f[-1]%1000000007

        # res = 0
        # for i in range(n//25+1):
        #     r = n - 25*i
        #     ten = r//10

        #     ## for j in range(ten+1):
        #     ##     res += (r-j*10)//5 + 1

        #     res += (ten+1)*(r//5) - ten*(ten+1) + ten+1

        # return res%1000000007
