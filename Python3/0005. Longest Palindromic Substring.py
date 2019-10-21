class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(len(s)<=1): return s
        len_s = len(s)
        result = ""
        temp = ""
        for i in range(1,len_s):
            if(s[i-1]==s[i]):     
                temp = s[i-1]+s[i]
                l = i-2
                r = i+1
                while(l>=0 and r<len_s and s[l]==s[r]):
                    temp = s[l] + temp + s[r]
                    l -= 1
                    r += 1
                if(len(temp)>len(result)):
                    result = temp
            
            temp = s[i]
            l = i-1
            r = i+1
            while(l>=0 and r<len_s and s[l]==s[r]):
                temp = s[l] + temp + s[r]
                l -= 1
                r += 1
                if(len(temp)>len(result)):
                    result = temp
        if(result==""): result = temp
        return result
