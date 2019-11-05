class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]
        # la = len(a)
        # lb = len(b)
        # a = (lb-la)*'0' + a
        # b = (la-lb)*'0' + b
        # res = ""
        # flag = 0
        # for i in range(max(la,lb)-1,-1,-1):
        #     res = str((int(a[i])+int(b[i])+flag)%2)+res
        #     flag =  (int(a[i])+int(b[i])+flag)//2
        # if(flag):
        #     res = '1'+res
        # return res
