class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        
        l = len(needle)

        letter = {}
        for i in range(l-1,-1,-1):
            if needle[i] not in letter:
                letter[needle[i]] = l-i

        i = 0
        while(i+l<=len(haystack)):
            if(haystack[i:i+l]==needle):
                return i
            else:
                if i+l==len(haystack):
                    return -1
                i += letter[haystack[i+l]] if haystack[i+l] in letter else l+1
        return -1

        # if needle=="":
        #     return 0
        
        # l = len(needle)
        # for i in range(len(haystack)-l+1):
        #     if(haystack[i:i+l]==needle):
        #         return i

        # return -1            
