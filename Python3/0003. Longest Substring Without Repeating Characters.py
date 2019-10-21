class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)<=1): return len(s)
        letter = set()
        i = j = 0
        result = 0
        while(j<len(s)):
            if(s[j] in letter):
                result = max(result,j-i)
                while(s[i]!=s[j]):
                    letter.remove(s[i])
                    i += 1
                    
                i += 1  
            else:
                letter.add(s[j])
            j += 1
        result = max(result,j-i)
        return result
#         result = 0
#         for i in range(len(s)):
#             temp = {s[i]}
#             j = i+1
            
#             while(j<len(s) and s[j] not in temp):
#                 temp.add(s[j])
#                 j += 1
            
#             result = max(result,j-i)
#         return result

        
