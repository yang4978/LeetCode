class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i,j,flag,res = len(num1)-1,len(num2)-1,0,""
        
        while(i>=0 or j>=0):
            x = int(num1[i]) if i>=0 else 0
            y = int(num2[j]) if j>=0 else 0
            res = str((x+y+flag)%10)+res
            flag = (x+y+flag)//10
            i -= 1
            j -= 1
        if(flag): res = "1" + res
        return res
        
        # l1 = len(num1)
        # l2 = len(num2)
        # num1 = (l2-l1)*'0'+num1
        # num2 = (l1-l2)*'0'+num2
        # res = ""
        # flag = 0
        # for i in range(max(l1,l2)-1,-1,-1):
        #     temp = int(num1[i])+int(num2[i])+flag
        #     flag = (temp)//10
        #     res += str(temp%10)
        # if(flag):
        #     res += '1'
        # return res[::-1]
