class Solution:
    def romanToInt(self, s: str) -> int:
        # num = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        # res = 0
        # temp = 0
        # for i in reversed(s):
        #     if(num[i]>=temp):
        #         res += num[i]
        #     else:
        #         res -= num[i]
        #     temp = num[i]
        # return res
        num = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        temp = 0
        res = 0
        for i in s:
            if(num[i]>temp):
                res -= temp
            else:
                res += temp
            temp = num[i]
        res += num[s[-1]]
        return res
