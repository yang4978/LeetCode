class Solution:
    def climbStairs(self, n: int) -> int:
        climb = [1]*(1+n)
        for i in range(2,n+1):
            climb[i] = climb[i-1]+climb[i-2]
        return climb[-1]
        # pre1 = 1
        # pre2 = 1
        # res = 1
        # while(n>=2):
        #     res = pre1+pre2
        #     pre2 = pre1
        #     pre1 = res
        #     n -= 1
        # return res
