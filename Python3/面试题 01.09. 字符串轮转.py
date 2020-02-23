class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)

        if l1 != l2:
            return False
        
        i = 0
        j = 0

        while i<l1:
            if s1[i]!=s2[j]:
                i += 1
                j = 0
            else:
                i += 1
                j += 1
        
        return s1[:l1-j] == s2[j:]
    
        # if len(s1) != len(s2):
        #     return False
        # else:
        #     ss = s2 + s2
        #     return s1 in ss

