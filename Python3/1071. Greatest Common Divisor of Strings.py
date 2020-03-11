class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        
        l1 = len(str1)
        l2 = len(str2)

        if l1 > l2:
            a,b = l1,l2
        else:
            a,b = l2,l1
        
        while a%b != 0:
            a,b = b, a%b
        
        for i in range(b):
            if str1[i] != str2[i]:
                return ""
        
        return str1[:b]

        # l1 = len(str1)
        # l2 = len(str2)

        # if l1 > l2:
        #     a,b = l1,l2
        # else:
        #     a,b = l2,l1
        
        # while a%b != 0:
        #     a,b = b, a%b
        
        # for i in range(b):
        #     if str1[i] != str2[i]:
        #         return ""
        
        # for i in range(b,l1):
        #     if str1[i] != str1[i%b]:
        #         return ""
        
        # for i in range(b,l2):
        #     if str2[i] != str2[i%b]:
        #         return ""
        
        # return str1[:b]
