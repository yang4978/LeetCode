class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        for i in s:
            index = t.find(i,index)
            if index == -1:
                return False
            index += 1
        return True
        # res = 0
        # i = 0
        # j = 0
        # while(i<len(s) and j<len(t)):
        #     if(t[j]==s[i]):
        #         res += 1
        #         i += 1
        #     j += 1
        # return res==len(s)

        
