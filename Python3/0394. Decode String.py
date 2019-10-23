class Solution:
    def decodeString(self, s: str) -> str:
        stack,times,result = [],0,""
        for c in s:
            if(c=='['):
                stack.append([times,result])
                times = 0
                result = ""
            elif(c==']'):
                [temp_times,temp_res] = stack.pop()
                result = temp_res + temp_times*result
            elif('0'<=c<='9'):
                times = times*10 + int(c)
            else:
                result += c
        return result
#         l = len(s)
#         encode = []
#         i = l-1
#         while i>-1:
#             if('0'<=s[i]<='9'):
#                 num = 0
#                 power = 1
#                 temp = i
#                 while(temp>=0 and '0'<=s[temp]<='9'):
#                     num += int(s[temp])*power
#                     power *= 10
#                     temp -= 1

#                 j = i+1
#                 while(j<len(s) and s[j]!=']'):
#                     j += 1
#                 s = s[:temp+1]+num*s[i+2:j]+s[j+1:]
#                 i = temp + 1
#             i -= 1
#         return s
