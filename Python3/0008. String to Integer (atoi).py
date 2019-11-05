class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.lstrip()
        if(str==""):return 0
        
        i = 2 if str[0]=='+' or str[0]=='-' else 1
        
        res = 0
        
        while i<=len(str):
            try:
                res = int(str[:i])
                i += 1
            except:
                break
        
        return min(2**31-1,max(-2**31,res))
        
        #return min(2**31-1,max(-2**31,int(*re.findall('^[\+\-]?\d+',str.lstrip()))))
    
    
        # i = 0
        # while(i<len(str)):
        #     if(str[i]!=' '):
        #         break
        #     i+=1
        # str = str[i:]
        # if(str==""): return 0
        # if(str[0]!='-' and str[0]!="+" and str[0]<'0' or str[0]>'9'):
        #     return 0
        # i = 1
        # while(i<len(str)):
        #     if(str[i]<'0' or str[i]>'9'):
        #         break
        #     i += 1
        # if(str[i-1]<'0' or str[i-1]>'9'):
        #     return 0
        # if(str[0]=='-' and len(str)>1):
        #     return -int(str[1:i]) if -int(str[1:i])>-2147483648 else -2147483648
        # elif('0'<=str[0]<='9'):
        #     return int(str[:i]) if int(str[:i])<2147483647 else 2147483647
        # elif(str[0]=='+'):
        #     return int(str[1:i]) if int(str[:i])<2147483647 else 2147483647
        # else:
        #     return 0
